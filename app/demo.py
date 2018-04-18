# coding:utf-8

from flask import Flask, render_template, url_for

# 生成Flask实例
app = Flask(__name__)


@app.route('/')
def my_echart():
    return render_template('/Volumes/Transcend/project/python/visual-transaction/my_template.html')


if __name__ == "__main__":
    # 运行项目
    app.run(debug=True)
