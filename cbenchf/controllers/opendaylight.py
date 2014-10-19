"""Module with abstraction of the OpenDaylight controller."""

import cbenchf.lib.lib as lib
import cbenchf.lib.docker as docker_lib


class OpenDaylight(object):

    """Abstraction of the OpenDaylight controller."""

    def __init__(self):
        """Build logger."""
        self.logger = lib.get_logger()

    def start(self):
        """API entry point for starting an ODL controller instance.

        See: https://github.com/dfarrell07/CBenchF/issues/6

        TODO: Verify that this works.

        """
        # TODO: Pull image name from config.yaml
        docker_lib.run("opendaylight/helium:dev", "./bin/start")

    def stop(self):
        """API entry point for stopping an ODL controller instance.

        See: https://github.com/dfarrell07/CBenchF/issues/6

        TODO: Verify that this works.

        """
        # TODO: Pull image name from config.yaml
        docker_lib.run("opendaylight/helium:dev", "./bin/stop")
