from flask import jsonify
from model import generate_ai_reply


def register_routes(app):

    @app.route("/")
    def home():

        return jsonify({
            "message": "Customer Support Assistant Backend Running"
        })

    @app.route("/generate")
    def generate_reply():

        sample_message = "My order has not arrived yet."

        reply = generate_ai_reply(sample_message)

        return jsonify({
            "customer_message": sample_message,
            "generated_reply": reply
        })