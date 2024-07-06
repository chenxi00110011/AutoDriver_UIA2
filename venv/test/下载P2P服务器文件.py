from file_operations import rename_file
from ntp_util import timestamp_to_date
import schedule
import os
import time
from sftp_utils import list_remote_directory_as_dict, download_file_from_sftp

# SFTP服务器配置信息
def job():
    host = '139.159.218.144'
    port = 22  # SFTP默认端口
    username = 'root'
    password = 'ZOWELL@123456'  # 或者使用密钥对认证
    remote_directory = '/root/EasyDebug/bin/'  # 你想查看的远程目录
    remote_files = list_remote_directory_as_dict(host, port, username, password, remote_directory)
    filtered_dict = {key: value for key, value in remote_files.items() if
                     '.txt.bz2' in key or 'DID_Dump.log' == key}
    print(filtered_dict)

    # Example usage:
    for remote_filename in filtered_dict.keys():
        local_path = r'C:\Users\Administrator\Desktop\data\sftp\139.159.218.144' + '/'
        if not os.path.exists(local_path + remote_filename):
            download_file_from_sftp(host, port, username, password, remote_directory, remote_filename, local_path)
    DID_Dump = r'C:\Users\Administrator\Desktop\data\sftp\139.159.218.144\DID_Dump.log'
    if os.path.exists(DID_Dump):
        time_str = timestamp_to_date(format="%Y-%m-%d %H-%M-%S")
        rename_file(DID_Dump, DID_Dump + time_str)


# 使用cron风格的时间设置，每30分钟执行一次，* 表示任意值，因此"*/30"表示每30分钟
job()
schedule.every(60).minutes.do(job)

print("Task scheduler started...")

while True:
    schedule.run_pending()
    time.sleep(1)
