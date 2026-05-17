"""Core chatbot logic without GenAI dependencies."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class ChatbotFramework:
    """Simple rule-based WhatsApp chatbot for learning and freelance projects."""

    welcome_message: str = (
        "Olá! Sou um chatbot de suporte. Envie 'menu' para ver as opções."
    )

    def build_reply(self, incoming_text: str | None) -> str:
        message = (incoming_text or "").strip().lower()

        if not message:
            return self.welcome_message

        if message in {"oi", "olá", "ola"}:
            return self.welcome_message

        if message == "menu":
            return (
                "Menu:\n"
                "1 - Horário de atendimento\n"
                "2 - Contato comercial\n"
                "3 - Falar com humano"
            )

        if message == "1":
            return "Nosso horário é de segunda a sexta, das 9h às 18h."

        if message == "2":
            return "Contato comercial: comercial@empresa.com"

        if message == "3":
            return "Certo! Em instantes você será direcionado para um atendente."

        return "Não entendi. Envie 'menu' para ver as opções disponíveis."
