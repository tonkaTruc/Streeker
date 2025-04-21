FROM ubuntu:22.04

USER root
ENV PATH="/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/root/.local/bin"

RUN apt-get update && apt-get -y --no-install-recommends install \
    sudo \
    vim \
    wget \
    build-essential \
    pkg-config \
    curl

# Install GStreamer and its dependencies
RUN apt-get -y --no-install-recommends install \
    git \
    cmake \
    autoconf \
    automake \
    libtool \
    gstreamer-1.0 \
    gstreamer1.0-dev \
    libgstreamer1.0-0 \
    gstreamer1.0-plugins-base \
    gstreamer1.0-plugins-good \
    gstreamer1.0-plugins-bad \
    gstreamer1.0-plugins-ugly \
    gstreamer1.0-libav \
    # gstreamer1.0-doc \
    gstreamer1.0-tools \
    gstreamer1.0-x \
    gstreamer1.0-alsa \
    gstreamer1.0-gl \
    gstreamer1.0-gtk3 \
    gstreamer1.0-qt5 \
    gstreamer1.0-pulseaudio \
    # python-gst-1.0 \
    libgirepository1.0-dev \
    libgstreamer-plugins-base1.0-dev \
    libcairo2-dev \
    gir1.2-gstreamer-1.0 \
    python3-gi \
    python-gi-dev

RUN apt-get install -y python3 \
    python3-pip \
    python3-dev

# Install Poetry
RUN curl -sSL https://install.python-poetry.org | python3 -
RUN poetry config virtualenvs.create false

# Copy application code and install dependencies
RUN mkdir -p /home/app
COPY . /home/app
RUN cd /home/app && poetry install
