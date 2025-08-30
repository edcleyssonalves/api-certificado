import json, pika, time


def send_notification(ch, method, properties, body):
    data = json.loads(body)
    name = data.get('name')
    email = data.get('email')
    time.sleep(3)
    print(f'Notificação enviada: {name} - {email}')
    ch.basic_ack(delivery_tag=method.delivery_tag)

if __name__ == '__main__':
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.basic_consume(
        queue='send_notification',
        on_message_callback=send_notification,
    )

    channel.start_consuming()