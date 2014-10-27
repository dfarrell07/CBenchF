"""Module with abstraction of the OpenDaylight controller."""

import docker as docker_mod

import cbenchf.lib.lib as lib


class OpenDaylight(object):

    """Abstraction of the OpenDaylight controller."""

    def __init__(self):
        """Grab logger and config, do initial Docker config."""
        # Build logger and config
        self.logger = lib.get_logger()
        self.config = lib.get_config()

        # Build a docker-py Client for issuing Docker commands
        self.docker = docker_mod.Client(version="1.2.0")
        self.logger.debug("Created docker-py Client")

        # Pull ODL Docker image (uses cache if present)
        self.docker.pull(self.config["odl_docker_image"])
        self.logger.debug("{} Docker image now local".format(
            self.config["odl_docker_image"]))

        # Create an ODL Docker container
        self.odl = self.docker.create_container(self.config["odl_docker_image"])
        self.logger.debug("Created ODL Docker container")

    def start(self):
        """API entry point for starting an ODL controller instance.

        See: https://github.com/dfarrell07/CBenchF/issues/6

        """
        self.docker.start(self.odl)

    def stop(self):
        """API entry point for stopping an ODL controller instance.

        See: https://github.com/dfarrell07/CBenchF/issues/6

        """
        self.docker.stop(self.odl)

    def install_feature(self, feature):
        """Install an OpenDaylight feature using Karaf.

        :param feature: Feature to install via Karaf.
        :type feature: string

        TODO: Verify this works.

        """
        feature_install_cmd = "./bin/client feature:install {}".format(feature)
        self.docker.create_container(self.config["odl_docker_image"],
                                     command=feature_install_cmd,
                                     detach=True)
        # TODO: Do we need to commit the container?
