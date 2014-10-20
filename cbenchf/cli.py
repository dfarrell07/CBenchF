#!/usr/bin/env python
"""CLI for interacting with CBenchF."""

import cmd
import os
import sys

# Makes imports relative to root of repo
new_path = [os.path.join(os.path.abspath(os.path.dirname(__file__)), "..")]
sys.path = new_path + sys.path

import cbenchf.controllers.opendaylight as odl_mod


class CLI(cmd.Cmd):

    """CLI for intracting with CBenchF."""

    prompt = "cbenchf$ "

    def __init__(self):
        """"""
        # Call superclass __init__ (required by cmd.Cmd)
        cmd.Cmd.__init__(self)

        # Build instance of ODL abstraction
        self.odl = odl_mod.OpenDaylight()

    def do_start_odl(self, raw_args):
        """Start an OpenDaylight controller.

        :param raw_args: Mandatory param for Cmd handler, not used.
        :type raw_args: string

        """
        self.odl.start()

    def help_start_odl(self):
        """Provide help message for start_odl command."""
        print("start_odl")
        print("\tStart an OpenDaylight controller.")

    def do_stop_odl(self, raw_args):
        """Stop the OpenDaylight controller.

        :param raw_args: Mandatory param for Cmd handler, not used.
        :type raw_args: string

        """
        self.odl.stop()

    def help_stop_odl(self):
        """Provide help message for stop_odl command."""
        print("stop_odl")
        print("\tStop the OpenDaylight controller.")

    def do_shell(self, cmd):
        """Allows normal shell commands to be run.

        :param cmd: Everything after "shell" or "!", to be passed to shell.
        :type cmd: string

        """
        os.system(cmd)

    def help_shell(self):
        """Provide help message for shell command."""
        print("!|shell <command>")
        print("\tSend command to underlying system shell (like Bash/ZSH).")

    def do_EOF(self, raw_args):
        """Cleans up when ctrl+d is used to exit CLI.

        TODO: Add any future clean-up (closing controller) here.

        :param raw_args: Mandatory param for Cmd handler, not used.
        :type raw_args: string

        """
        return True

    def help_EOF(self):
        """Provide help message for EOF (ctrl+d) command."""
        print("ctrl+d")
        print("\tClean up and close CLI cleanly.")

    def help_help(self):
        """Provide help message for help command."""
        print("help [command]")
        print("\tProvide help on given command. If no arg, list commands.")

if __name__ == "__main__":
    CLI().cmdloop()
