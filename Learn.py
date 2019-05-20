
import random
import string

def pr(something):
    print(something, end=" ")

def prl(something):
    print(something)

def random_string(length):
    return ''.join([random.choice(string.ascii_letters + string.digits) for n in range (length)]) # neat implementation found at:  https://pythontips.com/2013/07/28/generating-a-random-string/

class Node:

    def __init__(self, val):
        self.val = val
        self.uniqueId = random_string(32)
        self.children = []

    def parent(self):
        return self.parent

    def next(self):
        return self.next

    def val(self):
        return self.val

    def id(self):
        return self.uniqueId

    def children(self):
        return self.children

    def addChild(self, child_node):
        self.children.append(child_node)

    def firstChild(self):
        return self.children[0]

    def n_children(self):
        return len(self.children)

    def lastChild(self):
        return self.children[self.n_children()-1]

    def equals_v(self, node):
        return self.val() == node.val()

    def equals_id(self, node):
        return self.uniqueId == node.uniqueId



class Tree:

    def __init__(self, root_node):
        self.root = root_node

    def indent(self, level):
        if (level > 0):
            pr(" ")
            self.indent(level-1)

    def preorder_traversal_n(self, node, i):
        # print it
        self.indent(i)
        pr(node.val)
        print("")
        # print it's children
        children = node.children
        for child in children:
            self.preorder_traversal_n(child, i+1)

    def preorder_transversal(self):
        self.preorder_traversal_n(self.root, 0)

class Str:

    def __init__(self, val):
        self.str = val
        self.charAt = 0
        self.MAX_LENGTh  = len(val)

    def peek(self, i):
        if (self.charAt < self.MAX_LENGTh):
            # print("Comparing ", self.str[self.charAt], " to ", i)
            return self.str[self.charAt] == i
        else:
            return False

    def next(self):
        # if (self.charAt < self.MAX_LENGTh - 1):
            self.charAt += 1
        # else:
        #     print("Error: Tried to go to next when couldn\'t")

    def getNextChar(self):
        # print("Retreiving char ", self.charAt)
        if (self.charAt < self.MAX_LENGTh - 1):
            return self.str[self.charAt]
        else:
            return '\0'

    def process(self, i):
        if self.peek(i):
            self.next()
            return True
        return False

    def processList(self, _list):
        for i in _list:
            if self.process(i):
                return True
        return False

    def preprocess(self, i):
        if self.peek(i):
            return True
        return False

    def preprocessList(self, _list):
        for i in _list:
            if self.preprocess(i):
                return i
        return None

    def done(self):
        return (self.charAt == self.MAX_LENGTh)


def null(obj):
    return obj is None

def testTree():
    c1 = Node(10)
    c2 = Node(20)
    c3 = Node(30)
    c4 = Node(40)
    c5 = Node(50)
    c6 = Node(60)
    c7 = Node(70)

    c1.addChild(c2)
    c1.addChild(c3)

    c5.addChild(c6)
    c5.addChild(c7)

    # parent
    c4.addChild(c1)
    c4.addChild(c5)

    tree = Tree(c4)
    tree.preorder_transversal()





def eps_Node(par_letter):
    return new_Node_l(par_letter, "EPS")

def new_Node_l(par_letter, child_letter):
    par = Node(par_letter)
    n = Node(child_letter)
    par.addChild(n)
    return par

def new_Node_n(par_letter, child_node):
    par = Node(par_letter)
    par.addChild(child_node)
    return par

def new_Node_nList(par_letter, child_nodes):
    par = Node(par_letter)
    for child_node in child_nodes:
        par.addChild(child_node)
    return par

def node_D(_string):
    digit_list = ['0', '1', '2',  '3', '4', '5', '6', '7', '8', '9']
    letter = _string.preprocessList(digit_list)
    if not null(letter):
        _string.next()
        return new_Node_l('D', letter)
    return None

def node_P(_string):
    if  _string.process('^'):
        child_node = node_D(_string)
        if not null(child_node):
            return new_Node_n('P', child_node)
        else:
            return None
    else:
        return eps_Node("P")

def node_V(_string):
    letter = _string.preprocessList(['x','y','z'])
    if _string.process('x') or _string.process('y') or _string.process('z'):
        return new_Node_l('V', letter)
    return None

def node_VP(_string):

    if (_string.process('(')):
        v_node =  node_V(_string)
        if not null(v_node):
            if (_string.process(')')):
                p_node = node_P(_string)
                if not null(node_P(_string)):
                    return new_Node_nList("VP", [v_node, p_node])
                return None
            return None
        return None

    v_node =  node_V(_string)

    if not null(v_node):
        p_node = node_P(_string)
        if not null(p_node):
            return new_Node_nList("VP", [v_node, p_node])
        else:
            return None

    return None

def isC(_string):

    if isVP(_string):
        if isC(_string):
            return True
        else:
            return False

    else:
        return False

def str_to_int(_str):
    try:
        i = int(_str)
        return i

    except ValueError:
        print("Could not convert!")
        return None

#
# def Node_evaluate(node):
#     if (node.val() == 'D'): # D node
#         return str_to_int(node.val())
#     if (node.val() == 'V')




# D -> 1|2|3|4|5...
# V ->  x|y|z
# VD -> V | D
# P -> ^ D | NULL
# VP -> VD P | (E) P
# F -> +- VP | VP
# T  -> */ F T | F E
# E -> (T) P | T | NULL



def isD(_string):
    digit_list = ['0', '1', '2',  '3', '4', '5', '6', '7', '8', '9']
    if _string.processList(digit_list):
        return True
    return  False

def isV(_string):
    if _string.process('x') or _string.process('y') or _string.process('z'):
        return True
    return False

def isVD(_string):
    if isV(_string) or isD(_string):
        return True
    return False

def isP(_string):
    if  _string.process('^'):
        if isD(_string):
            return True
        else:
            return False
    else:
        return True

def isVP(_string):

    if (_string.process('(')):
        if isT(_string):
            if (_string.process(')')):
                if isP(_string):
                    return True
                return False
            return False
        return False

    if isVD(_string):
        if isP(_string):
            return True
        else:
            return False

    return False

def isF(_string):
        if (_string.process('+') or _string.process('-')):
            if isVP(_string):
                return True
            return False
        if isVP(_string):
            return True
        return False


def isT(_string):
    if (_string.process('*') or _string.process('/')):
        if isF(_string):
            if isT(_string):
                return True
            return False
        return False
    if isF(_string):
        if isT(_string):
            return True
        return False;
    return False

def isE(_string):
    if (_string.process('(')):
        if isT(_string):
            if (_string.process(')')):
                if isP(_string):
                    return True
                return False
            return False
        return False

    if isT(_string):
        return True

    if _string.done():
        return True
    return False

def parse(_string):
    res = isE(_string)
    if (res and _string.done()):
        return True
    return False

# D -> 1|2|3|4|5...
# V ->  x|y|z
# VD -> V | D
# P -> ^ D | NULL
# VP -> VD P | (E) P
# F -> +- VP | VP
# T  -> */ F T | F E
# E -> (T) P | T | NULL


# F -> +- VP | VP | NULL
# T  -> */ F | F E
# E -> (T F) P | T F | NULL

# Parsing function below works for exponents

def parseTree_for(openinga_parse_function, _string):
    t = openinga_parse_function(_string)
    if not null(t):
        if (_string.done()):
            return Tree(t)
        return None
    return None

def null(obj):
    return obj is None

def exists(obj):
    return not(obj is None)

def parse_timeee_babbyyyyyy(node):
    if (null(node) or node.val == 'EPS'):
        return 1
    if (node.val == 'D'):
        return int(node.firstChild().val)#int(parse_timeee_babbyyyyyy(node.firstChild()))
    if (node.val == 'V'):
        return 10;
    if (node.val == 'P'):
        return int(parse_timeee_babbyyyyyy(node.lastChild()))
    if (node.val == "VP"):
        if (node.firstChild == '('):
            return pow(parse_timeee_babbyyyyyy(node.children[1]),parse_timeee_babbyyyyyy(node.children[3]))
        return pow(parse_timeee_babbyyyyyy(node.children[0]), parse_timeee_babbyyyyyy(node.children[1]))
    if node.val.isDigit():
        return int(node.val)
    return 0

def start():

    try:

        i = input("Enter input: ")

        while i != "QUIT":

            str = Str(i)

            # tree = parseTree_for(node_VP, str)
            #
            # print("Parsing tree: \n")
            #
            # root = tree.root


            try:

                # tree.preorder_transversal()
                #
                # res = parse_timeee_babbyyyyyy(root)
                # print("Parsed output (vars=10) : ", res)

                print("String is in the Context-Free Grammar: ", parse(str))

                i = input("\nEnter input: ")

            except AttributeError as a:

                print("Sorry!  ", a)

                i = input("\nEnter input: ")




    except KeyboardInterrupt:

        prl("\n\n\n\t~~You should have entered something! Quitting..~~")


start()




















