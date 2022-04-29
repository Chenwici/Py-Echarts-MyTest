from random import randrange
from flask import Flask, render_template
from pyecharts import options as opts
from pyecharts.charts import Bar, Liquid, Gauge

app = Flask(__name__, static_folder="templates")

#靜態回傳方法
@app.route("/")
def index():
    return "Hello World!!"

#靜態回傳方法
@app.route("/GaugeTest")
def GaugeTest():
    c = (
    Gauge()
    .add("", [("完成率\n\n",90)])
    .set_global_opts(title_opts=opts.TitleOpts(title="Gauge-基本示例"))
    .render("templates/Gauge_StateValueTest.html")
    )
    return render_template("Gauge_StateValueTest.html")

if __name__ == "__main__":
    app.run()