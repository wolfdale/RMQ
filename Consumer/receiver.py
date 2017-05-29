import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
#Define a Name for Rabbit Que
channel.queue_declare(queue='runner')

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
    if body[0] == '+':
	adder(body)
    elif body[0] == '*':
	multiply(body)
    elif body[0] == '-':
	substract(body)
    elif body[0] == '/':
	divide(body)
    else:
	print "Worng format"

    #param = body.split("+")
    #result = int(param[0]) + int(param[1])
    #print result


def adder(param):
    result = int(param[1]) + int(param[2])
    print result
    
def multiply(param):
    result = int(param[1]) * int(param[2])
    print result
    
def substract(param):
    result = int(param[1]) - int(param[2])
    print result

def divide(param):
    result = float(param[1]) / float(param[2])
    print result

channel.basic_consume(callback,
                      queue='runner',
                      no_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
