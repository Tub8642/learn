import requests

TELEGRAM_BOT_TOKEN = "8279204061:AAF5js_6MmXXvgJwB41NVueioJD0p1cAGx0"  # Токен от BotFather
TELEGRAM_CHAT_ID = "1121234116"      # ID вашего Telegram-аккаунта

def send_telegram_message(message):
    """Отправляет сообщение в Telegram."""
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message,
        "parse_mode": "HTML",  # Чтобы можно было использовать HTML-теги для форматирования
    }
    try:
        response = requests.post(url, json=payload, timeout=10)
        response.raise_for_status()  # Вызовет исключение, если запрос не удался
    except requests.exceptions.RequestException as e:
        # Здесь можно добавить логирование ошибки
        print(f"Ошибка при отправке сообщения в Telegram: {e}")