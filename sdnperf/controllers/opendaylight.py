"""Module with abstraction of the OpenDaylight controller."""

import sdnperf.lib.lib as lib


class OpenDaylight(object):

    """Abstraction of the OpenDaylight controller."""

    def __init__(self):
        """Build logger."""
        self.logger = lib.get_logger()
