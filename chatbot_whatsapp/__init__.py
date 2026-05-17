"""Flask app factory for WhatsApp chatbot framework."""

from __future__ import annotations

import os

from flask import Flask, Response, abort, request
from twilio.request_validator import RequestValidator
from twilio.twiml.messaging_response import MessagingResponse

from chatbot_whatsapp.bot import ChatbotFramework


def create_app() -> Flask:
    app = Flask(__name__)
    bot = ChatbotFramework()

    auth_token = os.getenv("TWILIO_AUTH_TOKEN")
    validator = RequestValidator(auth_token) if auth_token else None

    @app.get("/health")
    def health() -> tuple[dict[str, str], int]:
        return {"status": "ok"}, 200

    @app.post("/webhook/whatsapp")
    def whatsapp_webhook() -> Response:
        if validator is not None:
            signature = request.headers.get("X-Twilio-Signature", "")
            form_data = request.form.to_dict(flat=True)
            if not validator.validate(request.url, form_data, signature):
                abort(403)

        incoming_text = request.form.get("Body")
        reply = bot.build_reply(incoming_text)

        response = MessagingResponse()
        response.message(reply)

        return Response(str(response), mimetype="application/xml")

    return app
