# -*- coding: utf-8 -*-
"""
-
Author:
Date:
"""
import re
from my_decorator import timer
from tqdm import tqdm


def extract_six_digit_numbers(filename, mark=None):
    # 定义正则表达式模式，查找任何位置上的连续6位数字
    pattern = re.compile(r'\d{6}' + mark)
    pattern1 = re.compile(r'\d{6}')
    # 打开文件并读取全部内容
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()

    # 使用正则表达式查找所有匹配项
    matches = re.findall(pattern, content)

    # 打印所有匹配到的6位数字
    res_match = []
    for match in matches:
        match = re.findall(pattern1, match)
        res_match.append(match[0])
    return res_match


def extract_content_between_markers(file_path, start_marker, end_marker):
    """
    提取文件中位于指定起始标记和结束标记之间的内容。

    :param file_path: 文件路径 (str)
    :param start_marker: 起始标记 (str)
    :param end_marker: 结束标记 (str)
    :return: 包含所有匹配内容的列表 (list of str)
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            # 构建正则表达式，匹配起始和结束标记之间的内容
            pattern = re.escape(start_marker) + '(.*?' + re.escape(end_marker) + ')'
            matches = re.findall(pattern, content, re.DOTALL)
            return matches
    except FileNotFoundError:
        print(f"错误：文件 {file_path} 未找到。")
        return []
    except Exception as e:
        print(f"读取文件时发生错误：{e}")
        return []


@timer
def process_data(content):
    """
    将给定的行数据列表转换为字典，其中每行的第一个字段作为键，
    该字段之后的所有数据（去除了前后空格和逗号）作为值列表。

    :param lines: 一个包含多行数据的列表，每行数据由空格分隔。
    :return: 转换后的字典，键为每行的第一个字段，值为该行其余字段组成的列表。
    """
    # with open(filename, 'r', encoding='utf-8') as file:
    #     content = file.read()

    # 使用splitlines()函数按行分割字符串
    lines_list = content.splitlines()
    # # 打印列表内容，查看结果
    # for line in lines_list:
    #     print(line)
    data_dict = {}
    for line in lines_list:
        # 分割行数据，去除键部分的冒号，并清理每个值元素
        parts = line.split(' ')
        key = parts[0].strip(':')
        values = [part.strip(',') for part in parts[1:] if part]

        # 将处理后的数据存入字典
        data_dict[key] = values
    return data_dict


def filter_online_devices(data_dict: dict):
    online_list = []
    for key, value in data_dict.items():
        if len(value) >= 3:
            online_list.append(key)
            continue
        elif len(value) == 0:
            continue
        # print(key, value)
        online_time = re.sub(r'\(.*?', '', value[0])
        if int(online_time) <= 3600:
            # print(key, value)
            online_list.append(key)
            continue
    return online_list


if __name__ == '__main__':
    # 读取源文件
    file_path_dump = 'F:\\DID_Dump.log'
    start_marker = '[IOTDBB]'
    end_marker = '[IOTDCC]'
    content_list = extract_content_between_markers(file_path_dump, start_marker, end_marker)
    content_str = ''
    for content in content_list:
        content_str = content_str.join(content)
    # 调用函数并打印结果
    processed_data = process_data(content_str)
    # for key, value in processed_data.items():
    #     print(f"{key}: {value}")
    # print(len(processed_data))
    online_list = filter_online_devices(processed_data)
    print(len(online_list))
    print(online_list[:100])

    # 读取增量包
    file_path_full = 'F:\\IOTDBB_DID_Dump_Increment_20240626163625.txt'
    matchs = extract_six_digit_numbers(file_path_full, mark='_')
    print(matchs[:100])
    print(f"增量包数量{len(matchs)},源文件在线设备数量{len(online_list)}")
    for i in tqdm(range(len(online_list))):
        if online_list[i] != '0' + matchs[i]:
            print(online_list[i], matchs[i])
            raise Exception("匹配出错")