import os
import re

import pytest
from sftp_utils import get_file_content_over_ssh

p2p_hosts = ['94.74.67.179', '139.159.218.144', '159.138.148.125']
relay_hosts = ['116.205.172.145']


@pytest.mark.p2p
@pytest.mark.parametrize("host", p2p_hosts)
@pytest.mark.flaky(reruns=2, reruns_delay=5)
def test_p2p_process_check_client_tree(host: str):
    username = "root"
    password = "ZOWELL@123456"
    exec_command = "ps -aux |grep ./client"
    ouput = get_file_content_over_ssh(host, username, password, exec_command)
    pattern = r"./client \d{3,}"
    matches = re.findall(pattern, ouput)
    match_count = len(matches)
    assert match_count == 3


@pytest.mark.p2p
@pytest.mark.parametrize("host", p2p_hosts)
@pytest.mark.flaky(reruns=2, reruns_delay=5)
def test_p2p_process_check_other(host: str):
    username = "root"
    password = "ZOWELL@123456"
    exec_command = "ps -aux"
    ouput = get_file_content_over_ssh(host, username, password, exec_command)
    assert "python3 GeoIPServer.py" in ouput
    assert "./Partner" in ouput
    assert "/root/PPC/RSIOTD_Server64" in ouput


@pytest.mark.relay
@pytest.mark.parametrize("host", relay_hosts)
@pytest.mark.flaky(reruns=2, reruns_delay=5)
def test_relay_process_check(host: str):
    username = "root"
    password = "ZOWELL@123456"
    exec_command = "ps -aux"
    ouput = get_file_content_over_ssh(host, username, password, exec_command)
    assert "/root/PPC/start_Relay.sh" in ouput
    assert "/root/PPC/P2P_Relay64" in ouput


