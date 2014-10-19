"""Module with abstraction of the OpenDaylight controller."""

import cbenchf.lib.lib as lib


class OpenDaylight(object):

    """Abstraction of the OpenDaylight controller."""

    def __init__(self):
        """Build logger."""
        self.logger = lib.get_logger()

    def start(self):
        """API entry point for starting an ODL controller instance.

        Initially, this might be done via WCBench. Would be better
        to move to something like Docker in the mid-term.

        See: https://github.com/dfarrell07/CBenchF/issues/6

        TODO: This is a stub.

        """
        pass

    def stop(self):
        """API entry point for stopping an ODL controller instance.

        Initially, this might be done via WCBench. Would be better
        to move to something like Docker in the mid-term.

        See: https://github.com/dfarrell07/CBenchF/issues/6

        TODO: This is a stub.

        """
        pass
