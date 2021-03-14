# We're using Alpine Edge
FROM alpine:edge

#
# We have to uncomment Community repo for some packages
#
RUN sed -e 's;^#http\(.*\)/edge/community;http\1/edge/community;g' -i /etc/apk/repositories

#
# Installing Packages
#
RUN apk add --no-cache=true --update \
    coreutils \
    bash \
    build-base \
    bzip2-dev \
    curl \
    figlet \
    gcc \
    g++ \
    git \
    sudo \
    util-linux \
    libevent \
    jpeg-dev \
    libffi-dev \
    libpq \
    libwebp-dev \
    libxml2 \
    libxml2-dev \
    libxslt-dev \
    linux-headers \
    musl \
    neofetch \
    openssl-dev \
    postgresql \
    postgresql-client \
    postgresql-dev \
    openssl \
    pv \
    jq \
    wget \
    freetype \
    freetype-dev \
    python3 \
    python3-dev \
    readline-dev \
    sqlite \
    ffmpeg \
    w3m \
    libjpeg-turbo-dev \
    sqlite-dev \
    libc-dev \
    sudo \
    chromium \
    chromium-chromedriver \
    zlib-dev \
    jpeg 
    #

RUN curl https://cli-assets.heroku.com/install.sh

RUN python3 -m ensurepip3 \
    && pip3 install --upgrade pip3 setuptools \
    && rm -r /usr/lib/python*/ensurepip && \
    if [ ! -e /usr/bin/pip3 ]; then ln -s pip3 /usr/bin/pip3 ; fi && \
    if [[ ! -e /usr/bin/python ]]; then ln -sf /usr/bin/python3 /usr/bin/python; fi && \
    rm -r /root/.cache




#
# Clone repo and prepare working directory
#

RUN git clone -b sql-extended https://github.com/mkaraniya/OpenUserBot /root/userbot
RUN mkdir /root/userbot/.bin
WORKDIR /root/userbot/
ENV PATH="/root/userbot/.bin:$PATH"
WORKDIR /root/userbot/
#
# Copies session and config (if it exists)
#
COPY ./sample_config.env ./userbot.session* ./config.env* /root/userbot/

#
# Install requirements
# Install PIP packages
RUN python3 -m pip3 install --no-warn-script-location --no-cache-dir --upgrade -r requirements.txt

# Cleanup
RUN rm -rf /var/lib/apt/lists /var/cache/apt/archives /tmp

#CMD ["python3","-m","userbot"]
ENTRYPOINT ["python", "-m", "userbot"]


