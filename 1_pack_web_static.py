#!/usr/bin/python3
from fabric.api import local
from time import strftime
from datetime import date


def do_pack():
    """ this script contents of web_static folder"""

    file_n = strftime("%Y%m%d%H%M%S")
    try:
        local("mkdir -p versions")
        local("tar -czvf versions/web_static_{}.tgz web_static/"
              .format(file_n))

        return "versions/web_static_{}.tgz".format(fil_n)

    except Exception as ex:
        return None
