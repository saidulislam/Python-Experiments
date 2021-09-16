class FirstHundredGenerator():
    def __init__(self):
        self.number = 0
    
    def __next__(self):
        if self.number < 100:
            current = self.number
            self.number += 1
            return current
        else:
            raise StopIteration()

    def __iter__(self):
        return self


print(list(FirstHundredGenerator()))

# you have to have __iter__ method implemented 
# to be able to call sum or use for

# print(sum(FirstHundredGenerator()))

# for i in FirstHundredGenerator():
#     print(i)


class AnotherIterable:
    def __init__(self):
        self.cars = ['Fiesta', 'Focus']

    def __len__(self):
        return len(self.cars)

    def __getitem__(self, i):
        return self.cars[i]


for car in AnotherIterable():
    print(car)


# list comprehension
my_numbers = [x for x in [1, 2, 3, 4, 5]]
print(my_numbers)

# like list comprehension, we can also do
# generator comprehension
my_number_generator = (x for x in [1, 2, 3, 4, 5])
print(next(my_number_generator))
print(next(my_number_generator))
print(next(my_number_generator))

