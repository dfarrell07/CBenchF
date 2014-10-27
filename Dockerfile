# Base the image on Debian 8 (Jessie)
# Picked Debian image because it's small
# Need 8 (not released) because Docker-in-Docker requires 3.14 kernel
# https://registry.hub.docker.com/_/debian/
FROM debian:jessie
MAINTAINER Daniel Farrell <dfarrell@redhat.com>

# Install required software
RUN apt-get update && apt-get install -y python-pip wget docker.io
RUN wget -q --no-check-certificate "https://raw.githubusercontent.com/dfarrell07/CBenchF/master/requirements.txt" && \
    pip install -r requirements.txt && \
    rm requirements.txt

# Do the ADD as late as possible, as it invalidates cache
ADD . /opt/cbenchf
WORKDIR /opt/cbenchf

# Default to dropping into CBenchF shell
CMD ["./cbenchf/cli.py"]
