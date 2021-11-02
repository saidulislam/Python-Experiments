import argparse

'''
Here, we added subparser = parser.add_subparsers(dest='command'). 
This is used to create the subparser, and the dest='command' is used to 
differentiate between which argument is actually used. You can see in the 
if statement that we distinguish between “login” and “register” 
with args.command.
'''
parser = argparse.ArgumentParser()
subparser = parser.add_subparsers(dest='command')

login = subparser.add_parser('login')
login.add_argument('--username', type=str, required=True)
login.add_argument('--password', type=str, required=True)


register = subparser.add_parser('register')
register.add_argument('--firstname', type=str, required=True)
register.add_argument('--lastname', type=str, required=True)
register.add_argument('--username', type=str, required=True)
register.add_argument('--email', type=str, required=True)
register.add_argument('--password', type=str, required=True)


args = parser.parse_args()


if args.command == 'login':
    print('Logging in with username:', args.username,
            'and password:', args.password)
elif args.command == 'register':
    print('Creating username', args.username,
            'for new member', args.firstname, args.lastname,
            'with email:', args.email,
            'and password:', args.password)

'''
$ arg_demo_6.py login --username jsmith --password superSecret
Logging in with username: jsmith and password: superSecret

$ arg_demo_6.py register --firstname John --lastname Smith --username jsmith --email jsmith@gmail.com --password superSecret
Creating username jsmith for new member John Smith with email: jsmith@gmail.com and password: superSecret
'''
