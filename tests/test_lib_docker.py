"""Tests for the Docker abstraction library."""

import unittest
import os

import cbenchf.lib.docker as docker_lib


class TestCheckDockerPerms(unittest.TestCase):

    """Tests Docker lib fn that verifies correct perms for Docker socket.

    Note that there doesn't seem to be an elegant way to change uid/gid here,
    so only the tests that make sense in the current uid/gid context are run.

    """

    @unittest.skipIf(os.geteuid() == 0, "Test requires uid != 0 (not-root)")
    def test_not_permitted(self):
        """Test failure behavior wrong uid and gid.

        TODO: Also confirm that gid isn't permitted in skipIf check

        """
        with self.assertRaises(IOError):
            docker_lib.check_docker_perms()

    @unittest.skipIf(os.geteuid() != 0, "Test requires uid == 0 (root)")
    def test_permitted_by_uid(self):
        """Test success when user has same uid as Docker socket.

        TODO: Also confirm that gid isn't the owner of Docker socket in skipIf.

        """
        docker_lib.check_docker_perms()

    @unittest.skip("Not implemented")
    def test_permitted_by_gid(self):
        """Test success when user has same gid as Docker socket."""
        pass


class TestRun(unittest.TestCase):

    """Tests Docker lib fn that abstracts the `docker run` command."""

    @unittest.skipIf(os.geteuid() != 0, "Test requires uid == 0 (root)")
    def test_no_exception(self):
        """Very basic test that no exceptions are raised by run fn.

        TODO: Look up Docker image name from config.yaml.
        TODO: Extend skipIf check to check gid.

        """
        docker_lib.run("opendaylight/helium:dev")
