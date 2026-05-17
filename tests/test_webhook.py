import os
import unittest
from unittest.mock import patch

from chatbot_whatsapp import create_app


class WhatsAppWebhookTests(unittest.TestCase):
    def setUp(self) -> None:
        app = create_app()
        app.config.update(TESTING=True)
        self.client = app.test_client()

    def test_health_route(self) -> None:
        response = self.client.get("/health")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"status": "ok"})

    def test_menu_response(self) -> None:
        response = self.client.post("/webhook/whatsapp", data={"Body": "menu"})

        self.assertEqual(response.status_code, 200)
        body = response.get_data(as_text=True)
        self.assertIn("Menu:", body)
        self.assertIn("Horário de atendimento", body)

    def test_unknown_message_response(self) -> None:
        response = self.client.post("/webhook/whatsapp", data={"Body": "xpto"})

        self.assertEqual(response.status_code, 200)
        body = response.get_data(as_text=True)
        self.assertIn("Não entendi", body)

    def test_invalid_twilio_signature_returns_403(self) -> None:
        with patch.dict(os.environ, {"TWILIO_AUTH_TOKEN": "fake-token"}, clear=False):
            app = create_app()
            app.config.update(TESTING=True)
            client = app.test_client()

            response = client.post("/webhook/whatsapp", data={"Body": "menu"})

            self.assertEqual(response.status_code, 403)


if __name__ == "__main__":
    unittest.main()
