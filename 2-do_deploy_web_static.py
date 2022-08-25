#!/usr/bin/python3
"""
Distributes an archive to your web servers, using the function do_deploy
"""

from fabric.api import put, run, env
from os.path import exists

env.hosts = ['54.242.106.85', '54.167.65.250']


def do_deploy(archive_path):
    """
    Deploy the web_static on remotes servers
    """
    if (not exists(archive_path)):
        return False

    try:
        put(archive_path, '/tmp/')

        # This contain the extension ex: .tgz
        only_file = archive_path.split('/')[-1]
        # File without extension
        only_name = only_file.split('.')[0]

        full_path = '/data/web_static/releases/' + only_name + '/'

        run('mkdir -p {:s}'.format(full_path))
        run('tar -xzf /tmp/{:s} -C {:s}'.format(only_file, full_path))
        run('rm /tmp/{:s}'.format(only_file))
        run('mv {:s} {:s}'.format(full_path + 'web_static/*', full_path))
        run('rm -rf {:s}'.format(full_path + 'web_static'))

        sym_link = '/data/web_static/current'

        run('rm -rf {:s}'.format(sym_link))
        run('ln -s {:s} {:s}'.format(full_path, sym_link))

        print('New version deployed!')

        return True

    except Exception:
        return False
