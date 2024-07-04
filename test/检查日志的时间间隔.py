import re
import ntp_util

with open(file=r'C:\Users\Administrator\Desktop\test.log', mode='r', encoding='utf-8') as f:
    read_data = f.read()
# # print(read_data)
# lines = read_data.split("\n")
# print(lines[0])
pattern1 = r'\d{4}/\d{1,2}/\d{1,2} \d{1,2}:\d{2}:\d{2}'
time_list = re.findall(pattern1, read_data)
# print(time_list)

timestamp_list = []
for time_str in time_list:
    res = ntp_util.str_time_to_timestamp(time_str, format="%Y/%m/%d %H:%M:%S")
    timestamp_list.append(res)
# print(timestamp_list)

for i in range(1, len(timestamp_list)):
    t = timestamp_list[i] - timestamp_list[i - 1]
    print(i, '\t', timestamp_list[i] - timestamp_list[i - 1], time_list[i - 1])
    if t < 290 or t > 310:
        # print('#' * 100)
        print(i, '\t', timestamp_list[i] - timestamp_list[i - 1], time_list[i - 1])
