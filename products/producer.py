#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: huangshan
# datetime: 2021-01-16 22:26
# software: PyCharm

import pika

amqpUlr = "amqps://favhlvqn:LM9kccEJ9RNfPUuolNurqHzPXClFkP-m@orangutan.rmq.cloudamqp.com/favhlvqn"
paramas = pika.URLParameters(amqpUlr)
connection = pika.BlockingConnection(paramas)
channel = connection.channel()


def publish():
    channel.basic_publish(exchange='', routing_key='integral', body='hello integral')
