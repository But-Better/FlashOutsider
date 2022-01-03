import pysftp
from paramiko.ssh_exception import AuthenticationException, PasswordRequiredException, SSHException
from pysftp.exceptions import *


# creation creation of a sftp connection
def start_connect(host: str, port: int, username: str, password: str):
    try:
        conn = pysftp.Connection(host=host, port=port, username=username, password=password)
        print(f'connection established successfully to {host}:{port}')
        return conn
    except ConnectionException:
        print(f'failed to establish connection to targeted server')
    except PasswordRequiredException:
        print(f'password is required to connect to {host}')
    except AuthenticationException:
        print(f'failed to authenticate connection to {host} with username:{username} and given password')
        pass


# recursive directory downloader
def download_directory_from_sftp(conn: pysftp.Connection, remote_dir: str, local_dir: str):
    if not conn.lexists(remote_dir):
        IOError(f"remote directory {remote_dir} doesn't exist")
        return
    conn.get_r(remote_dir, local_dir, True)


# directory scanner for remote directory,
# returns a sorted list of files/directories for the given remote path
def scan_dirs_in_remote_location(conn: pysftp.Connection, remote_dir: str):
    if not conn.lexists(remote_dir):
        IOError(f"remote directory {remote_dir} doesn't exist")
        return

    scan_result = conn.listdir(remote_dir)
    remote_dirs = list()
    for result in scan_result:
        if conn.isdir(result):
            remote_dirs.append(result)

    return remote_dirs

