# -*- coding: utf-8 -*-
"""
-
Author:
Date:
"""
import re
from tqdm import tqdm


def extract_six_digit_numbers(filename):
    # 打开文件并读取全部内容
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()

    # 使用正则表达式查找所有匹配项
    matches = re.findall(r'^.{7}', content, re.MULTILINE)
    clean_matches = [''.join(match[1:7]) for match in matches]
    # print(clean_matches[:10])
    return clean_matches


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


if __name__ == '__main__':
    file_path_full = 'F:\\IOTDAA_Increment.txt'
    six_matches = extract_six_digit_numbers(file_path_full)

    # 使用示例
    file_path_dump = 'F:\\DID_Dump.log'
    start_marker = '[IOTDAA]'
    end_marker = '[IOTDBB]'
    content_list = extract_content_between_markers(file_path_dump, start_marker, end_marker)
    content_str = ''
    for content in content_list:
        content_str = content_str.join(content)
    content_list = content_str.splitlines()
    print(content_list[:100])
    # for i in tqdm(range(len(matchs))):
    #     did = matchs[i]
    #     for j in range(i, len(content_list)):
    #         if did in content_list[j]:
    #             # print(F"{did}匹配到了{content_list[j]}")
    #             break
    #     else:
    #         raise Exception(F"未检测到{matchs[i]}")
    print(f"增量包数量{len(six_matches)},源文件数量{len(content_list)}")
    print(content_list[-1])
    for i in tqdm(range(len(six_matches))):
        j = i + 1
        if six_matches[i] not in content_list[j]:
            print(f"行号：{i},{six_matches[i]},{content_list[j]}")
            raise Exception("未匹配到")
