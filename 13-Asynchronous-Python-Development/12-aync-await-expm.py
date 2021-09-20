from collections import deque
from types import coroutine

friends = deque(("Mark", "Mike", "Taylor", "Hugo", "Anna"))


@coroutine
def friend_upper():
    while friends:
        friend = friends.popleft().upper()
        greeting = yield
        print(f"{greeting} {friend}")

async def greet(g):
    print('Starting...')
    await g
    print('Ending...')


greeter = greet(friend_upper())
greeter.send(None) # priming
greeter.send('Hello')

greeting = input("Enter a greeting: ")
greeter.send(greeting)

greeting = input("Enter another greeting: ")
greeter.send(greeting)
