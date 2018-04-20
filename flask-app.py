# coding:utf-8
import os
from flask import Flask, render_template, url_for, make_response, send_from_directory

# 生成Flask实例
app = Flask(__name__)
APP_ROOT = os.path.dirname(os.path.abspath(__file__))   # refers to application_top
APP_STATIC_TXT = os.path.join(APP_ROOT, 'sources') #设置一个专门的类似全局变量的东西

@app.route('/')
def test():
    print('get')
    return render_template('candlestick-brush.html')


@app.route("/download/<filename>", methods=['GET'])
def download_file(filename):
    directory = './sources/'
    print(directory)
    return send_from_directory(directory, filename, as_attachment=True)


@app.route("/download/log", methods=['GET'])
def download_log_file():
    log_data = []
    file = open(os.path.join(APP_STATIC_TXT, 'log1.txt'))
    for line in file:
        if '买开' in line or '买平今' in line or '卖平今' in line or '卖开' in line or '撤单' in line:
            log_data.append(line.split(' '))
    file.close()
    return str(log_data)


if __name__ == "__main__":
    # 运行项目
    app.run(debug=True)
