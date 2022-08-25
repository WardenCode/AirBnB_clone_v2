#!/usr/bin/python3
"""
Generates a .tgz archive from the contents of the web_static folder
"""

from fabric.api import local
from datetime import datetime


def do_pack():
    """
    Create a .tgz file that contains the files of the Airbnb Web Static
    """
    try:
        local("mkdir -p versions")
        path = "versions/web_static_{:s}.tgz"
        command = "tar -cvzf versions/web_static_{:s}.tgz web_static"
        date = datetime.now().strftime('%Y%m%d%H%M%S')
        local(command.format(date))
        return (path.format(date))
    except Exception:
        return (None)
