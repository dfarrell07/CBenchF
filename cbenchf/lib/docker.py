"""Abstraction for interactions with Docker and DockerHub."""

import subprocess
import os
import sys


def check_docker_perms():
    """Checks if the current user has permision to access Docker socket.

    Only root, a member of the docker group or a member of the group given
    to the Docker deamion with -G can work with Docker. In other words, the
    Docker socket (/var/run/docker.sock) must be owned by the user or a
    group the user belongs to.

    See: http://goo.gl/f5NvXQ

    TODO: Check if user is member of any group that owns socket, not just root.

    I would raise a PermissionError here, but trying to be Python 2.7
    compatible.

    :raises IOError: Need to be root to access Docker socket

    """
    if os.geteuid() != 0:
        err_msg = "Error: Must be root to interact with Docker socket"
        sys.stderr.write(err_msg)
        raise IOError(err_msg)


def run(image_name, detached=True):

    """Runs, using `docker run`, the given image.

    Note that the image will be pulled down from DockerHub if it isn't
    stored locally. This is handled by Docker automatically.

    TODO: Pull default image_name from config.yaml.

    :param image_name: Full name of the image to run.
    :type image_name: string

    """
    # Confirm that the user has permission to access the Docker socket
    check_docker_perms()

    # Build list describing the run command for the Docker process to execute
    params = ["run"]
    if detached:
        params.append("-d")
    params.append(image_name)

    # Spawn subprocess to execute Docker run command
    subprocess.check_call(["docker"] + params)
