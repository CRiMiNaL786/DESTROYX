
FROM python:3.8-slim-buster
RUN apt-get update && apt upgrade -y && apt-get install sudo -y

RUN apt-get install -y\
    coreutils \
    bash \
    nodejs \
    bzip2 \
    curl \
    figlet \
    gcc \
    g++ \
    git \
    aria2 \
    #util-linux \
    libevent-dev \
    libjpeg-dev \
    libffi-dev \
    libpq-dev \
    libwebp-dev \
    libxml2 \
    libxml2-dev \
    libxslt-dev \
    musl \
    neofetch \
    libcurl4-openssl-dev \
    postgresql \
    postgresql-client \
    postgresql-server-dev-all \
    #chromedriver \
    openssl \
    pv \
    jq \
    wget \
    python3 \
    python3-dev \
    python3-pip \
    libreadline-dev \
    #metasploit-framework \
    #apktool \
    #openjdk-13-jdk \
    #zipalign \
    sqlite \
    ffmpeg \
    libsqlite3-dev \
    chromium \
    zlib1g-dev \
    recoverjpeg \
    zip \
    megatools \
    libfreetype6-dev




RUN pip3 install --upgrade pip setuptools 
RUN pip3 install --upgrade pip install wheel 
RUN git clone https://github.com/Sh1vam/javes-2.0 /root/userbot
RUN mkdir /root/userbot/bin/
WORKDIR /root/userbot/
#RUN mv userbot/modules /root/userbot/modules
RUN mv userbot/javes_main/extra/apktool /usr/local/bin
RUN mv userbot/javes_main/extra/apktool.jar /usr/local/bin
#RUN mv userbot/javes_main/extra/apk.rb /usr/share/metasploit-framework/lib/msf/core/payload
RUN chmod +x /usr/local/bin/*
RUN python3 -m pip install --no-warn-script-location --no-cache-dir --upgrade -r requirements.txt
RUN sudo chmod o+r /usr/lib/python3/dist-packages/*
CMD ["python3","-m","userbot"]
