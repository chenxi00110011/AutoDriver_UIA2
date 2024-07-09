import time
import pytest
from sftp_utils import get_file_content_over_ssh

hosts = ['139.159.218.144']


@pytest.mark.p2p
@pytest.mark.parametrize("host", hosts)
@pytest.mark.flaky(reruns=2, reruns_delay=5)
def test_monitor_server_resources(host: str):
    username = "root"
    password = "ZOWELL@123456"
    exec_command = 'top -b -n1 | grep "Cpu(s)"'
    cpu_list = get_file_content_over_ssh(host, username, password, exec_command).split()
    exec_command = 'free|grep "Mem"'
    mem_list = get_file_content_over_ssh(host, username, password, exec_command).split()
    exec_command = 'df |grep "/dev/sda1"'
    sda_list = get_file_content_over_ssh(host, username, password, exec_command).split()
    # 空闲cpu占比
    idle = float(cpu_list[7])
    # 空闲内存占比
    memory_usage_rate = int(mem_list[-1]) / int(mem_list[1])
    # 空闲磁盘占比
    free_disk_percentage = int(sda_list[3]) / int(sda_list[1])

    # print(idle, memory_usage_rate, free_disk_percentage)

    # cpu资源中，空闲资源大于20%
    assert idle >= 0.2
    # 空闲内存占比，大于20%
    assert memory_usage_rate >= 0.2
    # 空闲磁盘占比大于10%
    assert free_disk_percentage >= 0.1
