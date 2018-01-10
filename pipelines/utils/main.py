# -*- coding: utf-8 -*-
import os
import time
import logging

from fabric.api import (
    local, run, sudo, cd, put
)


"""Global Variables:"""
timestamp = int(time.time())
logging.basicConfig(level=logging.INFO)
checkout_root = "src"


def link_create(src, dst):
    sudo("rm -rf {0}".format(dst))
    sudo("ln -s {src} {dst}".format(src=src, dst=dst))


def dir_create_remote_structure(working_dir):
    print("dir create remote structure")
    run("mkdir -p {working_dir}".format(working_dir=working_dir))
    return working_dir


def pack_code(src, dst, exclude=None):
    if src != "" and dst != "":
        print("pack code")
        with cd(src):
            local("rm -f {0}".format(dst))
            excluded = ""
            if exclude:
                excluded = "--exclude='{}'".format(exclude)
            local("tar -cf {dst} --exclude='.git*' {exc}  -C {src} .".format(src=src, dst=dst, exc=excluded))


def upload_unpack_code(local_path_to_archive, remote_dir):
    print("upload code")
    put(local_path_to_archive, remote_dir)
    with cd(remote_dir):
        arch_name = os.path.basename(local_path_to_archive)
        run("tar -xf {0}".format(arch_name))
        run("rm -f {0}".format(arch_name))


def switch_code(release_dir, dir_current_release):
    print("sw code")
    link_create(release_dir, dir_current_release)
