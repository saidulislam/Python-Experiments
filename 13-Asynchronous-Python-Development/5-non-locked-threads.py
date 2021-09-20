from threading import Thread
import time
import random

counter = 0

def increment_counter():
	global counter
	time.sleep(random.randint(0, 2))
	counter += 1
	time.sleep(random.randint(0, 2))
	print(f'New counter value: {counter}')
	time.sleep(random.randint(0, 2))
	print('-----------')

# not how you would use in real life examples
# this is to show as an example

if __name__ == '__main__':
    for x in range(10):
        t = Thread(target=increment_counter)
        time.sleep(random.randint(0,2))
        t.start()
