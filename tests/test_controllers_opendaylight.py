"""Tests for the module that abstracts the OpenDaylight controller."""

import unittest

import cbenchf.controllers.opendaylight as odl_mod


class TestInit(unittest.TestCase):

    """Test building the ODL abstraction."""

    @unittest.skip("Travis doesn't have Docker")
    def test_basic(self):
        """Test a basic, all default construction."""
        odl_mod.OpenDaylight()


class TestStart(unittest.TestCase):

    """Test starting an OpenDaylight controller instance"""

    def setUp(self):
        """Build an ODL abstraction."""
        self.odl = odl_mod.OpenDaylight()

    @unittest.skip("Travis doesn't have Docker")
    def test_present(self):
        """Confirm that the start method is present. Required API method."""
        hasattr(self.odl, "start") and callable(getattr(self.odl, "start"))


class TestStop(unittest.TestCase):

    """Test stopping an OpenDaylight controller instance"""

    def setUp(self):
        """Build an ODL abstraction."""
        self.odl = odl_mod.OpenDaylight()

    @unittest.skip("Travis doesn't have Docker")
    def test_present(self):
        """Confirm that the stop method is present. Required API method."""
        hasattr(self.odl, "stop") and callable(getattr(self.odl, "stop"))
