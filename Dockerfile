FROM python:3.13

# 1. Устанавливаем системные зависимости: Git, Java, сертификаты и библиотеки для Chrome
RUN apt-get update && apt-get install -y tini git wget unzip curl gnupg jq default-jre ca-certificates libnss3 libatk1.0-0 libatk-bridge2.0-0 libcups2 libdrm2 libxcomposite1 libxdamage1 libxrandr2 libgbm1 libasound2 && rm -rf /var/lib/apt/lists/*

# 2. Установка Chrome (собираем ссылку по частям. чарм не хочет воспринимать длинную ссылку и упорно делит на курски при попытке сборки образа)
RUN P1="https://storage.googleapis.com" && \
    P2="/chrome-for-testing-public/134.0.6998.35/linux64" && \
    P3="/chrome-linux64.zip" && \
    wget --no-check-certificate -q -O /tmp/chrome.zip "${P1}${P2}${P3}" && \
    unzip -q /tmp/chrome.zip -d /opt/ && \
    ln -s /opt/chrome-linux64/chrome /usr/local/bin/google-chrome && \
    rm /tmp/chrome.zip

# 3. Установка ChromeDriver (собираем ссылку по частям по той же причине. см.п.2)
RUN P1="https://storage.googleapis.com" && \
    P2="/chrome-for-testing-public/134.0.6998.35/linux64" && \
    P3="/chromedriver-linux64.zip" && \
    wget --no-check-certificate -q -O /tmp/chromedriver.zip "${P1}${P2}${P3}" && \
    unzip -q /tmp/chromedriver.zip -d /opt/ && \
    ln -s /opt/chromedriver-linux64/chromedriver /usr/local/bin/chromedriver && \
    rm /tmp/chromedriver.zip

# 4. Скачиваем и устанавливаем Allure CLI (через Node.js)
RUN apt-get update && apt-get install -y nodejs npm && npm install -g allure-commandline --save-dev && ln -s /usr/local/bin/allure /usr/bin/allure

# Устанавливаем рабочую директорию
WORKDIR /app

# 5. Устанавливаем Python-библиотеки
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# 6. Копируем файлы проекта
COPY . /app

# 7. Точка входа: tini следит за процессами, чтобы джоба не висла
ENTRYPOINT ["/usr/bin/tini", "--"]

# Запуск тестов по умолчанию
CMD ["pytest", "--alluredir=allure-results", "-v"]