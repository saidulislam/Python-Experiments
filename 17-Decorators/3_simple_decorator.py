user = {'username': 'jose123', 'access_level': 'admin'}


def user_has_permission(func):
    def secure_func():
        if user.get('access_level') == 'admin':
            return func()
    return secure_func()

@user_has_permission
def my_function():
    return 'Password for admin panel is 1234.'


# my_secure_function = user_has_permission(my_function) # we don't this anymore because we are using @user_has_permission
print(my_function)
