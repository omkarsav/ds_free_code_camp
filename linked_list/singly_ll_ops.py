import argparse
import random

class node:
    def __init__(self, val = None):
        self.data = val
        self.next = None


class list_head:
    def __init__(self):
        self.head = None


list = list_head()
elem_vals = [1,4, 57, 6, 70]

def main(args):
    if args.print:
        list.head = node(elem_vals[0])
        elem = list.head
        for i in elem_vals:
            elem.next = node(i)
            elem = elem.next

        elem = list.head
        i = 0
        while(elem):
            print("|elem(%d):%d| --> " % (i, elem.data), end='')
            elem = elem.next
            i += 1
        print('NULL')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Code for operations on singly linked list")
    parser.add_argument("--print", "-p", action='store_true', help="Print current linked list")
    parser.add_argument("--add", "-a", metavar="pos:val", help="Add node at position")
    parser.add_argument("--del", "-d", type=int, help="Delete node at position")
    main(parser.parse_args())
