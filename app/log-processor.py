# -*- coding:utf-8 -*-

LOG_FILE = '../sources/log1.txt'


# 卖开
# 买平今
# 卖平今
# 卖开
# 撤单


def load_log(log_file):
    log_data = []
    file = open(log_file)
    for line in file:
        if '买开' in line or '买平今' in line or '卖平今' in line or '卖开' in line or '撤单' in line:
            log_data.append(line.split(' '))
    file.close()
    return log_data

