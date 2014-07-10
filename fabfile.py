"""
Common tools for deploy run shell and the like.
"""

import os

from fabric.api import *
from fabric.colors import *

env.use_ssh_config = True


@task
def install():
    """Install the node_modules dependencies"""
    local('git submodule update --init')
    local('python manage.py syncdb')
    local('python manage.py migrate')
    if not os.path.isfile('yuna/secrets.py'):
        local('cp yuna/secrets.py.template yuna/secrets.py')