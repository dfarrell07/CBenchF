"""Tests for the module that abstracts the OpenDaylight controller."""

import unittest

import sdnperf.lib.lib as lib
import sdnperf.controllers.opendaylight as odl


class TestInit(unittest.TestCase):

    """Test building the ODL abstraction."""

    def test_basic(self):
        """Test a basic, all default construction."""
        odl.OpenDaylight()
