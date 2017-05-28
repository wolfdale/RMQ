import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='runner')
channel.basic_publish(exchange='',
			routing_key='runner',
			body="This msg is sent from sender")
print "[x] Sent !!"
connection.close()


