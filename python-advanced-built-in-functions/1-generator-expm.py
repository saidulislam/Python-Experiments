def get_next_number():
    i = 0
    while i < 100:
        yield i
        i += 1

next_number =get_next_number()

print(next(next_number))
print(next(next_number))

#print(list(next_number))

def prime_generator(bound):
    # n starts from 2 to bound
    for n in range(2, bound):
        # check if there is a number x (1<x<n) that can divide n
        for x in range(2, n):
            if n % x == 0:
                # as long as we can find any such x, then n is not prime
                break
        else:
            # if no such x is found after exhausting all 1<x<n
            # generate this prime
            yield  n

print(list(prime_generator(10)))



