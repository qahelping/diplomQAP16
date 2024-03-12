import logging

import allure
from logging import StreamHandler, Formatter, FileHandler

import requests

from data.urls import DOMEN_API


class BaseServices:
    logger = None

    @allure.step('GET: {path}')
    def get(self, path):
        response = requests.get(DOMEN_API + path)
        if response.status_code == 200:
            self.logger.info('OK')
            return response.json()
        else:
            self.logger.error('Fail')
            assert False

    @allure.step('POST: {path}')
    def post(self, path, body):
        response = requests.post(DOMEN_API + path, data=body)
        if response.status_code == 200:
            # self.logger.info('OK')
            return response.json()
        else:
            # self.logger.error('Fail')
            assert False

    @allure.step('PUT: {path}')
    def put(self, path):
        response = requests.put(DOMEN_API + path)
        if response.status_code == 200:
            self.logger.info('OK')
            return response.json()
        else:
            self.logger.error('Fail')
            assert False

    @allure.step('DELETE: {path}')
    def delete(self, path, token, code):
        headers = {"Authorization": "Basic " + token}
        response = requests.delete(DOMEN_API + path, headers=headers)
        if response.status_code == code:
            # self.logger.info('OK')
            assert True
        else:
            # self.logger.error('Fail')
            assert False

    @allure.step('PATCH: {path}')
    def patch(self, path):
        response = requests.patch(DOMEN_API + path)
        if response.status_code == 200:
            self.logger.info('OK')
            return response.json()
        else:
            self.logger.error('Fail')
            assert False

    def _logger(self):
        self.logger = logging.getLogger(self.__class__.__name__)
        self.logger.setLevel(logging.DEBUG)
        handler = StreamHandler()
        handler.setFormatter(Formatter(fmt='%(asctime)s %(levelname)s %(message)s'))
        file_handler = FileHandler('logging_api.log')
        self.logger.addHandler(file_handler)
        self.logger.addHandler(handler)
