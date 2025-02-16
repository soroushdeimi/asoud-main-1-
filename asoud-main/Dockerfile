FROM python:3.13-alpine

# Skip rust installation and other related dependencies
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    CRYPTOGRAPHY_DONT_BUILD_RUST=1

WORKDIR /asoud

# Install runtime and build dependencies
# libffi-dev for cryptography
# libxml2-dev & libxslt-dev for lxml
# jpeg-dev zlib-dev for Pillow
# gettext for Django internationalization
# postgresql-client for PostgreSQL
RUN set -ex \
    && apk add --no-cache \
    python3-dev \
    musl-dev \
    libffi-dev \
    libxml2-dev \
    libxslt-dev \
    jpeg-dev \
    zlib-dev \
    gettext \
    postgresql-client \
    git \
    && apk add --no-cache --virtual \
    .build-deps \
    build-base \
    postgresql-dev

COPY ./requirements.txt /asoud/requirements.txt

# Create python's env and install Django's dependencies
RUN set -ex \
    # Upgrade pip, setuptools, and wheel
    && pip install --no-cache-dir --upgrade pip setuptools wheel \
    # Install Python dependencies
    && pip install --no-cache-dir -r /asoud/requirements.txt \
    # Extract runtime dependencies required by the installed packages
    && runDeps="$(scanelf --needed --nobanner --recursive /usr/local \
    | awk '{ gsub(/,/, "\nso:", $2); print "so:" $2 }' \
    | sort -u \
    | xargs -r apk info --installed \
    | sort -u)" \
    # Add runtime dependencies
    && apk add --no-cache --virtual rundeps $runDeps \
    # Remove build dependencies
    && apk del .build-deps \
    # Clean up caches to reduce image size
    && rm -rf /root/.cache /tmp/*

# TODO: Add a non-root user for better security
# RUN addgroup -S appgroup && adduser -S appuser -G appgroup
# USER appuser

COPY . /asoud

ENV VIRTUAL_ENV /env
ENV PATH /env/bin:$PATH

# Ensure the entrypoint is executable
RUN chmod +x /asoud/entrypoint.sh

# Ensure the logs directory exists and is writable
RUN mkdir -p /asoud/logs && chmod -R 755 /asoud/logs

# run entrypoint.sh
ENTRYPOINT ["/asoud/entrypoint.sh"]
