import os
import pytest
from sftp_utils import get_file_content_over_ssh

p2p_hosts = ['94.74.67.179', '139.159.218.144', '159.138.148.125']


@pytest.mark.parametrize("host", p2p_hosts)
def test_check_config(host: str):
    username = "root"
    password = "ZOWELL@123456"
    exec_command = "cat /root/EasyDebug/config/EasyDebugConfig.ini"
    file_config = get_file_content_over_ssh(host, username, password, exec_command)
    with open("EasyDebugConfig.ini", "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            assert line in file_config


if __name__ == "__main__":
    os.system('pytest  test_check_config')
