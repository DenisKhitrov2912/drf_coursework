import requests


def send_message(token, chat_id, message):
    """Функция интеграции с Телеграм"""
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    data = {
        "chat_id": chat_id,
        "text": message
    }

    try:
        response = requests.post(url, data=data)
        response.raise_for_status()  # Проверяем наличие ошибок в ответе
        return response.json()
    except requests.exceptions.RequestException as e:
        print("Ошибка при отправке сообщения:", e)
        return None
