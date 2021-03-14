FROM python:3-slim-buster

RUN apt update && apt upgrade -y && \
    apt install --no-install-recommends -y \
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
    # musl-dev \
    atomicparsley \
    && rm -rf /var/lib/apt/lists /var/cache/apt/archives /tmp

COPY . /usr/src/app/OpenUserBot/
WORKDIR /usr/src/app/OpenUserBot/

# "Dirty Fix" for Heroku Dynos to track updates via 'git'.
# Fork/Clone maintainers may change the clone URL to match
# the location of their repository. [#ThatsHerokuForYa!]
RUN if [ ! -d /usr/src/app/OpenUserBot/.git ] ; then \
    git clone "https://github.com/mkaraniya/OpenUserBot.git" /tmp/dirty/OpenUserBot/ && \
    mv -v -u /tmp/dirty/OpenUserBot/.git /usr/src/app/OpenUserBot/ && \
    rm -rf /tmp/dirty/OpenUserBot/; \
    fi

# Install PIP packages
RUN python3 -m pip install --no-warn-script-location --no-cache-dir --upgrade -r requirements.txt

# Cleanup
RUN rm -rf /var/lib/apt/lists /var/cache/apt/archives /tmp

ENTRYPOINT ["python", "-m", "userbot"]
