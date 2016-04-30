#!/usr/bin/env python
import os
import click

from lib.cli_common import BaseCLI


class JenkinsSlaveCLI(BaseCLI):

    JENKINS_SLAVE_COMMANDS = ['setup', 'teardown']
    SUB_GROUP_NAME = 'jenkins_slave'

    @classmethod
    def register_cli(cls):
        for cmd in cls.JENKINS_SLAVE_COMMANDS:
            cls.jenkins_slave.add_command(getattr(cls, cmd))

    @staticmethod
    @click.group(subcommand_metavar='COMMAND [OPTIONS]',
                 context_settings=BaseCLI.CONTEXT_SETTINGS)
    @click.option(
        '--topology',
        type=click.Path(),
        default='foo/bar/jslave_config',
        help='path/to/file')
    @click.option(
        '--ssh_keyfile',
        type=click.Path(),
        help='path to keyfile')
    @click.option(
        '--jslavename',
        type=click.STRING,
        default='my-cool-jslave',
        help='name of Jenkins slave - ex. my-cool-jslave')
    @click.option(
        '--workspace',
        type=click.Path(),
        default=os.getcwd(),
        help='/path/to/workspace - ex. /var/lib/jenkins')
    @BaseCLI.context()
    def jenkins_slave(ctx, **kwargs):
        """
        jenkins_slave provisioner help message
        """
        # general update
        ctx.config_dict.update(**kwargs)

    @staticmethod
    @click.command()
    @click.option(
        '--jslavelabel',
        type=click.STRING,
        default='my-cool-jslave',
        help='label(s) for Jenkins slave - comma separated list of desired '
             'labels')
    @click.option(
        '--jenkins_master_url',
        type=click.STRING,
        required=True,
        help='url of jenkins master - ex. http://10.3.4.4')
    @click.option(
        '--jenkins_master_username',
        type=click.STRING,
        help='The username used to connect to the jenkins master')
    @click.option(
        '--jenkins_master_password',
        type=click.STRING,
        help='The password used to connect to the jenkins master')
    @click.option(
        '--jslavecreate',
        is_flag=True,
        help="Create jenkins slave if it doesn't exists")
    @BaseCLI.context()
    def setup(ctx, **kwargs):
        """
        setup jslave help message
        """
        ctx.config_dict.update(**kwargs)
        # call to your backend like
        #JenkinsSlaveProvisioner(ctx.config_dict).setup()

    @staticmethod
    @click.command()
    @click.option(
        '--jenkins_slave_username',
        type=click.STRING,
        required=True,
        help='username of the jenkins slave - ex. root')
    @click.option(
        '--jenkins_slave_password',
        type=click.STRING,
        help='password of the jenkins slave - ex. 123456')
    @click.option(
        '--jenkins_slave_ip',
        type=click.STRING,
        required=True,
        help='ip of slave - ex. 10.3.4.4')
    @BaseCLI.context()
    def teardown(ctx, **kwargs):
        """
        teardown jslave help message
        """
        ctx.config_dict.update(**kwargs)
        # call to your backend like
        # JenkinsSlaveProvisioner(ctx.config_dict).teardown()
