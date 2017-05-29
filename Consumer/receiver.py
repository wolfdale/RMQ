import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
#Define a Name for Rabbit Que
channel.queue_declare(queue='runner')

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
    param = body.split("+")
    result = int(param[0]) + int(param[1])
    print result

channel.basic_consume(callback,
                      queue='runner',
                      no_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
