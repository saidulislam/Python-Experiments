import argparse

# Showing both short and long argument options

def get_args():
    """"""
    parser = argparse.ArgumentParser(
        description="A simple argument parser",
        epilog="This is where you might put example usage"
    )

    # required argument
    parser.add_argument('-x', '--execute', action="store", required=True,
                        help='Help text for option X')
    # optional arguments
    parser.add_argument('-y', '--message1', help='Help text for option Y', default=False)
    parser.add_argument('-z', '--message2', help='Help text for option Z', type=int)
    
    print(parser.parse_args())

if __name__ == '__main__':
    get_args()

'''
$ arg_demo_3.py
usage: arg_demo_3.py [-h] -x EXECUTE [-y MESSAGE1] [-z MESSAGE2]
arg_demo_3.py: error: the following arguments are required: -x/--execute
$ arg_demo_3.py --execute something
Namespace(execute='something', message1=False, message2=None)
$ arg_demo_3.py --execute something --message1 text1 --message2 text2
usage: arg_demo_3.py [-h] -x EXECUTE [-y MESSAGE1] [-z MESSAGE2]
arg_demo_3.py: error: argument -z/--message2: invalid int value: 'text2'
$ arg_demo_3.py --execute something --message1 text1 --message2 100  
Namespace(execute='something', message1='text1', message2=100)
'''