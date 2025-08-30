import json, pika, time


def generate_certificate(ch, method, properties, body):
    data = json.loads(body)
    name = data.get('name')
    email = data.get('email')
    course = data.get('course')
    time.sleep(5)
    print(f'Certificado gerado: {name} - {email} - {course}')
    ch.basic_ack(delivery_tag=method.delivery_tag)

if __name__ == '__main__':
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.basic_consume(
        queue='generate_certificate',
        on_message_callback=generate_certificate,
    )

    channel.start_consuming()