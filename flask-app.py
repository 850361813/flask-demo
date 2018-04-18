# coding:utf-8
import os
from flask import Flask, render_template, url_for, make_response, send_from_directory

# 生成Flask实例
app = Flask(__name__)


@app.route('/')
def test():
    print('get')
    return render_template('candlestick-brush.html')


@app.route("/download/<filename>", methods=['GET'])
def download_file(filename):
    directory = './sources/'
    print(directory)
    return send_from_directory(directory, filename, as_attachment=True)


if __name__ == "__main__":
    # 运行项目
    app.run(debug=True)
