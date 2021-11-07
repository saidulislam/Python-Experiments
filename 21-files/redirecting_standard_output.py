import sys

class RedirectStdoutTo:
    def __init__(self, out_new):
        self.out_new = out_new

    def __enter__(self):
        self.out_old = sys.stdout
        sys.stdout = self.out_new

    def __exit__(self, *args):
        sys.stdout = self.out_old

print('A')
# nested with
with open('out.log', mode='w', encoding='utf-8') as a_file, RedirectStdoutTo(a_file):
    print('B')
print('C')

# you can also write the above with statement like the following
# with open('out.log', mode='w', encoding='utf-8') as a_file:
#     with RedirectStdoutTo(a_file):
#         print('B')