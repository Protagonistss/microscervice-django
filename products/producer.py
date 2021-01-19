#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: huangshan
# datetime: 2021-01-16 22:26
# software: PyCharm

import pika, json, os

amqpUlr = os.getenv('AMQPURL')
paramas = pika.URLParameters(amqpUlr)
connection = pika.BlockingConnection(paramas)
channel = connection.channel()


def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='integral', body=json.dumps(body), properties=properties)
