from collections import defaultdict, OrderedDict, namedtuple, deque

def task1() -> defaultdict:
    dd = defaultdict(lambda: 'Unknown')
    dd['Alan'] = 'Manchester'
    return dd

print(task1())


def task2(arg_od: OrderedDict):
    # arg_od.popitem()
    # arg_od.popitem(False)
    # remember to remove start and end before moving Bob and Dan, otherwise they will be removed instead
    arg_od.move_to_end('Bob')
    arg_od.move_to_end('Dan', False)
    print(arg_od)

o = OrderedDict()
o['Bob'] = 4
o['John'] = 6
o['Dan'] = 10
o['Brent'] = 3
print("\n")
print(o)  # keys are always in the order in which they were inserted

task2(o)


def task3(name: str, club: str) -> namedtuple:
    Player = namedtuple('Player', ['name', 'club'])
    player = Player(name, club)
    return player

p = task3("Lucas", "CBUS")
print(p)


def task4(arg_deque: deque):
    arg_deque.pop()     # remove last element
    arg_deque.append(arg_deque.popleft())   # remove first element and append it to last
    arg_deque.appendleft('Zack')    # add Zack to start

friends = deque(('John', 'Dan', 'Jen', 'Anna'))
task4(friends)
print(friends)