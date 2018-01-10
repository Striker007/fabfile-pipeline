# -*- coding: utf-8 -*-
from __future__ import print_function

import os

from fabric.api import (
    env, task, roles, execute
)

from utils.main import (
    timestamp, dir_create_remote_structure, upload_unpack_code, switch_code, pack_code
)


@roles('all')
def rsync_code():
    pass


@task()
@roles('proxy')
def deploy_proxy():
    print('deploy proxy')
    execute(dir_create_remote_structure, REMOTE_RELEASE_DIR)
    execute(upload_unpack_code, ARCHIVE_PATH, REMOTE_RELEASE_DIR)
    execute(switch_code, REMOTE_RELEASE_DIR, REMOTE_CURRENT_RELEASE_LINK)


@task(default=True)
def deploy_main():
    execute(deploy_proxy)


# COMMON
"""Global Variables:"""
env.roledefs = {"proxy": [env.ip]}
ARCHIVE_PATH = os.path.join(os.curdir, "go_pipe_deploy.tar")
CODE_DIR = local_current_release_dir = os.pardir
REMOTE_DIR = "/data/ggg"
REMOTE_RELEASE_DIR = os.path.join(REMOTE_DIR, "releases", str(timestamp))
REMOTE_CURRENT_RELEASE_LINK = os.path.join(REMOTE_DIR, "current")

# config = load_yaml_config(env.deploy_config, env.environment)
pack_code(CODE_DIR, ARCHIVE_PATH)


if __name__ == '__main__':
    pass
