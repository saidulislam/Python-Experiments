user = {
    'id': 1,
    'name': 'jose',
    'role': 'admin'
}


def delete_database():
    # perform deletion
    print('Database deleted!')


def check_permission(func):
    def wrapper():
        if user.get('role') == 'admin':
            return func()
        else:
            raise PermissionError('You are not an admin.')
    return wrapper()

secure_delete_database = check_permission(delete_database)



# another simple example

def welcome_user(func):
    print("Welcome to my application!")
    func()

def say_hello():
    user_name = input("Enter your name: ")
    print(f"Hello, {user_name}!")

welcome_user(say_hello)  # Calls both functions and prints both things.
