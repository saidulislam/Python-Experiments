from Database import Database
from Admin import Admin

a = Admin('Kent', 'Flor', 2)
b = Admin('Mark', 'Smith', 1)

a.save()
b.save()

user = Database.find(lambda x: x['username'] == 'Mark')[0]
user_obj = Admin(**user)
print(user_obj.username)