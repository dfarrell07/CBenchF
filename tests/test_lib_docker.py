"""Tests for the Docker abstraction library."""

import unittest
import os

import cbenchf.lib.docker as docker_lib

# Find gid of group that owns the Docker socket
# TODO: Pull docker socket path from config.yaml?
stat_info = os.stat("/var/run/docker.sock")
sock_uid = stat_info.st_uid
sock_gid = stat_info.st_gid

# Get gids and uid of user running this process
user_gids = os.getgroups()
user_uid = os.geteuid()


class TestCheckDockerPerms(unittest.TestCase):

    """Tests Docker lib fn that verifies correct perms for Docker socket.

    Note that there doesn't seem to be an elegant way to change uid/gid here,
    so only the tests that make sense in the current uid/gid context are run.

    I know that the logic used to check if tests can be run is a large subset
    of the work being done by the code under test, and that this is less than
    ideal. Unfortunately, I don't know of a good way to get around it for these
    types of tests. At least we get *some* code coverage by having these,
    which is better than not writing them I think.

    """

    @unittest.skipIf(user_uid == sock_uid or sock_gid in user_gids,
                     "Test requires user to not have perms for Docker socket")
    def test_not_permitted(self):
        """Test failure behavior wrong uid and gid."""
        with self.assertRaises(IOError):
            docker_lib.check_docker_perms()

    @unittest.skipUnless(user_uid == sock_uid and sock_gid not in user_gids,
                         "Requires user to have uid-only perms to Docker sock")
    def test_permitted_by_uid(self):
        """Test success when user has same uid as Docker socket."""
        # Success if no exception is raised
        docker_lib.check_docker_perms()

    @unittest.skipUnless(user_uid != sock_uid and sock_gid in user_gids,
                         "Requires user to have gid-only perms to Docker sock")
    def test_permitted_by_gid(self):
        """Test success when user has same gid as Docker socket."""
        # Success if no exception is raised
        docker_lib.check_docker_perms()

    @unittest.skipUnless(user_uid == sock_uid and sock_gid in user_gids,
                         "Requires user to have gid/uid perms to Docker sock")
    def test_permitted_by_gid_and_uid(self):
        """Test success when user has same uid and gid as Docker socket."""
        # Success if no exception is raised
        docker_lib.check_docker_perms()


class TestRun(unittest.TestCase):

    """Tests Docker lib fn that abstracts the `docker run` command."""

    @unittest.skipUnless(user_uid == sock_uid or sock_gid in user_gids,
                         "Requires user to have uid or gid perms to Dsock")
    def test_no_exception(self):
        """Very basic test that no exceptions are raised by run fn.

        TODO: Look up Docker image name from config.yaml.

        """
        docker_lib.run("opendaylight/helium:dev")
