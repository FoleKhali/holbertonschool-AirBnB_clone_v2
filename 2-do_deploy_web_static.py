#!/usr/bin/python3
""" distributes an archive to your web servers,
using the function do_deploy """
from fabric.api import *
import os

env.hosts = ['52.73.0.54', '34.230.19.232']
env.user = "ubuntu"


def do_deploy(archive_path):
    """ It does deploy in the webserver """
    if not os.path.exists("archive_path"):
        return False

    try:

        fil_tgz = os.path.basename(archive_path)
        fol_des = fil_tgz.replace(".tgz", "")
        path = "/data/web_static/releases/"

        put(archive_path, "/tmp/")

        run("mkdir -p {}{}/".format(path, fol_des))
        run("tar -xzf /tmp/{} -C {}{}/".format(fil_tgz, path, fol_des))
        run("rm /tmp/{}".format(fil_tgz))
        run("mv {}{}/web_static/* {}{}/".format(path, fol_des, path, fol_des))
        run("rm -rf {}{}/web_static".format(path, fol_des))
        run("rm -rf /data/web_static/current")
        run("ln -s {}{}/ /data/web_static/current".format(path, fol_des))

        print("New version deployed!")

        return True

    except:
        return None
