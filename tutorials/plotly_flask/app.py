from flask import Flask, render_template
import plotly.graph_objs as go
import plotly.io as pio

app = Flask(__name__)


@app.route("/")
def home():
    # create the data
    x = ["Apples", "Oranges", "Bananas"]
    y = [10, 8, 12]

    # create the bar chart
    data = [go.Bar(x=x, y=y)]

    # create the layout
    layout = go.Layout(
        title="Fruit Sales",
        xaxis={"title": "Fruit"},
        yaxis={"title": "Sales"},
    )

    # create the figure
    fig = go.Figure(data=data, layout=layout)

    fig.update_layout(plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor="rgba(0,0,0,0)")

    # export the figure to HTML
    plot_div = pio.to_html(fig, full_html=False)

    # render the HTML template
    return render_template("home.html", plot_div=plot_div)


if __name__ == "__main__":
    app.run(debug=True)
