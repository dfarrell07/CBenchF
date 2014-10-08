"""Tests for the lib module."""

import unittest
import logging

import sdnperf.lib.lib as lib


class TestGetLogger(unittest.TestCase):

    """Tests for the lib method that builds loggers."""

    def test_type(self):
        """Confirm that the object returned is of type Logger."""
        logger = lib.get_logger()
        assert type(logger) is logging.Logger


class TestGetConfig(unittest.TestCase):

    """Tests for the lib method that loads the general program config."""

    def test_type(self):
        """Confirm that the object returned is of type Logger."""
        config = lib.get_config()
        assert type(config) is dict

    def test_invalid(self):
        """Test proper failure for fake config file."""
        with self.assertRaises(IOError):
            lib.get_config("fake.yaml")
