from pika import BlockingConnection, ConnectionParameters


def callback(ch, method, properties, body):
    print(f" [x] Received {body}, the other stuff is -> {ch=}, {method=}, {properties=}")


def connect_and_receive():

    connection = BlockingConnection(ConnectionParameters('localhost'))
    try:
        channel = connection.channel()
        channel.queue_declare(queue='hello')
        channel.basic_consume(queue='hello',
                              on_message_callback=callback,
                              auto_ack=True)
        channel.start_consuming()
    finally:
        connection.close()


if __name__ == '__main__':
    connect_and_receive()