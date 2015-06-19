# docker-meep
containerized meep (fdtd) application, for scientific computing

This docker image provides a clean install of Ubuntu 14.04, MEEP, and python-meep built with openmpi. The purpose of this software is to save useres the time and hassle of installing MEEP with python bindings. If it works... well here it is!

MEEP: http://ab-initio.mit.edu/wiki/index.php/Meep

python-meep: https://launchpad.net/python-meep

python-meep src: https://github.com/FilipDominec/python-meep-install


## Usage:

#### pull docker image
docker pull sirgogo/meep-fdtd

OR you can build it yourself, as follows:

###### build docker image
-> install docker on your local (HOST) machine

-> git clone https://github.com/sirgogo/docker-meep.git && cd docker-meep

-> docker build -t meepdocker .

#### start a session
docker run -it -v /HOSTdirectory:/home/hostSRC -p 2222:22 meepdocker \# with access to HOST files and a port mapping HOSTip:2222 to meepdockerIP:22

#### enjoy!
python siex.py

#### some useful commands
docker run -i -t ubuntu:14.04 /bin/bash \# get initial image to set up everything

docker ps -a \# lists available dockers (-a list of non running containers, without -a, running ones)

docker build -t meepdocker . \# makes a docker image with local Dockerfile and tag meepdocker

sudo docker run -it -v /home/Documents:/home/hostSRC -p 2222:22 meepdocker \# open ports and link folder

docker docker start -i id \# starts the docker (-i means interactive (like bash), you should use this after the first time

## Notes on setup:
Ideally, there are very few apps running in the docker, so its very lightweight. In my implementation, I run an extra ssh server so I can forward GUI windows to my host. Potentially, we could work around this by performing a "xhost +" on the HOST and simply setting the display variable "export DISPLAY=HOSTip:0", but it didn't seem to work for me. So ssh was the way to go.

#### ps -aux
USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND

root         1  0.0  0.0  18180  3200 ?        Ss   18:36   0:00 /bin/bash

root       857  0.0  0.0  61372  3128 ?        Ss   18:44   0:00 /usr/sbin/sshd

root       900  0.0  0.0  15572  2128 ?        R+   18:55   0:00 ps -aux

Obviously if you log in via ssh, there would be another bash open. Also if you open python, meep, etc.. 

#### setup of ssh inside meepdocker
apt-get install -y openssh-server && update-rc.d ssh defaults && service ssh restart && service ssh status
