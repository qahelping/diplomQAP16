FROM jenkins/jenkins:lts-jdk11
USER root
RUN apt-get update && apt-get -y install wget && apt-get -y install zip && apt-get -y install unzip
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN wget https://chromedriver.storage.googleapis.com/107.0.5304.62/chromedriver_linux64.zip
RUN unzip chromedriver_linux64.zip
RUN cp chromedriver /usr/local/bin
RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
RUN apt-get update && apt-get install -y python3
RUN python3 --version
USER jenkins