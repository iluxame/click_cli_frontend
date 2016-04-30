import os
from setuptools import setup

setup(
    name='ci-tool',
    version='0.1',
    py_modules=['ci_tool', 'cli_interfaces.jenkins_slave',
                'cli_interfaces.jenkins_master', 'lib.cli_common'],
    include_package_data=True,
    install_requires=[
        'click',
    ],
    entry_points='''
        [console_scripts]
        ci-tool=ci_tool:CLI.cli
    ''',
)
# ugly bash completion hack according to http://click.pocoo.org/6/bashcomplete/
with open('%s/.bashrc' % os.path.expanduser('~'), 'a') as f:
    f.write('eval "$(_CI_TOOL_COMPLETE=source ci-tool)"\n')
