import json, pika, time


def update_student(ch, method, properties, body):
    data = json.loads(body)
    name = data.get('name')
    email = data.get('email')
    status = 'concluído'
    time.sleep(2)
    print(f'Aluno atualizado: {name} - {email} - {status}')
    ch.basic_ack(delivery_tag=method.delivery_tag)

if __name__ == '__main__':
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.basic_consume(
        queue='update_student',
        on_message_callback=update_student,
    )

    channel.start_consuming()