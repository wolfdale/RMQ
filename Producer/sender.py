import pika
import sys
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='runner')


msg = sys.argv[1]
channel.basic_publish(exchange='',
			routing_key='runner',
			body=msg)
print "[x] Sent !!"
connection.close()


