"""Flask app factory for WhatsApp chatbot framework."""

from __future__ import annotations

from flask import Flask, Response, request
from twilio.twiml.messaging_response import MessagingResponse

from chatbot_whatsapp.bot import ChatbotFramework


def create_app() -> Flask:
    app = Flask(__name__)
    bot = ChatbotFramework()

    @app.get("/health")
    def health() -> tuple[dict[str, str], int]:
        return {"status": "ok"}, 200

    @app.post("/webhook/whatsapp")
    def whatsapp_webhook() -> Response:
        incoming_text = request.form.get("Body")
        reply = bot.build_reply(incoming_text)

        response = MessagingResponse()
        response.message(reply)

        return Response(str(response), mimetype="application/xml")

    return app
