#!/usr/bin/python3
"""
Generates a .tgz archive from the contents
of the web_static folder of the AirBnB Clone repo
"""
import os.path
from fabric.api import *

env.hosts = ['52.73.0.54', '34.230.19.232']

def do_deploy(archive_path):
    """ distributes an archive to a web server """
    if os.path.exists(archive_path) is False:
        return False
    try:
        path = '/data/web_static/releases/' # agregar esto
        path_id = archive_path.split('/') # [versions, web_static_20170315003959.tgz]
        a = path_id[1].split('.') # ---> [web_static_20170315003959, tgz]
        put(archive_path, "/tmp") # ---> OK
        run("mkdir -p {}{}".format(path, a[0]))
        run("tar -xzf /tmp/{} -C {}{}".format(path_id[1], path, a[0]))
        run("rm /tmp/{}".format(path_id[1])) #  ---> OK
        run("mv {}{}/web_static/* {}{}".format(path, a[0], path, a[0])) # ---> OK
        run("rm -rf {}{}/web_static".format(path ,a[0]))
        run("rm -rf /data/web_static/current")
        run("ln -s {}{}/ /data/web_static/current".format(path ,a[0]))
        print("New version deployed!")
        return True
    except:
        return False
