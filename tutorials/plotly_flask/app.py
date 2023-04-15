from flask import Flask, render_template
import plotly.graph_objs as go
import plotly.io as pio
import pandas as pd
from flask_table import Table, Col
import random

app = Flask(__name__)


class Data(Table):
    x = Col("x")
    y = Col("y")


@app.route("/")
def home():
    # # create the data
    # x = ["Apples", "Oranges", "Bananas"]
    # y = [10, 8, 12]

    # # create the bar chart
    # data = [go.Bar(x=x, y=y)]

    # # create the layout
    # layout = go.Layout(
    #     title="Fruit Sales",
    #     xaxis={"title": "Fruit"},
    #     yaxis={"title": "Sales"},
    # )

    # # create the figure
    # fig = go.Figure(data=data, layout=layout)

    # create a sample dataframe
    # data = {
    #     "Name": ["Alice", "Bob", "Charlie"],
    #     "Age": [25, 30, 35],
    #     "City": ["New York", "San Francisco", "London"],
    # }
    # df = pd.DataFrame(data)

    # # create a table using plotly
    # fig = go.Figure(
    #     data=[
    #         go.Table(
    #             header=dict(
    #                 values=list(df.columns), fill_color="paleturquoise", align="left"
    #             ),
    #             cells=dict(
    #                 values=[df.Name, df.Age, df.City],
    #                 fill_color="lavender",
    #                 align="left",
    #             ),
    #         )
    #     ]
    # )

    data = []
    for i in range(10):
        data.append({"x": i, "y": random.randint(0, 10)})
    table = Data(data)
    return render_template("home.html", table=table)

    # fig.update_layout(plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor="rgba(0,0,0,0)")

    # # export the figure to HTML
    # plot_div = pio.to_html(fig, full_html=False)

    # # render the HTML template
    # return render_template("home.html", plot_div=plot_div)


if __name__ == "__main__":
    app.run(debug=True)
