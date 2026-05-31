from flask import jsonify, request
from model import generate_ai_reply


def detect_sentiment(text):

    negative_words = [
        "angry",
        "sad",
        "upset",
        "late",
        "delay",
        "bad",
        "worst",
        "refund",
        "issue",
        "problem"
    ]

    text = text.lower()

    for word in negative_words:
        if word in text:
            return "Negative"

    return "Positive"


def register_routes(app):

    @app.route("/")
    def home():
        return jsonify({
            "message": "Customer Support Assistant Backend Running"
        })

    @app.route("/generate", methods=["POST"])
    def generate_reply():

        try:

            data = request.get_json()

            customer_message = data.get("message", "")

            reply = generate_ai_reply(customer_message)

            sentiment = detect_sentiment(customer_message)

            return jsonify({
                "status": "success",
                "customer_message": customer_message,
                "generated_reply": reply,
                "sentiment": sentiment,
                "technique_used": "Baseline"
            })

        except Exception as e:

            return jsonify({
                "status": "error",
                "message": str(e)
            })