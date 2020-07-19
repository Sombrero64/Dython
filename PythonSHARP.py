# PYTHON #
# Version 3.10.2

# Contrants
menuFunctionLow = "must be at least 2 items"
menuFunctionGenral = "function 'menu()' error"
waitForChildDelay = "possible infinite wait for child"
newChildNil = "new instance isn't required object"
LOCALchangeType = "local varible must match the changer's type"
itemsAddtyNon = "try using the itemsMerge() function instead of itemsAddty()"
itemsAddtyGenral = "function 'itemsAddty()' error"
itemsSubtyNon = "try using the itemsDerge() function instead of itemsSubty()"
itemsSubtyGenral = "function 'itemsSubty()' error"
cloneMaster = "cannot clone a master instance"

# Guide
def info():
    print('████ █ █ ███ █ █ ███ █  █ #')
    print('█  █  █   █  █ █ █ █ ██ █')
    print('████  █   █  ███ █ █ █ ██')
    print('█    █    █  █ █ █ █ █  █')
    print('█   █     █  █ █ ███ █  █')
    print('''Version 3.9.2''')
    print('')
    print('''Python# (PythonSharp) is a free open source module for Python 3.8.3.''')
    print('''Python# allows the branching, convenient creation of objects with propterties.''')
    print('''It also have local variables (stores clearable varaibles) and useful functions.''')
    print('')
    print('''Created by Daniel; copyright (©) 2020 Daniel Lawson.''')
    print('github.com/Sombrero64')
    print('sites.google.com/view/unclejimbo')
    print('')
    print('''Python# uses the MIT license (mit).''')
    print('')
    print('CREDITS')
    print('▔▔▔▔▔▔▔▔▔')
    print('18001767679')
    print("Dan's Papa (Grandfather)")
    

# Oprations
def itemsAddty(var):
    num = 0
    try:
        for i in list(var): num += float(i)
        return float(num)
    except ValueError:
        raise ValueError(itemsAddtyNon)
    except:
        raise RuntimeError(itemsAddtyGenral)

def itemsMerge(var):
    value = ''
    for i in list(var): value += str(i)
    return str(value)

def itemsSubty(var):
    num = list(var)[0] * 2
    try:
        for i in list(var): num -= float(i)
        return float(num)
    except ValueError:
        raise ValueError(itemsSubtyNon)
    except:
        raise RuntimeError(itemsSubtyGenral)

def itemsMulty(var):
    num = 1
    for i in list(var): num *= float(i)
    return num

def itemsDidty(var):
    num = list(var)[0]
    passer = False
    for i in list(var):
        if bool(passer):
            if float(i) == 0:
                raise ZeroDivisionError('division by zero')
            else: num /= float(i)
        else: passer = True
    return num

def itemCount(var, item):
    count = 0
    for i in list(var):
        if i == item: count += 1
    return int(count)
    
def rangeLimit(num, Min, Max):
    NUM = float(num); MIN = float(Min); MAX = float(Max)
    if NUM > MAX: return MAX
    elif NUM < MIN: return MIN
    else: return NUM
        
def feturn(con, true, false):
    return true if bool(con) else false
    
def listInit(var, item):
    for j in range(len(list(var))):
        if list(var)[j] == item: return int(j)
    return None
    
def listInits(var, item):
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

def indexList(var, indexes):
    items = []
    for IN in list(indexes): items.append(list(var)[int(IN)])
    return list(items)

def findGreatest(var):
    number = float(list(var)[0])
    for i in list(var):
        if float(i) > number: number = i
    return number

def findGreatestIndex(var):
    number = float(list(var)[0])
    index = 0
    for i in range(len(list(var))):
        if float(list(var)[i]) > number:
            number = var[i]
            index = i
    return index

def findSmallest(var):
    number = float(list(var)[0])
    for i in list(var):
        if float(i) < number: number = i
    return number

def findSmallestIndex(var):
    number = float(list(var)[0])
    index = 0
    for i in range(len(list(var))):
        if float(list(var)[i]) < number:
            number = var[i]
            index = i
    return index

def reverse(value): return float(value - value * 2)

def genNumList(nin, nax):
    C = float(nin)
    List = []

    while True:
        if not C > float(nax): List.append(float(C))
        else: break
        C += 1;
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
    for s in list(['true', 'yes', 'correct', 'on', '1']):
        if str(value) == s: return True
    for s in list(['false', 'no', 'incorrect', 'off', '0']):
        if str(value) == s: return False
    for s in list(['none', 'nothing', 'nil', 'null', '']):
        if str(value) == s: return None
    return str(value)

def menu(options, noAnwser):
    if int(len(options)) == 0 or (int(len(options)) == 1 and not bool(noAnwser)):
        raise ValueError(menuFunctionLow)
    for optionCount in range(len(options)): print(str(optionCount) + ": " + str(options[optionCount]))
    while True:
        optionAnwser = input("└> ")
        try: testAnwser = int(optionAnwser); mest = "int"
        except ValueError:
            try: testAnwser = float(optionAnwser); mest = "float"
            except ValueError:
                try: testAnwser = str(optionAnwser); mest = "str"
                except:
                    raise RuntimeError(menuFunctionGenral)
        if mest == "int" or mest == "float":
            if mest == "float": testAnwser = int(round(float(testAnwser)))
            optionAnswer = testAnwser
            if int(optionAnswer) >= 0 and int(optionAnswer) < int(len(options)): return int(optionAnswer)
        elif mest == "str":
            if bool(noAnwser) and str(optionAnwser) == "": return None
        
# Local Variables

class Localment():
    def __init__(self): self.CONTENT = []

    def new(self, Name):
        testBool = True
        for i in list(self.CONTENT):
            if str(list(i)[0]) == str(Name): testBool = False; break
        if bool(testBool): self.CONTENT.append([str(Name), None])

    def define(self, Name, Value):
        testBool = True
        for i in list(self.CONTENT):
            if str(list(i)[0]) == str(Name): testBool = False; break
        if bool(testBool): self.CONTENT.append([str(Name), Value])

    def set(self, Name, New):
        for i in list(self.CONTENT):
            if str(list(i)[0]) == str(Name): i[1] = New

    def change(self, Name, Change):
        for i in list(self.CONTENT):
            try:
                if str(list(i)[0]) == str(Name): i[1] += Change
            except TypeError:
                raise TypeError(LOCALchangeType)

    def bange(self, Name, Change):
        for i in list(self.CONTENT):
            try:
                if str(list(i)[0]) == str(Name): i[1] -= Change
            except TypeError:
                raise TypeError(LOCALchangeType)

    def rename(self, Name, New):
        for i in list(self.CONTENT):
            if str(list(i)[0]) == str(Name): i[0] = str(New)

    def get(self, Name):
        for i in list(self.CONTENT):
            if str(list(i)[0]) == str(Name): return i[1]

    def find(self, Index):
        for i in range(len(self.CONTENT)):
            if int(i) == int(Index): return self.CONTENT[Index][0]
        return None

    def remove(self, Name):
        for i in range(len(self.CONTENT)):
            try:
                if str(Name) == str(self.CONTENT[i][0]): self.CONTENT.pop(i)
            except IndexError:
                if str(Name) == str(self.CONTENT[0][0]): self.CONTENT.pop(i)

    def wipe(self): self.CONTENT = []

    def variables(self): return list(self.CONTENT)

# Objects
# object: [subject, class, children, props]
# prop: [name, value, default, category]
# variable: [name, value]

def dump(Instance):
    try: return [
        Instance.SUB,
        Instance.CLASS,
        Instance.PROPS,
        Instance.CHILDS,
        Instance.PARENT,
        Instance.VARIABLES
        ]
    except: return [
        Instance[0].SUB,
        Instance[0].CLASS,
        Instance[0].PROPS,
        Instance[0].CHILDS,
        Instance[0].PARENT,
        Instance[0].VARIABLES
        ]

def rip(Inst):
    ripper = Instance(Inst.SUB, Inst.CLASS, Inst.PROPS)
    ripper.CHILDS = list(Inst.CHILDS)
    ripper.PARENT = Inst.PARENT
    ripper.VARIABLES = list(Inst.VARIABLES)
    return ripper

class Instance():
    def __init__(self, Subject, Class, Props):
        self.SUB = str(Subject)
        self.CLASS = str(Class)
        self.PROPS = list(Props)
        self.CHILDS = []
        self.PARENT = None
        self.VARIABLES = []

    # Info
    def Sub(self): return self.SUB
    def Class(self): return self.CLASS
    def Props(self): return self.PROPS

    def sitSub(self, New): self.SUB = str(New)
    def sitClass(self, New): self.CLASS = str(New)
    def sitProps(self, New): self.PROPS = list(New)

    def findProp(self, Prop):
        for p in list(self.PROPS):
            if p[0] == str(Prop): return p
        return None
    
    def gitProp(self, Prop):
        for p in list(self.PROPS):
            if p[0] == str(Prop): return p[1]
        return None

    def sitProp(self, Prop, New):
        for p in list(self.PROPS):
            if p[0] == str(Prop): p[1] = New; break

    def ritProp(self, Prop):
        for p in list(self.PROPS):
            if p[0] == str(Prop): p[1] = p[2]; break

    def assignParentAs(self, NewParent): self.PARENT = NewParent

    def parent(self):
        if self.PARENT == None: return None
        else: return self.PARENT

    # Objects
    def newChild(self, Instance):
        if Instance == None:
            raise ValueError(newChildNil)
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
            raise AttributeError(cloneMaster)

    def clearChild(self, Child):
        for oj in range(int(len(list(self.CHILDS)))):
            if self.CHILDS[oj] == Child:
                self.CHILDS.pop(oj); break
    
    def clearChildren(self, Children):
        for oj in range(int(len(list(self.CHILDS)))):
            if self.CHILDS[oj] == Children: self.CHILDS.pop(oj)

    def clearAllChildren(self): self.CHILDS = []

    def replaceChild(self, Child, NewChild):
        for oj in range(int(len(list(self.CHILDS)))):
            if self.CHILDS[oj] == Child: self.CHILDS[oj] = NewChild; self.CHILDS[oj].PARENT = self; break

    def replaceChildren(self, Children, NewObject):
        for oj in range(int(len(list(self.CHILDS)))):
            if self.CHILDS[oj] == Children: self.CHILDS[oj] = NewObject; self.CHILDS[oj].PARENT = self

    # Find Objects
    # > Get Children
    def getChildren(self): return list(self.CHILDS)

    def getChildbyIndex(self, Index):
        try: return list(self.CHILDS)[int(Index)]
        except IndexError: return None

    # > Find Child
    def findChild(self, ChildName):
        for o in list(self.CHILDS):
            if dump(o)[0] == str(ChildName): return o
        return None

    def findFirstChild(self, ChildClass):
        for o in list(self.CHILDS):
            if dump(o)[1] == str(ChildClass): return o
        return None

    def findSpecificChild(self, ChildName, ChildClass):
        for o in list(self.CHILDS):
            if dump(o)[0] == str(ChildName) and dump(o)[1] == str(ChildClass): return o
        return None

    # > Find Children
    def findFirstChildren(self, ChildrenClass):
        op = []
        for o in list(self.CHILDS):
            if dump(o)[1] == str(ChildrenClass): op.append(o)
        return list(op)

    def findRelatedChildren(self, ChildrenName):
        op = []
        for o in list(self.CHILDS):
            if dump(o)[0] == str(ChildrenName): op.append(o)
        return list(op)

    def locateRelatedChildren(self, Name, Class):
        op = []
        for o in list(self.CHILDS):
            if dump(o)[0] == str(Name) and dump(o)[1] == str(Class): op.append(o)
        return list(op)

    # > Wait for Child
    def waitForChild(self, ChildName):
        delay = 0
        while True:
            for o in list(self.CHILDS):
                if dump(o)[0] == str(ChildName): return o
            delay += 1
            if delay >= 1500:
                raise RuntimeError(waitForChildDelay)      

    def waitForFirstChild(self, ChildClass):
        delay = 0
        while True:
            for o in list(self.CHILDS):
                if dump(o)[1] == str(ChildClass): return o
            delay += 1
            if delay >= 1500:
                raise RuntimeError(waitForFirstChildDelay)

    def waitForSpecificChild(self, ChildName, ChildClass):
        delay = 0
        while True:
            for o in list(self.CHILDS):
                if dump(o)[0] == str(ChildName) and dump(o)[1] == str(ChildClass): return o
            delay += 1
            if delay >= 1500:
                raise RuntimeError(waitForSpecificChildDelay)

    # > Does Child Exists?
    def doesChildExist(self, ChildName):
        for o in list(self.CHILDS):
            if dump(o)[0] == str(ChildName): return True
        return False

    def doesFirstChildExist(self, ChildClass):
        for o in list(self.CHILDS):
            if dump(o)[1] == str(ChildClass): return True
        return False

    def doesSpecificChildExist(self, ChildName, ChildClass):
        for o in list(self.CHILDS):
            if dump(o)[0] == str(ChildName) and dump(o)[1] == str(ChildClass): return True
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
            if list(v)[0] == str(Name): testBool = False; break
        if bool(testBool): self.VARIABLES.append([str(Name), Value])

    def GET(self, Name):
        for v in list(self.VARIABLES):
            if list(v)[0] == str(Name): return list(v)[1]
        return None

    def INDEX(self, Index): return list(list(self.VARIABLES)[int(Index)])[0]

    def SET(self, Name, Value):
        for v in list(self.VARIABLES):
            if list(v)[0] == str(Name): v[1] = Value

    def DEL(self, Name):
        for vi in range(len(list(self.VARIABLES))):
            if list(self.VARIABLES[vi])[0] == str(Name): self.VARIABLES.pop(vi)
