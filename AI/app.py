from flask import Flask, render_template, request
from textblob import TextBlob

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    text = request.form["comment"]
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity

    if polarity > 0.1:
        sentiment = "Positive"
    elif polarity < -0.1:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    return render_template("index.html", prediction=sentiment, input_text=text)

if __name__ == "__main__":
    app.run(debug=True)
