def silly_generator():
    yield "Python"
    yield "Rocks"
    yield "So do you!"
gen = silly_generator()


for item in gen:
    print(item)

# #Python
# #Rocks
# #So do you!