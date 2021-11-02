import argparse

def get_args():
    """"""
    parser = argparse.ArgumentParser(
        description="A simple argument parser",
        epilog="This is where you might put example usage"
    )

    # required argument
    parser.add_argument('-x', action="store", required=True,
                        help='Help text for option X')
    # optional arguments
    parser.add_argument('-y', help='Help text for option Y', default=False)
    parser.add_argument('-z', help='Help text for option Z', type=int)
    
    print(parser.parse_args())

if __name__ == '__main__':
    get_args()

'''
$ arg_demo_2.py -x something
Namespace(x='something', y=False, z=None)
$ arg_demo_2.py -x something -y text
Namespace(x='something', y='text', z=None)
$ arg_demo_2.py -x something -y text -z text2
usage: arg_demo_2.py [-h] -x X [-y Y] [-z Z]
arg_demo_2.py: error: argument -z: invalid int value: 'text2'
$ arg_demo_2.py -x something -y text -z 500  
Namespace(x='something', y='text', z=500)
'''