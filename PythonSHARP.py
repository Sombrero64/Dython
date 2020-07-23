"""
===========================
████ █ █ ███ █ █ ███ █  █ #
█  █  █   █  █ █ █ █ ██ █
████  █   █  ███ █ █ █ ██
█    █    █  █ █ █ █ █  █
█   █     █  █ █ ███ █  █
===========================

Python# is an open source module that allows the branching, convenient creation of objects.
It also had storable variables and useful functions to use.

Created by Daniel; copyright (©) 2020 Daniel Lawson.
github.com/Sombrero64

Python# uses the MIT license (mit).

CREDITS
▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔
18001767679
Dan's Papa (Grandfather)
"""
def info(): print(__doc__)

# PYTHON#
# Version 3.15.3

# Imports
import warnings

# Contrants
Errors = [
    # menu(): throw this if the options is set to two (or one but false).
    "must be at least 2 items",
    "function 'menu()' error",
    # waitForChild(): throw this if cannot find a child.
    "infinite waiting for child",
    # newChild(): throw this if the object being added is not an instance.
    "new instance isn't required object",
    # change()/bange(): error when changing
    "local varible must match the changer's type",
    # itemsAddty() + itemsSubty()
    "try using the itemsMerge() function instead of itemsAddty()",
    "function 'itemsAddty()' error",
    "try using the itemsDerge() function instead of itemsSubty()", 
    "function 'itemsSubty()' error",
    # clone(): throw this if the instance is a master
    "cannot clone a master instance"
    ]

Warnings = [
    # waitForChild(): throw this if the child is taking too long
    "possible infinite wait for the child",
    # hold(): throw this if the possibly of an infinite pause.
    "possibly of an infinite pause"
    ]

# Oprations
def itemsAddty(var):
    num = 0
    try:
        for i in list(var): num += float(i)
        return num
    except ValueError:
        raise ValueError(Errors[2])
    except:
        raise RuntimeError(Errors[2])

def itemsMerge(var):
    value = ''
    for i in list(var): value += i
    return value

def itemsSubty(var):
    num = list(var)[0] * 2
    try:
        for i in list(var): num -= float(i)
        return num
    except ValueError:
        raise ValueError(Errors[2])
    except:
        raise RuntimeError(Errors[2])

def itemsMulty(var):
    num = 1
    for i in list(var): num *= float(i)
    return num

def itemsDidty(var):
    num, passer = list(var)[0], False
    for i in list(var):
        if bool(passer):
            if i == 0:
                raise ZeroDivisionError('division by zero')
            else: num /= float(i)
        else: passer = True
    return num
    
def rangeLimit(num, nin, nax):
    if num > nax: return nax
    elif num < nin: return nin
    else: return num
        
def feturn(con, true, false):
    return true if bool(con) else false
    
def listPairs(var, item):
    items = []
    for j in range(len(list(var))):
        if list(var)[j] == item: items.append(j)
    if items != []: return list(items)
    else: return None
        
def filterList(var, item):
    items = []
    for j in list(var):
        if j != item: items.append(j)
    return list(items)

def findGreatestIndex(var):
    number, index = list(var)[0], 0
    for i in range(len(list(var))):
        if list(var)[i] > number:
            number = var[i]
            index = i
    return index

def findSmallestIndex(var):
    number, index = list(var)[0], 0
    for i in range(len(list(var))):
        if list(var)[i] < number:
            number = var[i]
            index = i
    return index

def reverse(value): return value - value * 2

def genNumList(nin, nax):
    C, List = nin, []
    while True:
        if not C > nax: List.append(C)
        else: break
        C += 1
    return list(List)

def itemsInt(value):
    newList = []
    for i in list(value): newList.append(int(i))
    return list(newList)

def itemsFloat(value):
    newList = []
    for i in list(value): newList.append(float(i))
    return list(newList)

def itemsStr(value):
    newList = []
    for i in list(value): newList.append(str(i))
    return list(newList)

def itemsList(value):
    newList = []
    for i in list(value): newList.append([i])
    return list(newList)

def truth(value):
    for s in list(['true', 'yes', 'correct', 'on', 1]):
        if value == s: return True
    for s in list(['false', 'no', 'incorrect', 'off', 0]):
        if value == s: return False
    for s in list(['none', 'nothing', 'nil', 'null', '']):
        if value == s: return None
    return value

def orItems(value):
    for b in list(value):
        if bool(b): return True
    return False

def andItems(value):
    for b in list(value):
        if not bool(b): return False
    return True

def xorItems(value):
    testBoolean = False
    for b in list(value):
        if bool(b):
            if testBoolean: return False
            else: testBoolean = True
    return testBoolean

def truthBalance(value, nim, nax):
    count = 0
    for b in list(value):
        if bool(b): count += 1
    return count >= nim and count <= nax

def factors(number):
    factors, counter = [], 1
    while True:
        if int(number) % counter == 0: factors.append(counter)
        if counter >= number: return list(factors)
        counter += 1

def commonFactor(num1, num2):
    counter, num = 1, 0
    while True:
        if int(num1) % counter == 0 and int(num2) % counter == 0: num = counter
        if counter > num1 and counter > num1: return num
        counter += 1

def multiples(number, nax):
    multiples = []
    for q in range(nax): multiples.append(number * (q + 1))
    return list(multiples)

def commonMultiple(num1, num2, nax):
    one, two = [], []
    for q in range(nax):
        one.append(num1 * (q + 1))
        two.append(num2 * (q + 1))
    for o in list(one):
        for t in list(two):
            if o == t: return o
    return None

def menu(options, noAnwser):
    if len(options) == 0 or (len(options) == 1 and not bool(noAnwser)):
        raise ValueError(Errors[0])
    for optionCount in range(len(options)): print(str(optionCount) + ": " + str(options[optionCount]))
    while True:
        optionAnwser = input("└> ")
        try: testAnwser = int(optionAnwser); mest = 'num'
        except ValueError:
            try: testAnwser = str(optionAnwser); mest = 'string'
            except:
                raise RuntimeError(Errors[1])
        if mest == 'num':
            optionAnswer = int(round(float(testAnwser)))
            if optionAnswer >= 0 and optionAnswer < len(options): return optionAnswer
        elif mest == 'str':
            if bool(noAnwser) and optionAnwser == '': return None
        
# Local Variables

class Localment():
    def __init__(self): self.CONTENT = []
    def __int__(self): return len(list(self.CONTENT))

    def new(self, Name):
        testBool = True
        for i in list(self.CONTENT):
            if list(i)[0] == Name: testBool = False; break
        if bool(testBool): self.CONTENT.append([Name, None])

    def define(self, Name, Value):
        testBool = True
        for i in list(self.CONTENT):
            if list(i)[0] == Name: testBool = False; break
        if bool(testBool): self.CONTENT.append([Name, Value])

    def set(self, Name, New):
        for i in list(self.CONTENT):
            if list(i)[0] == Name: i[1] = New

    def change(self, Name, Change):
        for i in list(self.CONTENT):
            try:
                if list(i)[0] == Name: i[1] += Change
            except TypeError:
                raise TypeError(Errors[2])

    def bange(self, Name, Change):
        for i in list(self.CONTENT):
            try:
                if list(i)[0] == Name: i[1] -= Change
            except TypeError:
                raise TypeError(Errors[2])

    def rename(self, Name, New):
        for i in list(self.CONTENT):
            if list(i)[0] == Name: i[0] = New

    def get(self, Name):
        for i in list(self.CONTENT):
            if list(i)[0] == Name: return i[1]

    def find(self, Index):
        for i in range(len(self.CONTENT)):
            if i == Index: return self.CONTENT[Index][0]
        return None

    def remove(self, Name):
        for i in range(len(self.CONTENT)):
            try:
                if Name == self.CONTENT[i][0]: self.CONTENT.pop(i)
            except IndexError:
                if Name == self.CONTENT[0][0]: self.CONTENT.pop(i)

    def wipe(self): self.CONTENT = []

    def variables(self): return list(self.CONTENT)

# Objects
# object: [subject, class, children, props, parent, variables]
# prop: [name, value, default, category]
# variable: [name, value]

def dump(Instance):
    try: return [Instance.SUB, Instance.CLASS, Instance.PROPS, Instance.CHILDS, Instance.PARENT, Instance.VARIABLES]
    except: return [Instance[0].SUB, Instance[0].CLASS, Instance[0].PROPS, Instance[0].CHILDS, Instance[0].PARENT, Instance[0].VARIABLES]

def rip(Inst):
    ripper = Instance(Inst.SUB, Inst.CLASS, Inst.PROPS)
    ripper.CHILDS = list(Inst.CHILDS)
    ripper.PARENT = Inst.PARENT
    ripper.VARIABLES = list(Inst.VARIABLES)
    return ripper

# [object, parent, parent, etc]
class Path():
    def __init__(self, Instance):
        self.PATH = []
        self.PATH.append(Instance)
        if dump(Instance)[4] != None:
            obj = Instance.PARENT
            while True:
                self.PATH.append(obj)
                if dump(obj)[4] == None: break
                else: obj = obj.PARENT

    def __object__(self): return self

    def __str__(self):
        returnStr = ''
        counter = 1
        for o in list(self.PATH):
            if counter < len(self.PATH): returnStr += (dump(o)[0] + ' ~ ')
            else: returnStr += dump(o)[0]
            counter += 1
        return str(returnStr)

class Instance():
    def __init__(self, Subject, Class, Props):
        self.SUB = str(Subject)
        self.CLASS = str(Class)
        self.PROPS = list(Props)
        self.CHILDS = []
        self.PARENT = None
        self.VARIABLES = []

    def __object__(self): return self

    # Oprations
    def __str__(self): return self.SUB

    def __add__(self, two):
        twos = two
        twos.PARENT = self
        self.CHILDS.append(two)
    
    # Info
    def Sub(self): return self.SUB
    def Class(self): return self.CLASS
    def Props(self): return self.PROPS

    def sitSub(self, New): self.SUB = New
    def sitClass(self, New): self.CLASS = New
    def sitProps(self, New): self.PROPS = list(New)

    def findProp(self, Prop):
        for p in list(self.PROPS):
            if p[0] == Prop: return p
        return None
    
    def gitProp(self, Prop):
        for p in list(self.PROPS):
            if p[0] == Prop: return p[1]
        return None

    def sitProp(self, Prop, New):
        for p in list(self.PROPS):
            if p[0] == Prop: p[1] = New; break

    def ritProp(self, Prop):
        for p in list(self.PROPS):
            if p[0] == Prop: p[1] = p[2]; break

    def assignParentAs(self, NewParent): self.PARENT = NewParent

    def parent(self):
        if self.PARENT == None: return None
        else: return self.PARENT

    # Objects
    def newChild(self, Instance):
        if Instance == None:
            raise ValueError(Errors[2])
        else:
            Instance.PARENT = self; self.CHILDS.append(Instance)

    def clear(self):
        if self.PARENT != None:
            for oi in range(len(list(self.PARENT.CHILDS))):
                if self.PARENT.CHILDS[oi] == self: self.PARENT.CHILDS.pop(oi)
        else: self = None

    def clone(self):
        if self.PARENT != None: self.PARENT.CHILDS.append(self)
        else:
            raise AttributeError(Errors[2])

    def clearChild(self, Child):
        for oj in range(len(list(self.CHILDS))):
            if self.CHILDS[oj] == Child:
                self.CHILDS.pop(oj); break
    
    def clearChildren(self, Children):
        for oj in range(len(list(self.CHILDS))):
            if self.CHILDS[oj] == Children: self.CHILDS.pop(oj)

    def clearAllChildren(self): self.CHILDS = []

    def replaceChild(self, Child, NewChild):
        for oj in range(len(list(self.CHILDS))):
            if self.CHILDS[oj] == Child: self.CHILDS[oj] = NewChild; self.CHILDS[oj].PARENT = self; break

    def replaceChildren(self, Children, NewObject):
        for oj in range(len(list(self.CHILDS))):
            if self.CHILDS[oj] == Children: self.CHILDS[oj] = NewObject; self.CHILDS[oj].PARENT = self

    # Find Objects
    # > Get Children
    def getChildren(self): return list(self.CHILDS)

    def getChildbyIndex(self, Index):
        try: return list(self.CHILDS)[Index]
        except IndexError: return None

    # > Find Child
    def findChild(self, ChildName):
        for o in list(self.CHILDS):
            if dump(o)[0] == ChildName: return o
        return None

    def findFirstChild(self, ChildClass):
        for o in list(self.CHILDS):
            if dump(o)[1] == ChildClass: return o
        return None

    def findSpecificChild(self, ChildName, ChildClass):
        for o in list(self.CHILDS):
            if dump(o)[0] == ChildName and dump(o)[1] == ChildClass: return o
        return None

    # > Find Children
    def findFirstChildren(self, ChildrenClass):
        op = []
        for o in list(self.CHILDS):
            if dump(o)[1] == ChildrenClass: op.append(o)
        return list(op)

    def findRelatedChildren(self, ChildrenName):
        op = []
        for o in list(self.CHILDS):
            if dump(o)[0] == ChildrenName: op.append(o)
        return list(op)

    def locateRelatedChildren(self, Name, Class):
        op = []
        for o in list(self.CHILDS):
            if dump(o)[0] == Name and dump(o)[1] == Class: op.append(o)
        return list(op)

    # > Wait for Child
    def waitForChild(self, ChildName):
        delay = 0
        while True:
            for o in list(self.CHILDS):
                if dump(o)[0] == ChildName: return o
            delay += 1
            if delay >= 1000:
                warnings.warn(Warnings[0])
            if delay >= 1500:
                raise RuntimeError(Errors[2])      

    def waitForFirstChild(self, ChildClass):
        delay = 0
        while True:
            for o in list(self.CHILDS):
                if dump(o)[1] == ChildClass: return o
            delay += 1
            if delay >= 1000:
                warnings.warn(Warnings[0])
            if delay >= 1500:
                raise RuntimeError(Errors[2])

    def waitForSpecificChild(self, ChildName, ChildClass):
        delay = 0
        while True:
            for o in list(self.CHILDS):
                if dump(o)[0] == ChildName and dump(o)[1] == ChildClass: return o
            delay += 1
            if delay >= 1000:
                warnings.warn(Warnings[0])
            if delay >= 1500:
                raise RuntimeError(Errors[2])

    # > Does Child Exists?
    def doesChildExist(self, ChildName):
        for o in list(self.CHILDS):
            if dump(o)[0] == ChildName: return True
        return False

    def doesFirstChildExist(self, ChildClass):
        for o in list(self.CHILDS):
            if dump(o)[1] == ChildClass: return True
        return False

    def doesSpecificChildExist(self, ChildName, ChildClass):
        for o in list(self.CHILDS):
            if dump(o)[0] == ChildName and dump(o)[1] == ChildClass: return True
        return False

    # > Find Pairs
    def findNamePairs(self, Object):
        for o in list(self.CHILDS):
            if dump(o)[0] == dump(Object)[0]: return o
        return None

    def findClassPairs(self, Object):
        for o in list(self.CHILDS):
            if dump(o)[1] == dump(Object)[1]: return o
        return None

    def findPairs(self, Object):
        for o in list(self.CHILDS):
            if dump(o)[0] == dump(Object)[0] and dump(o)[1] == dump(Object)[1]: return o
        return None

    # > Get Pairs
    def getNamePairs(self, Object):
        op = []
        for o in list(self.CHILDS):
            if dump(o)[0] == dump(Object)[0]: op.append(o)
        return list(op)

    def getClassPairs(self, Object):
        op = []
        for o in list(self.CHILDS):
            if dump(o)[1] == dump(Object)[1]: op.append(o)
        return list(op)

    def getPairs(self, Object):
        op = []
        for o in list(self.CHILDS):
            if dump(o)[0] == dump(Object)[0] and dump(o)[0] == dump(Object)[0]: op.append(o)
        return list(op)

    # Instance Variables
    def NEW(self, Name, Value):
        testBool = True
        for v in list(self.VARIABLES):
            if v[0] == Name: testBool = False; break
        if bool(testBool): self.VARIABLES.append([Name, Value])

    def GET(self, Name):
        for v in list(self.VARIABLES):
            if v[0] == Name: return v[1]
        return None

    def INDEX(self, Index): return self.VARIABLES[Index][0]

    def SET(self, Name, Value):
        for v in list(self.VARIABLES):
            if v[0] == Name: v[1] = Value

    def DEL(self, Name):
        for vi in range(len(list(self.VARIABLES))):
            if self.VARIABLES[vi][0] == Name: self.VARIABLES.pop(vi)
