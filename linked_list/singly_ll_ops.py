import argparse

class node:
    def __init__(self, val = None):
        self.data = val
        self.next = None

class list_head:
    def __init__(self):
        self.head = None

    def traverse(self, pos):
        i = 0
        elem = self.head
        while i != (pos - 1):
            i += 1
            elem = elem.next
            if elem is None:
                print('Error: Position out of bound')
                return None
        return elem

    def prepare(self, file):
        lines = file.readlines()
        self.head = node(int(lines[0].strip("\n")))
        elem = self.head
        for line in lines[1:]:
            elem.next = node(int(line.strip("\n")))
            elem = elem.next

    def print(self,  file, update=False):
        i = 0
        elem = self.head
        while(elem):
            print("|elem(%d):%d| --> " % (i, elem.data), end='')
            if(update):
                file.write(str(elem.data) + "\n")
            elem = elem.next
            i += 1
        print("NULL")

    def add(self, pos, elem_val):
        elem = self.traverse(pos)
        if elem is None:
            return
        new_elem = node(elem_val)
        new_elem.next = elem.next
        elem.next = new_elem

    def delete(self, pos):
        elem = self.traverse(pos)
        if elem is None:
            return
        del_node = elem.next
        elem.next = del_node.next
        del_node.next = None


list = list_head()


def open_and_prepare():
    f = open('ll_nodes.txt', 'r')
    list.prepare(f)
    f.close()


def main(args):
    open_and_prepare()
    if args.print:
        f = open('ll_nodes.txt', 'r')
        list.print(f)
        f.close()
    elif args.add:
        pos_val = args.add.split(':')
        f = open_and_prepare()
        list.add(int(pos_val[0]), int(pos_val[1]))
        f = open('ll_nodes.txt', 'w+')
        list.print(f, True)
        f.close()
    elif args.delete:
        pos_val = args.delete
        open_and_prepare()
        list.delete(int(pos_val))
        f = open('ll_nodes.txt', 'w+')
        list.print(f, True)
        f.close()
    else:
        print("Invalid argument")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Code for operations on singly linked list")
    parser.add_argument("--print", "-p", action='store_true', help="Print current linked list")
    parser.add_argument("--add", "-a", metavar="pos:val", help="Add node at position")
    parser.add_argument("--delete", "-d", type=int, help="Delete node at position")
    main(parser.parse_args())
