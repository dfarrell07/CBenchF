"""Module with abstraction of the OpenDaylight controller."""

import docker as docker_mod

import cbenchf.lib.lib as lib


class OpenDaylight(object):

    """Abstraction of the OpenDaylight controller."""

    def __init__(self):
        """Build logger."""
        self.logger = lib.get_logger()
        self.config = lib.get_config()
        self.docker = docker_mod.Client(base_url="unix://var/run/docker.sock",
                                        version="1.2.0",
                                        timeout=10)

    def start(self):
        """API entry point for starting an ODL controller instance.

        See: https://github.com/dfarrell07/CBenchF/issues/6

        TODO: Verify that this works.

        """
        self.docker.create_container(self.config["odl_docker_image"],
                                     detach=True)
        # TODO: Do we need to commit the container?

    def stop(self):
        """API entry point for stopping an ODL controller instance.

        See: https://github.com/dfarrell07/CBenchF/issues/6

        TODO: Verify that this works.

        """
        self.docker.create_container(self.config["odl_docker_image"],
                                     command="./bin/stop",
                                     detach=True)
        # TODO: Do we need to commit the container?

    def install_feature(self, feature):
        """Install an OpenDaylight feature using Karaf.

        :param feature: Feature to install via Karaf.
        :type feature: string

        """
        feature_install_cmd = "./bin/client feature:install {}".format(feature)
        self.docker.create_container(self.config["odl_docker_image"],
                                     command=feature_install_cmd,
                                     detach=True)
        # TODO: Do we need to commit the container?
