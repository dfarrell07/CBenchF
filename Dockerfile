# Base the image on Debian 7
# Picked Debian image because it's small
# https://registry.hub.docker.com/_/debian/
FROM debian:7
MAINTAINER Daniel Farrell <dfarrell@redhat.com>

# Install required software
RUN apt-get update && apt-get install -y python-pip wget
RUN wget -q --no-check-certificate "https://raw.githubusercontent.com/dfarrell07/CBenchF/master/requirements.txt" && \
    pip install -r requirements.txt && \
    rm requirements.txt

# Do the ADD as late as possible, as it invalidates cache
ADD . /opt/cbenchf
WORKDIR /opt/cbenchf

# Default to dropping into CBenchF shell
CMD ["./cbenchf/cli.py"]
