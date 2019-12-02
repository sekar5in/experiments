#!/usr/bin/python

import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

channel = connection.channel()


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)


channel.basic_consume(callback,
                      queue='qht.info',
                      no_ack=True)


print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()

