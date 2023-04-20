from flask import Flask, render_template
import plotly.graph_objs as go
import plotly.io as pio
import pandas as pd
import plotly.express as px

app = Flask(__name__)


@app.route("/")
def home():
    df = pd.read_csv("data.csv")
    # games = len(data["points"])
    # ppg = round(sum(data["points"]) / games, 1)

    fig = px.bar(
        df,
        x="date",
        y="points",
        color="type",
        height=500,
    )
    fig.update_layout(plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor="rgba(0,0,0,0)")
    fig.update_layout(margin=dict(l=1))
    plot_div = pio.to_html(fig, full_html=False)

    return render_template("home.html", plot_div=plot_div, ppg=12, games=12)


if __name__ == "__main__":
    app.run(debug=True)
