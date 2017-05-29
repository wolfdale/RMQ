import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='runner')



channel.basic_publish(exchange='',
			routing_key='runner',
			body="5+2")
print "[x] Sent !!"
connection.close()


