#查詢Port的占用
#netstat -nao | find "0.0.0.0:5000"
#砍掉占用XXXXX為上列找到的PID編號,後面加/F是強制刪除
#taskkill /pid XXXXX /F
import time
from random import randrange

from flask.json import jsonify
from flask import Flask, render_template

from pyecharts import options as opts
from pyecharts.charts import Line


app = Flask(__name__, static_folder="templates")


def line_base() -> Line:
    line = (
        Line()
        .add_xaxis(["9:45:55","9:46:0","9:46:5"])
        .add_yaxis(
            series_name="",
            y_axis=[randrange(50, 80) for _ in range(3)],
            is_smooth=True,
            label_opts=opts.LabelOpts(is_show=False),
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(title="動態數據"),
            xaxis_opts=opts.AxisOpts(type_="value"),
            yaxis_opts=opts.AxisOpts(type_="value"),
        )
    )
    return line


@app.route("/DynamicTest")
def index():
    return render_template("DynamicTest.html")


@app.route("/lineChart")
def get_line_chart():
    c = line_base()
    return c.dump_options_with_quotes()

#idx = time.localtime()
localtime = time.localtime()
idx = time.strftime("%I:%M:%S", localtime)


@app.route("/lineDynamicData")
def update_line_data():
    global idx
    #idx = idx + 1
    return jsonify({"name": idx, "value": randrange(50, 80)})


if __name__ == "__main__":
    app.run()