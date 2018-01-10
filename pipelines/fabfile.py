# -*- coding: utf-8 -*-
from __future__ import print_function

import os, sys

from fabric.api import (
    env, task, roles, execute, lcd, local
)

from utils.main import (
    timestamp, dir_create_remote_structure, upload_unpack_code, switch_code, pack_code
)


@roles('all')
def rsync_code():
    pass


@task()
def test():
    with lcd(env.testdir):
        local("make test")


@task()
@roles('proxy')
def deploy_proxy():
    print('deploy proxy')
    execute(dir_create_remote_structure, REMOTE_RELEASE_DIR)
    execute(upload_unpack_code, ARCHIVE_PATH, REMOTE_RELEASE_DIR)
    execute(switch_code, REMOTE_RELEASE_DIR, REMOTE_CURRENT_RELEASE_LINK)


@task(default=True)
def deploy():
    preperation()
    execute(deploy_proxy)


def preperation():
    pack_code(CODE_DIR, ARCHIVE_PATH, 'fabfile-pipeline')

# COMMON
"""Global Variables:"""
env.roledefs = {"proxy": [env.ip]}
ARCHIVE_PATH = os.path.join(os.curdir, "go_pipe_deploy.tar")
CODE_DIR = local_current_release_dir = os.path.join(os.pardir, env.codedir)
REMOTE_DIR = "/data/ggg"
REMOTE_RELEASE_DIR = os.path.join(REMOTE_DIR, "releases", str(timestamp))
REMOTE_CURRENT_RELEASE_LINK = os.path.join(REMOTE_DIR, "current")


if __name__ == '__main__':
    pass
