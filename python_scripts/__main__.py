import pysftp

from python_scripts.utils import sftp_utils
from sftp import project_downloader
from flash_preparation import prepare_flash

env_file = ".env"

if __name__ == '__main__':
    (sftp_host, sftp_port, sftp_username, sftp_password, sftp_download_path) = project_downloader.read_in_env(env_file)
    sftp_connection: pysftp.Connection = sftp_utils.start_connect(sftp_host, sftp_port, sftp_username, sftp_password)
    path = project_downloader.get_next_project(sftp_connection, sftp_download_path)

    (zephyr_base_installation, cmake_install, toolchain_installation) = prepare_flash.read_in_from_env(env_file)
    prepare_flash.run()
