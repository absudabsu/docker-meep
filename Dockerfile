FROM ubuntu:14.04
MAINTAINER Abhejit Rajagopal <rajagopal.abhejit@gmail.com>

RUN apt-get update && \
apt-get install -y wget vim git tcl && \
apt-get install -y swig python-dev python-numpy python-scipy python-matplotlib && \
apt-get install -y guile-2.0-dev autoconf zlib1g pkg-config && \
apt-get install -y libgsl0ldbl libhdf5-openmpi-dev && \
apt-get install -y harminv fftw-dev && \
apt-get install -y openmpi-bin openmpi-doc libopenmpi-dev && \
cd /home && git clone https://github.com/FilipDominec/python-meep-install.git && cd python-meep-install && ./python-meep-install.sh && cd .. && rm -rf python-meep-install

RUN mkdir /home/hostSRC
VOLUME /home/hostSRC
