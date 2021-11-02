import argparse

def get_args():
    """"""
    parser = argparse.ArgumentParser(
        description="A simple argument parser",
        epilog="This is where you might put example usage"
    )
    return parser.parse_args()

if __name__ == '__main__':
    get_args()

'''
call the script from the command line
$ arg_demo_1.py -h

usage: arg_demo_1.py [-h]

A simple argument parser 

optional arguments:      
  -h, --help  show this help message and exit

This is where you might put example usage
'''