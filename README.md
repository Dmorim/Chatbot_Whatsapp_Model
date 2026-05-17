# Chatbot_Whatsapp_Model

Framework base para desenvolvimento de chatbots de WhatsApp com **Python + Flask + Twilio**, voltado para estudo e para acelerar projetos freelance.

## Características
- Estrutura simples em Flask com `app factory`
- Webhook para WhatsApp em `/webhook/whatsapp`
- Lógica de respostas baseada em regras (sem uso de GenIA)
- Validação de assinatura do Twilio quando `TWILIO_AUTH_TOKEN` está configurado
- Fácil de expandir para novos fluxos de atendimento

## Como executar
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
export TWILIO_AUTH_TOKEN="seu_auth_token"  # recomendado em produção
python app.py
```

Por padrão, a aplicação roda em `127.0.0.1:5000`.
Você pode ajustar com `FLASK_RUN_HOST` e `FLASK_RUN_PORT`.

## Testes
```bash
python -m unittest discover -s tests
```

## Configuração no Twilio
No sandbox/console do WhatsApp no Twilio, configure a URL de webhook para:

`https://SEU_DOMINIO/webhook/whatsapp`

com método **HTTP POST**.
