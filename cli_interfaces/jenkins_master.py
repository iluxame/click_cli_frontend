#!/usr/bin/env python
import click
from lib.cli_common import BaseCLI


class JenkinsMasterCLI(BaseCLI):

    SUB_GROUP_COMMANDS = ['setup']
    SUB_GROUP_NAME = 'jenkins_master'

    @staticmethod
    @click.group(subcommand_metavar='COMMAND [OPTIONS]',
                 context_settings=BaseCLI.CONTEXT_SETTINGS)
    @BaseCLI.context()
    def jenkins_master(ctx, **kwargs):
        """
        jenkins_master provisioner help message
        """
        ctx.config_dict.update(**kwargs)
        # DEBUG INFO
        click.echo(ctx.config_dict)

    @staticmethod
    @click.command()
    @BaseCLI.context()
    def setup(ctx, **kwargs):
        """
        setup jenkins_master help message
        """
        ctx.config_dict.update(**kwargs)
        # DEBUG INFO
        click.echo(ctx.config_dict)
