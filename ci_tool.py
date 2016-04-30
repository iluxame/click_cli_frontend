#!/usr/bin/env python
import click

from lib.cli_common import BaseCLI
# lib.cli_common.CLIMeta takes care for registration of bootstrap stuff
# so import here is in order to include cli sub groups
import cli_interfaces.jenkins_slave  # noqa
import cli_interfaces.jenkins_master  # noqa


class CLI(BaseCLI):

    SUB_GROUPS_REGISTRY = []

    @classmethod
    def register_cli(cls):
        for group in cls.SUB_GROUPS_REGISTRY:
            cls.cli.add_command(group)

    @staticmethod
    @click.group(subcommand_metavar='COMMAND [OPTIONS] OPCODE [OPTIONS]',
                 context_settings=BaseCLI.CONTEXT_SETTINGS)
    @click.option('--project_defaults',
                  type=click.Path(),
                  required=True,
                  help='path to project defaults conf file')
    @BaseCLI.context()
    def cli(ctx, **kwargs):
        """
        ci-provisioner help message
        """
        # DEBUG INFO
        ctx.config_dict.update(**kwargs)


if __name__ == "__main__":
    # ctx will be created/got by @BaseCLI.context() decorator
    CLI.cli()
