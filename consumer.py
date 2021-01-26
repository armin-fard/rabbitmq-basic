#!/usr/bin/env python
import pika

credentials = pika.PlainCredentials('con-1', 'secret')
connection = pika.BlockingConnection(pika.ConnectionParameters('ec2-34-219-237-101.us-west-2.compute.amazonaws.com', 5672, '/', credentials, socket_timeout=300))
channel = connection.channel()

channel.queue_declare(queue='sample_test', durable=True)

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)

channel.basic_consume(callback,
                      queue='sample_test',
                      no_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()