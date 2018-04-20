# -*- coding:utf-8 -*-

LOG_FILE = '../sources/log1.txt'


# 卖开
# 买平今
# 卖平今
# 卖开
# 撤单


def load_log(log_file):
    total_data = {}
    file = open(log_file)
    for line in file:
        if '买开' in line or '买平今' in line or '卖平今' in line or '卖开' in line or '撤单' in line:
            line_data = line.split(' ')
            date_key = line_data[0]
            time_key = line_data[1]
            if date_key in total_data.keys():
                total_data[date_key][time_key] = line_data
            else:
                time_data = {time_key: line_data}
                total_data[date_key] = time_data
    file.close()
    return total_data


