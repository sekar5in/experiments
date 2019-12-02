import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s:%(levelname)s:%(message)s')

def add(x,y):
   '''add function '''
   return x + y

def subtract(x,y):
   '''subtract function '''
   return x - y

num_1 = 20
num_2 = 30

add_result = add(num_1, num_2)

logging.debug('ADD :  {} + {} = {}'.format(num_1, num_2, add_result))


sub_result = subtract(num_1, num_2)

logging.debug('SUB :  {} - {} = {}'.format(num_1, num_2, sub_result))
