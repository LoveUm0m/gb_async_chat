import json
import socket
import argparse

Функция для обработки запросов клиента
def process_client_message(message):
    """
    Функция для обработки запросов клиента

:param message: словарь - сообщение от клиента
:return: словарь - ответ сервера
"""
# Проверка наличия ключа 'action' в сообщении
if 'action' in message:
    # Обработка запроса presence
    if message['action'] == 'presence':
        return {'response': 200, 'message': 'OK'}
    # Обработка запроса unknown
    else:
        return {'response': 400, 'error': 'Bad Request'}
# Обработка ошибки - отсутствует ключ 'action'
else:
    return {'response': 400, 'error': 'Bad Request'}


Функция для запуска сервера
def start_server():
    # Создание парсера аргументов командной строки
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', type=int, default=7777, help='TCP-port')
    parser.add_argument('-a', default='', help='IP-address')
    args = parser.parse_args()

# Создание объекта сокета
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Привязка сокета к IP-адресу и порту
sock.bind((args.a, args.p))

# Ожидание подключения клиента
sock.listen(1)
print('Server started!')

while True:
    # Подключение клиента
    conn, addr = sock.accept()
    print(f'Client connected: {addr}')

    # Получение сообщения от клиента
    data = conn.recv(1024)

    # Если сообщение не пустое
    if data:
        # Декодирование сообщения из байтового формата в формат JSON
        message = json.loads(data.decode('utf-8'))

        # Обработка сообщения
        response = process_client_message(message)

        # Кодирование ответа сервера в формат JSON
        response_data = json.dumps(response).encode('utf-8')

        # Отправка ответа клиенту
        conn.sendall(response_data)

    # Закрытие соединения
    conn.close()


Запуск сервера
if name == 'main':
    start_server()Клиентский скрипт client.py:
import json
import socket
import argparse

Функция для создания сообщения presence
def create_presence_message(account_name='Guest'):
    """
    Функция для создания сообщения presence

:param account_name: имя аккаунта, по умолчанию 'Guest'
:return: словарь - сообщение presence
"""
message = {
    'action': 'presence',
    'type': 'status',
    'user': {
        'account_name': account_name
    }
}
return message


Функция для отправки сообщения серверу
def send_message(sock, message):
    """
    Функция для отправки сообщения серверу

:param sock: объект сокета
:param message: словарь - сообщение для отправки
:return: словарь - ответ сервера
"""
# Кодирование сообщения в формат JSON
message_data = json.dumps(message).encode('utf-8')

# Отправка сообщения серверу
sock.sendall(message_data)

# Получение ответа от сервера
data = sock.recv(1024)

# Если ответ не пустой
if data:
    # Декодирование ответа из байтового формата в формат JSON
    response = json.loads(data.decode('utf-8'))
    return response


Функция для запуска клиента
def start_client():
    # Создание парсера аргументов командной строки
    parser = argparse.ArgumentParser()
    parser.add_argument('addr', type=str, help='IP-address')
    parser.add_argument('port', type=int, nargs='?', default=7777, help='TCP