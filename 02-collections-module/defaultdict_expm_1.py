from collections import defaultdict

sentence = "The red for jumped over the fence and ran to the zoo for food"
words = sentence.split(' ')

# regular way
# reg_dict = {}
# for word in words:
#     if word in reg_dict:
#         reg_dict[word] += 1
#     else:
#         reg_dict[word] = 1

# print(reg_dict)

# using the same with defaultdict
d = defaultdict(int)
print(d)

for word in words:
    d[word] += 1

print(d)


# using the regular way
my_list = [(1234, 100.23), (345, 10.45), (1234, 75.00),
           (345, 222.66), (678, 300.25), (1234, 35.67)]

# reg_dict = {}
# for acct_num, value in my_list:
#     if acct_num in reg_dict:
#         reg_dict[acct_num].append(value)
#     else:
#         reg_dict[acct_num] = [value]

# print(reg_dict)


# using the same with defaultdict
d = defaultdict(list)
for acct_num, value in my_list:
    d[acct_num].append(value)

print(d)


animal = defaultdict(lambda: "Monkey")
animal['Sam'] = 'Tiger'
# no matter what key use, Monkey will get printed as the value
print (animal['blah']) 
#Monkey

print (animal)
#defaultdict(<function <lambda> at 0x7f32f26da8c0>, {'Nick': 'Monkey', 'Sam': 'Tiger'})