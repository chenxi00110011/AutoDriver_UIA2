import time
import pytest
from sftp_utils import get_file_content_over_ssh

p2p_hosts = ['94.74.67.179', '139.159.218.144', '159.138.148.125']


@pytest.mark.p2p
@pytest.mark.parametrize("host", p2p_hosts)
@pytest.mark.flaky(reruns=2, reruns_delay=5)
def test_is_log_file_being_written_now(host: str):
    # 检查文件最近1分钟是否有修改
    username = "root"
    password = "ZOWELL@123456"
    exec_command = "stat -c %Y /root/EasyDebug/log/Partner_Log1.log"
    ouput = get_file_content_over_ssh(host, username, password, exec_command)
    assert int(time.time()) - int(ouput) < 60  # 用电脑当前时间戳 - 文件最后修改的时间，小于60秒
