"""Tests for the lib module."""

import unittest
import logging

import sdnperf.lib.lib as lib


class TestGetLogger(unittest.TestCase):

    """Tests for the lib method that builds loggers."""

    @unittest.expectedFailure
    def test_type(self):
        """Confirm that the object returned is of type Logger."""
        logger = lib.get_logger()
        assert type(logger) is logging.Logger
