# -*- coding: utf-8 -*-

# http://docs.fabfile.org/en/1.5/tutorial.html
from fabric.api import *

project = "hello-tfidf"

# the user to use for the remote commands
env.user = ''
# the servers where the commands are executed
env.hosts = []


def reset():
    """Reset local debug env."""
    activate_this = "env/bin/activate_this.py"
    from cffi.setuptools_ext import execfile
    execfile(activate_this, dict(__file__=activate_this))
    local("which python3")

def setup():
    """Setup virtual env."""
    local("virtualenv env")
    reset()
    local("pip install -r requirements.txt")

def index():
    """Basic Example of Indexing and Searching"""
    reset()
    local("python3 index.py")

