import time

from pika import BlockingConnection, ConnectionParameters


def connect_and_produce():
    """
    We don't set it up as you would generally do in a production environment.

    First off, we make use of the Default exchange since we don't supply an exchange name, normally you would supply
    a specific exchange which allows you to control a lot better where your messages are being sent.

    second we use the routing key to define to which queue we're sending this stuff, and creating the queue within the
    function. As that is not impossible, you will often see the queues and exchanges being defined in some central
    place so you can use them in different places.

    For now this works, yay!

    :return:
    """
    connection = BlockingConnection(ConnectionParameters('localhost'))
    try:
        channel = connection.channel()
        channel.queue_declare(queue='hello')
        while True:
            channel.basic_publish(exchange='',
                                  routing_key='hello',
                                  body=b'Hello World!')
            time.sleep(1)
    finally:
        connection.close()

if __name__ == '__main__':
    connect_and_produce()