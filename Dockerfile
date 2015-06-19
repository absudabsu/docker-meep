FROM ubuntu:12.04
MAINTAINER Abhejit Rajagopal <rajagopal.abhejit@gmail.com>

RUN apt-get update && \
apt-get install -y wget vim git tcl && \
apt-get install -y swig python-dev python3 python-numpy python-scipy python-matplotlib && \
apt-get install -y guile-2.0 autoconf zlib1g pkg-config && \
apt-get install -y libatlas-base-dev liblapack-dev libblas-dev libblas-doc liblapack-doc && \
apt-get install -y harminv fftw-dev hdf5-tools libgsl0ldbl libhdf5-mpi-dev libhdf5-mpich2-dev libhdf5-openmpi-dev libhdf5-doc && \
apt-get install -y libibnetdisc-dev openmpi-bin openmpi-doc libopenmpi-dev && \
apt-get install -y libcr-dev mpich2 mpich2-doc && \
apt-get clean

RUN cd /home && git clone https://github.com/FilipDominec/python-meep-install.git && cd python-meep-install && ./python-meep-install.sh && cd .. && rm -rf python-meep-install

RUN mkdir /home/hostSRC
VOLUME /home/hostSRC


##########################################
## real here
FROM ubuntu:12.04
MAINTAINER Abhejit Rajagopal <rajagopal.abhejit@gmail.com>

apt-get update && \
apt-get install -y wget vim git tcl &&
apt-get install -y swig python-dev python-numpy python-scipy python-matplotlib && \
apt-get install -y guile-2.0-dev autoconf zlib1g pkg-config && \
apt-get install -y libgsl0ldbl libhdf5-openmpi-dev && \
apt-get install -y harminv fftw-dev && \
apt-get install -y openmpi-bin openmpi-doc libopenmpi-dev && \
cd /home && git clone https://github.com/FilipDominec/python-meep-install.git && cd python-meep-install && ./python-meep-install.sh && cd .. && rm -rf python-meep-install

RUN mkdir /home/hostSRC
VOLUME /home/hostSRC
