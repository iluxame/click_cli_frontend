#!/usr/bin/env python
import click


class Context(object):
    """
    Configuration Context
    """
    def __init__(self):
        self.config_dict = {}


class CLIMeta(type):

    SUB_GROUPS_REGISTRY = []

    def __new__(cls, *args, **kwargs):
        new_cls = super(CLIMeta, cls).__new__(cls, *args, **kwargs)

        # collect sub groups
        if new_cls.__name__ not in ['CLI', 'BaseCLI']:
            cls.SUB_GROUPS_REGISTRY.append(
                getattr(new_cls, new_cls.SUB_GROUP_NAME))
        # init context
        if new_cls.__name__ == 'BaseCLI':
            new_cls.context()
        # pass sub groups registry to main cli
        else:
            new_cls.SUB_GROUPS_REGISTRY = cls.SUB_GROUPS_REGISTRY

        # register cli subgroup methods
        if new_cls.__name__ != 'BaseCLI' and hasattr(new_cls, 'register_cli'):
            new_cls.register_cli()

        return new_cls


class BaseCLI(object):
    """
    Base class for all CLI providers
    """

    __metaclass__ = CLIMeta

    CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])

    @classmethod
    def register_cli(cls):
        """
        Registration logic of subgroups, should be overwritten in main CLI
        """
        for cmd in cls.SUB_GROUP_COMMANDS:
            getattr(cls, cls.SUB_GROUP_NAME).add_command(getattr(cls, cmd))

    @staticmethod
    def context():
        """
        Configuration context holder
        """
        return click.make_pass_decorator(Context, ensure=True)
