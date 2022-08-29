#!/usr/bin/python3
"""
Generates a .tgz archive from the contents
of the web_static folder of the AirBnB Clone repo
"""
import os
from fabric.api import *
from datetime import datetime

env.hosts = ['52.73.0.54', '34.230.19.232']


def do_pack():
    """generates a .tgz file from the contents
    of the web_static folder of your AirBnB Clone repository"""
    file_result = "versions/web_static_{}.tgz web_static".format(
            datetime.strftime(datetime.now(), "%Y%m%d%H%M%S"))
    local("mkdir -p versions")
    result = local("tar -cvzf " + file_result + " ./web_static")
    if result.succeeded:
        return file_result
    return None


def do_deploy(archive_path):
    """ distributes an archive to a web server """
    if os.path.exists(archive_path) is False:
        return False
    try:
        path = '/data/web_static/releases/'
        path_id = archive_path.split('/')
        a = path_id[1].split('.')
        put(archive_path, "/tmp")
        run("mkdir -p {}{}".format(path, a[0]))
        run("tar -xzf /tmp/{} -C {}{}".format(path_id[1], path, a[0]))
        run("rm /tmp/{}".format(path_id[1]))
        run("mv {}{}/web_static/* {}{}".format(path, a[0], path, a[0]))
        run("rm -rf {}{}/web_static".format(path, a[0]))
        run("rm -rf /data/web_static/current")
        run("ln -s {}{}/ /data/web_static/current".format(path, a[0]))
        print("New version deployed!")
        return True
    except:
        return False
