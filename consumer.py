#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: huangshan
# datetime: 2021-01-17 02:08
# software: PyCharm

import pika

amqpUlr = "amqps://favhlvqn:LM9kccEJ9RNfPUuolNurqHzPXClFkP-m@orangutan.rmq.cloudamqp.com/favhlvqn"

params = pika.URLParameters(amqpUlr)
connection = pika.BlockingConnection(params)
channel = connection.channel()
channel.queue_declare(queue='admin')


def callback(ch, method, properties, body):
    print('Received in admin')
    print(body)


channel.basic_consume(queue='admin', on_message_callback=callback, auto_ack=True)

print('Started Consuming')

channel.start_consuming()

channel.close()
