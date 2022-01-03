from python_scripts.utils import sftp_utils
from python_scripts.env_reader import env_reader


def read_in_env():
    read: dict = env_reader.read_from_env(".env")
    host = read["sftp_host"]
    port = int(read["sftp_port"])
    username = read["sftp_username"]
    password = read["sftp_password"]
    download_path = read["sftp_download_path"]
    return host, port, username, password, download_path


def start_connection(host, port, username, password):
    return sftp_utils.start_connect(host, port, username, password)


def choose_directory_to_download(possibilities):
    return possibilities[-1]


def get_next_project(conn, download_path):
    remote_dirs: list = sftp_utils.scan_dirs_in_remote_location(conn, ".")
    remote_dir_to_download = choose_directory_to_download(remote_dirs)
    sftp_utils.download_directory_from_sftp(conn, remote_dir_to_download, f"{download_path}/{remote_dir_to_download}")
