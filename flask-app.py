# -*- coding:utf-8 -*-
import json
import os
from flask import Flask, render_template, url_for, make_response, send_from_directory
from app import store

# 生成Flask实例
app = Flask(__name__)
APP_ROOT = os.path.dirname(os.path.abspath(__file__))  # refers to application_top
APP_STATIC_TXT = os.path.join(APP_ROOT, 'sources')  # 设置一个专门的类似全局变量的东西


@app.route('/')
def test():
    print('get')
    return render_template('tpt_line.html')


@app.route("/download/<filename>", methods=['GET'])
def download_file(filename):
    if store.exist(store.COLLECTION_RECORDS, store.COLLECTION_KEY, filename) is not None:
        return store.query(store.COLLECTION_RECORDS, filename)
    else:
        directory = './sources/'
        if not os.path.exists(os.path.join(APP_STATIC_TXT, filename)):
            return send_from_directory(directory, filename, as_attachment=True)
        file = open(os.path.join(APP_STATIC_TXT, filename))
        data = [{store.COLLECTION_KEY: filename, "records": file.read()}]
        store.insert(data, 'records')
        return send_from_directory(directory, filename, as_attachment=True)


@app.route("/download/log", methods=['GET'])
def download_log_file():
    filename = 'log1.txt'
    if store.exist(store.COLLECTION_LOGS, store.COLLECTION_KEY, filename) is not None:
        return store.query(store.COLLECTION_LOGS, filename)

    file = open(os.path.join(APP_STATIC_TXT, filename))
    total_data = {}
    for line in file:
        if '买开' in line or '买平今' in line or '卖平今' in line or '卖开' in line or '撤单' in line or '撮合失败' in line:
            line_data = line.split(' ')
            date_key = line_data[0]
            time_key = line_data[1]
            if date_key in total_data.keys():
                total_data[date_key][time_key] = line_data
            else:
                time_data = {time_key: line_data}
                total_data[date_key] = time_data
    file.close()
    data = json.dumps(total_data, ensure_ascii=False)

    insert_data = [{store.COLLECTION_KEY: filename, "records": data}]
    store.insert(insert_data, 'records')
    return data


if __name__ == "__main__":
    # 运行项目
    app.run(debug=True)
