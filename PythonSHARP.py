"""
===========================
████ █ █ ███ █ █ ███ █  █ #
█  █  █   █  █ █ █ █ ██ █
████  █   █  ███ █ █ █ ██
█    █    █  █ █ █ █ █  █
█   █     █  █ █ ███ █  █
===========================
            Version 3.17.4

Python# is an open source module that allows the branching, convenient creation of objects.
It also had storable variables and useful functions to use.

----------------------------------------------------------------
from PythonSHARP import *
playerInfoStuff = [
Instance('Health', 'IntStore', [['Value', 0, 0]]),
Instance('Level', 'IntStore', [['Value', 1, 0]]),
Instance('XP', 'FloatStore', [['Value', 0.0, 0.0]]),
Instance('XP Max', 'FloatStore', [['Value', 10.0, 0.0]]),
Instance('Health', 'IntStore', [['Value', 100, 0]]),
Instance('Name', 'StringStore', [['Name', '', '']]),
Instance('Character', 'ObjectStore', [['Value', None, None]])
]

objects = Instance('ObjectStorage', 'service', [])

objects.newChild(Instance('PlayerInfo', 'folder', []))
playerInfo = objects.findSpecificChild('PlayerInfo', 'folder')

for s in playerInfoStuff: playerInfo.newChild(s)
----------------------------------------------------------------

Created by Daniel; copyright (©) 2020 Daniel Lawson.
github.com/Sombrero64

Python# uses the MIT license (mit).

CREDITS
▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔
18001767679
Dan's Papa (Grandfather)
"""

def info(): print(__doc__) 

# Imports
import warnings, random

# Oprations
def addty(var):
    """
    returns the sum of all items in {var}
    """
    num = 0.0
    for i in var: num += i
    return num

def join(var):
    """
    returns a joined string of all items in {var}
    """
    string = ''
    for i in var: string += str(i)
    return string

def subty(var):
    """
    returns the difference of all items in {var}
    """
    num = var[0] * 2.0
    for i in var: num -= i
    return num

def multy(var):
    """
    returns the product of all items in {var}
    """
    num = 1.0
    for i in var: num *= i
    return num

def didty(var):
    """
    returns the quotient of all items in {var}
    """
    num, passer = var[0], False
    for i in var:
        if passer:
            if i == 0: raise ZeroDivisionError('division by zero')
            else: num /= i
        else: passer = True
    return num
    
def limit(num, nin, nax):
    """
    returns {num} with a range limit

    returns {nax} if {num} is bigger than it;
    returns {nin} if {num} is smaller than it
    """
    if num > nax: return nax
    elif num < nin: return nin
    else: return num
    
def pairs(var, item):
    """
    returns a list of indexes of {var}'s items that equals to {item}
    """
    items = []
    for j in range(len(var)):
        if var[j] == item: items.append(j)
    return items
        
def filterList(var, item):
    """
    returns {var} without items that equals to {item}
    """
    items = []
    for j in var:
        if j != item: items.append(j)
    return items

def itemIndex(var, indexs):
    """
    returns items from {var} based of a list of indexes from {indexs}
    """
    items = []
    for i in indexs: items.append(var[i])
    return items

def reverse(value):
    """
    returns {value} from positive to negivite, & vice versa
    """
    return value - value * 2

def genNumList(nin, nax):
    """
    returns a list of integers from {nin} to {nax}
    """
    C, List = nin, []
    while True:
        if not C > nax: List.append(C)
        else: break
        C += 1
    return List

def itemsInt(value):
    """
    returns {value}'s items converted into a integer
    """
    newList = []
    for i in value: newList.append(int(float(i)))
    return newList

def itemsFloat(value):
    """
    returns {value}'s items converted into a float
    """
    newList = []
    for i in value: newList.append(float(i))
    return newList

def itemsStr(value):
    """
    returns {value}'s items converted into a string
    """
    newList = []
    for i in value: newList.append(str(i))
    return newList

def itemsList(value):
    """
    returns {value}'s items converted into a list
    """
    newList = []
    for i in value: newList.append(list(i))
    return newList

def boolList(value):
    """
    returns {value}'s items converted into a Boolean
    """
    newList = []
    for i in value: newList.append(bool(i))
    return newList

def shutItems(value):
    """
    returns {value}'s items placed into an empty list
    """
    newList = []
    for i in value: newList.append([i])
    return newList

def orItems(value):
    """
    prefroms an or opration on all {value}'s items
    """
    for b in value:
        if b: return True
    return False

def andItems(value):
    """
    prefroms an and opration on all {value}'s items
    """
    for b in value:
        if not b: return False
    return True

def xorItems(value):
    """
    prefroms an ^ (xor) opration on all {value}'s items
    """
    testBoolean = False
    for b in value:
        if b:
            if testBoolean: return False
            else: testBoolean = True
    return testBoolean

def balance(value, nim, nax):
    """
    returns True if the count of true Booleans from {value} is around {nim} & {nax}
    """
    count = 0
    for b in value:
        if b: count += 1
    return count >= nim and count <= nax

def factors(number):
    """
    returns the factors of {number}
    """
    factors, counter = [], 1
    while True:
        if number % counter == 0: factors.append(counter)
        if counter >= number: return factors
        counter += 1

def commonFactor(num1, num2):
    """
    returns the greatest common factor (gcf) of {num1} & {num2}
    """
    counter, num = 1, None
    while True:
        if num1 % counter == 0 and num2 % counter == 0: num = counter
        if counter > num1 and counter > num1: return num
        counter += 1

def multiples(number, nax):
    """
    returns the multiples of {number} based on a limit of {nax}
    """
    multiples = []
    for q in range(nax): multiples.append(number * (q + 1))
    return multiples

def commonMultiple(num1, num2, nax):
    """
    returns the lowest common multiple of {num1} & {num2} based on a limit of {nax}
    """
    one, two = [], []
    for q in range(nax):
        one.append(num1 * (q + 1))
        two.append(num2 * (q + 1))
    for o in one:
        for t in two:
            if o == t: return o
    return None

def randItem(var):
    """
    returns a random item from {var}
    """
    return var[random.randint(0, len(var) - 1)]

def proba(var):
    """
    returns True if a random number from 0 to {var} equals 0
    """
    return random.randint(0, var) == 0

def test(boolean, one, two):
    """
    if {boolean} is True, then return {one}. {two} if false
    """
    return one if boolean else two

def contains(var, item):
    """
    returns True if {var} contains an item that equals to {item}
    """
    for i in var:
        if i == item: return True
    return False

def sort(var):
    """
    returns {var} being sorted from smallest to greatest
    """
    sort, numbers = [], var
    for i in range(len(var)):
        sort.append(min(var))
        numbers.pop(numbers.index(min(var)))
    return sort

def flip(var):
    """
    returns {var}'s order of all of its items reversed
    """
    new, length = [], len(var)
    for i in range(length): new.append(var[length - (i + 1)])
    return new

# Inputs

def intInput(caption):
    """
    returns the integer the user provided
    """
    test, final = None, ''
    while True:
        an = input(caption)
        try:
            test = int(an)
            final = 'int'
        except: pass
        if final == 'int': return test

def floatInput(caption):
    """
    returns the number the user provided
    """
    test, final = None, ''
    while True:
        an = input(caption)
        try:
            test = float(an)
            final = 'int'
        except: pass
        if final == 'int': return test

def boolInput(caption):
    """
    returns either True or False depending what the user provided
    """
    while True:
        an = input(caption)
        for i in['y', 'Y', 'yes', 'Yes', 'YES']:
            if an == i: return True
        for i in['n', 'N', 'no', 'No', 'NO']:
            if an == i: return False

def Menu(options, none):
    """
    displays a mutlichoice list of the items from {options},
    and returns the index of the select item

    if {none} is true, then the user is allowed to provide an empty string
    if the user provided as such, then None is returned
    """
    if len(options) < 2: raise ValueError('list argument must contain at least 2 items')
    else:
        for s in options: print(str(options.index(s) + 1) + ': ' + s)
        while True:
            my, test, final = input('└> '), None, ''
            try:
                test = int(my)
                final = 'num'
            except: final = 'str'
            if final == 'num' and test > 0 and test <= len(options): return (test - 1)
            elif final == 'str':
                if my == '' and none: return None
                else:
                    for si in options:
                        if my == si: return options.index(si)

# Packages (Local Variables)

class Package():
    """
    Packages are variables stored in a Package() object.
    """
    def __init__(self): self.CONTENT = []
    def __len__(self): return len(self.CONTENT)

    def define(self, Name, Value):
        """
        creates a new package named {Name} with the value of {Value}
        """
        testBool = True
        for i in self.CONTENT:
            if i[0] == Name: testBool = False
        if testBool: self.CONTENT.append([Name, Value])

    def set(self, Name, New):
        """
        changes the value of a package named {Name} to {New}
        """
        for i in self.CONTENT:
            if i[0] == Name: i[1] = New

    def change(self, Name, Change):
        """
        increases the value of a package named {Name} by {Change}
        """
        for i in self.CONTENT:
            if i[0] == Name: i[1] += Change

    def rename(self, Name, New):
        """
        renames a package from {Name} to {New}
        """
        for i in self.CONTENT:
            if i[0] == Name: i[0] = New

    def get(self, Name):
        """
        returns the value of {Name}
        returns None if no package was found
        """
        for i in self.CONTENT:
            if i[0] == Name: return i[1]
        return None

    def find(self, Index):
        """
        returns the name of a package by its index ({Index})
        returns None if no package was found
        """
        for i in range(len(self.CONTENT)):
            if i == Index: return self.CONTENT[Index][0]
        return None

    def remove(self, Name):
        """
        finds a package named [Name} and removes it if found
        """
        for i in range(len(self.CONTENT)):
            try:
                if Name == self.CONTENT[i][0]: self.CONTENT.pop(i)
            except IndexError:
                if Name == self.CONTENT[0][0]: self.CONTENT.pop(i)

    def wipe(self):
        """
        removes all packages
        """
        self.CONTENT = []

    def all(self):
        """
        returns the list of all packages

        item 1: name
        item 2: value
        """
        return self.CONTENT

# Objects
# object: [subject, class, children, props, parent, variables]
# prop: [name, value, default, category]
# variable: [name, value]

def dump(Instance):
    """
    returns a list of {Instance}'s content

    1: name
    2: class
    3: properties
    4: children
    5: parent
    6: variables
    """
    try: return [Instance.SUB, Instance.CLASS, Instance.PROPS, Instance.CHILDS, Instance.PARENT, Instance.VARIABLES]
    except: return [Instance[0].SUB, Instance[0].CLASS, Instance[0].PROPS, Instance[0].CHILDS, Instance[0].PARENT, Instance[0].VARIABLES]

def take(Inst):
    """
    returns an Instance() object containing {Inst}'s content
    """
    ripper = Instance(Inst.SUB, Inst.CLASS, Inst.PROPS)
    ripper.CHILDS, ripper.PARENT, ripper.VARIABLES = Inst.CHILDS, Inst.PARENT, Inst.VARIABLES
    return ripper

# [object, parent, parent, etc]
class Path():
    """
    genrates a path of an Instance() object
    """
    def __init__(self, Instance):
        self.PATH = []
        self.PATH.append(Instance)
        if dump(Instance)[4] != None:
            obj = Instance.PARENT
            while True:
                self.PATH.append(obj)
                if dump(obj)[4] == None: break
                else: obj = obj.PARENT

    def __str__(self):
        returnStr, counter = '', 1
        for o in self.PATH:
            if counter < len(self.PATH): returnStr += (dump(o)[0] + ' ~ ')
            else: returnStr += dump(o)[0]
            counter += 1
        return returnStr

class Instance():
    """
    an Instance() object contains a name, class, properties, and children

    property:
        1: name
        2: value
        3: default value
        4: category 
    """
    def __init__(self, Subject, Class, Props):
        self.SUB, self.CLASS = Subject, Class
        self.PROPS = Props
        self.CHILDS, self.PARENT = [], None
        self.VARIABLES = []

    def __str__(self): return self.SUB

    def __add__(self, two):
        """
        adds {two} to {self}
        """
        twos = rip(two)
        twos.PARENT = self
        self.CHILDS.append(two)

    def __sub__(self, two):
        """
        removes the first child that matches {two} in {self}
        """
        for oj in range(len(self.CHILDS)):
            if self.CHILDS[oj] == two: self.CHILDS.pop(oj)

    def __len__(self): return len(self.CHILDS)

    def Sub(self):
        """
        returns the subject (name) of {self}
        """
        return self.SUB
    def Class(self):
        """
        returns the class of {self}
        """
        return self.CLASS
    def Props(self):
        """
        returns the properties of {self}
        """
        return self.PROPS

    def sitSub(self, New):
        """
        renames {self} to {New}
        """
        self.SUB = New
    def sitClass(self, New):
        """
        reclassifies {self} to {New} 
        """
        self.CLASS = New
    def sitProps(self, New):
        """
        sets the propterties of {self} to {New}
        """
        self.PROPS = New

    def newProp(self, Prop):
        """
        adds a new property to {self}
        """
        testBool = True
        for p in self.PROPS:
            if p[0] == Prop[0]: testBool = False
        if testBool: self.PROPS.append(Prop)

    def findProp(self, Prop):
        """
        returns a property named {Prop} from {self}
        """
        for p in self.PROPS:
            if p[0] == Prop: return p
        return None
    
    def gitProp(self, Prop):
        """
        returns the value of a property named {Prop} from {self}
        """
        for p in self.PROPS:
            if p[0] == Prop: return p[1]
        return None

    def sitProp(self, Prop, New):
        """
        sets the value of {Prop} to {New}
        """
        for p in self.PROPS:
            if p[0] == Prop: p[1] = New

    def ritProp(self, Prop):
        """
        sets the value of {Prop} to the default value
        """
        for p in self.PROPS:
            if p[0] == Prop: p[1] = p[2]

    def renameProp(self, Prop, New):
        """
        renames {Prop} to {New}
        """
        for p in self.PROPS:
            if p[0] == Prop: p[0] = New

    def catProp(self, Prop, Category):
        """
        sets the name of {Prop}'s category to {Category}
        """
        for p in self.PROPS:
            if p[0] == Prop: p[3] = Category

    def gatProp(self, Prop):
        """
        gets the name of {Prop}'s category
        """
        for p in self.PROPS:
            if p[0] == Prop: return p[3]

    def allProps(self, Category):
        """
        returns all propterties under the {Category} category
        """
        props = []
        for p in self.PROPS:
            if p[3] == Category: props.append(p)
        return props

    def assignParentAs(self, NewParent):
        """
        sets the parent of {self} to {NewParent}
        """
        self.PARENT = NewParent

    def parent(self):
        """
        returns the parent of {self}
        """
        if self.PARENT == None: return None
        else: return self.PARENT

    def clear(self):
        """
        removes {self} from its parent, then it sets it to None
        """
        if self.PARENT != None:
            for oi in range(len(self.PARENT.CHILDS)):
                if self.PARENT.CHILDS[oi] == self:
                    self.PARENT.CHILDS.pop(oi)
                    self = None
        else: self = None

    def clone(self):
        """
        creates another Instance() object alike {self} in {self}'s parent
        """
        if self.PARENT != None: self.PARENT.CHILDS.append(self)
        else: raise AttributeError('object must have a parent')

    def clearAllChildren(self):
        """
        removes all children from {self}
        """
        self.CHILDS = []

    def replaceChild(self, Child, NewChild):
        """
        replaces {Child} from {self} with {NewChild}
        """
        for oj in range(len(self.CHILDS)):
            if self.CHILDS[oj] == Child: self.CHILDS[oj] = NewChild; self.CHILDS[oj].PARENT = self

    def getChildren(self):
        """
        returns {self}'s children
        """
        return self.CHILDS

    def findChild(self, ChildName):
        """
        returns the first child from {self} that is named as {ChildName}
        returns None if {self} doesn't have it
        """
        for o in self.CHILDS:
            if dump(o)[0] == ChildName: return o
        return None

    def findFirstChild(self, ChildClass):
        """
        returns the first child from {self} that is classifed as {ChildName}
        returns None if {self} doesn't have it
        """
        for o in self.CHILDS:
            if dump(o)[1] == ChildClass: return o
        return None

    def findSpecificChild(self, ChildName, ChildClass):
        """
        returns the first child from {self} that is named as {ChildName} and classifed as {ChildClass}
        returns None if {self} doesn't have it
        """
        for o in self.CHILDS:
            if dump(o)[0] == ChildName and dump(o)[1] == ChildClass: return o
        return None

    def findChildren(self, ChildrenName):
        """
        returns a list of children from {self} that's named {ChildrenName}
        """
        op = []
        for o in self.CHILDS:
            if dump(o)[0] == ChildrenName: op.append(o)
        return op

    def findFirstChildren(self, ChildrenClass):
        """
        returns a list of children from {self} that's classifed {ChildrenClass}
        """
        op = []
        for o in self.CHILDS:
            if dump(o)[1] == ChildrenClass: op.append(o)
        return op

    def findRelatedChildren(self, Name, Class):
        """
        returns a list of children from {self} that's named {ChildrenName} and classifed as {ChildrenClass}
        """
        op = []
        for o in self.CHILDS:
            if dump(o)[0] == Name and dump(o)[1] == Class: op.append(o)
        return op

    def findNamePairs(self, Object):
        """
        return the first child from {self} that shares its name with {Object}
        """
        for o in self.CHILDS:
            if dump(o)[0] == dump(Object)[0]: return o
        return None

    def findClassPairs(self, Object):
        """
        return the first child from {self} that shares its class with {Object}
        """
        for o in self.CHILDS:
            if dump(o)[1] == dump(Object)[1]: return o
        return None

    def findPairs(self, Object):
        """
        return the first child from {self} that shares its name and class with {Object}
        """
        for o in self.CHILDS:
            if dump(o)[0] == dump(Object)[0] and dump(o)[1] == dump(Object)[1]: return o
        return None

    def getNamePairs(self, Object):
        """
        return a list of children from {self} that shares its name with {Object}
        """
        op = []
        for o in self.CHILDS:
            if dump(o)[0] == dump(Object)[0]: op.append(o)
        return op

    def getClassPairs(self, Object):
        """
        return a list of children from {self} that shares its class with {Object}
        """
        op = []
        for o in self.CHILDS:
            if dump(o)[1] == dump(Object)[1]: op.append(o)
        return op

    def getPairs(self, Object):
        """
        return a list of children from {self} that shares its name and class with {Object}
        """
        op = []
        for o in self.CHILDS:
            if dump(o)[0] == dump(Object)[0] and dump(o)[0] == dump(Object)[0]: op.append(o)
        return op

    def NEW(self, Name, Value):
        """
        creates a variable named {Name} for {self} with the value of {Value}
        """
        testBool = True
        for v in self.VARIABLES:
            if v[0] == Name: testBool = False
        if testBool: self.VARIABLES.append([Name, Value])

    def GET(self, Name):
        """
        returns a variable named {Name}'s value
        """
        for v in self.VARIABLES:
            if v[0] == Name: return v[1]
        return None

    def INDEX(self, Index):
        """
        returns a variable from {self} of an index ({Index})
        """
        return self.VARIABLES[Index][0]

    def SET(self, Name, Value):
        """
        sets the value of {self}'s variable to {Value}
        """
        for v in self.VARIABLES:
            if v[0] == Name: v[1] = Value

    def DEL(self, Name):
        """
        deletes a variable from {self}
        """
        for vi in range(len(self.VARIABLES)):
            if self.VARIABLES[vi][0] == Name: self.VARIABLES.pop(vi)
