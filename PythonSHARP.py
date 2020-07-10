# PYTHON #
# Version 3.8.1

# Contrants
menuFunctionLow = "argument 'options' should contain at least 2 options to pick from as a list."
menuFunctionLowFalse = "argument 'options' should contain at least 2 options to pick from as a list. In order for one option, you must provide True to the third argument, 'noAnwser'."
menuFunctionGenral = "function 'menu()' encountered an error, please report this iusses."
waitForChildDelay = "possible infinite wait for child with function 'waitForChild()'"
waitForFirstChildDelay = "possible infinite wait for child with function 'waitForFirstChild()'"
waitForSpecificChildDelay = "possible infinite wait for child with function 'waitForSpecificChild()'"
newChildNil = "new instance on 'newChild()' isn't object"
LOCALchangeType = "local varible must match the changer's type"
recordNone = "must be an Instance() or Localment() object."
recordGenral = "function 'record()' encountered an error, please report this iusses."

# Guide
def info():
    print('████ █ █ ███ █ █ ███ █  █ #')
    print('█  █  █   █  █ █ █ █ ██ █')
    print('████  █   █  ███ █ █ █ ██')
    print('█    █    █  █ █ █ █ █  █')
    print('█   █     █  █ █ ███ █  █')
    print('''Version 3.8.1''')
    print('')
    print('''Python# (PythonSharp) is a free open source module for Python 3.8.3.''')
    print('''Python# allows the branching, convenient creation of objects with propterties.''')
    print('''It also have local variables (stores clearable varaibles) and useful functions.''')
    print('')
    print('''Created by Daniel Lawson: Copyright (©) 2020 Daniel Lawson.''')
    print('''Python# uses the MIT license (mit).''')
    print('')
    print('CREDITS')
    print('▔▔▔▔▔▔▔▔▔')
    print('Daniel Lawson')
    print(''' Python# Creator''')
    print('18001767679')
    print(''' Contributing to Python#''')
    print('''Dan's Papa (Grandfather)''')
    

# Oprations
def itemsAddty(var):
    num = 0
    for i in list(var):
        num += float(i)
    return num

def itemsSubty(var):
    num = list(var)[0] * 2
    for i in list(var):
        num -= float(i)
    return num

def itemsMulty(var):
    num = 1
    for i in list(var):
        num *= float(i)
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
    
def rangeLimit(num, MIN, MAX):
    if int(num) > int(MAX): return int(MAX)
    elif int(num) < int(MIN): return int(MIN)
    else: return int(num)
        
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

def menu(caption, options, noAnwser):
    if caption != "" and caption != None: print(str(caption))
    if int(len(options)) == 0:
        raise ValueError(menuFunctionLow)
    elif int(len(options)) == 1 and not bool(noAnwser):
        raise ValueError(menuFunctionLowFalse)
    for optionCount in range(len(options)):
        print(str(optionCount) + ": " + str(options[optionCount]))
    while True:
        optionAnwser = input("└> ")
        try:
            testAnwser = int(optionAnwser)
            mest = "int"
        except ValueError:
            try:
                testAnwser = float(optionAnwser)
                mest = "float"
            except ValueError:
                try:
                    testAnwser = str(optionAnwser)
                    mest = "str"
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
            if str(list(i)[0]) == str(Name):
                testBool = False
                break
        if bool(testBool): self.CONTENT.append([str(Name), None])

    def define(self, Name, Value):
        testBool = True
        for i in list(self.CONTENT):
            if str(list(i)[0]) == str(Name):
                testBool = False
                break
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
                if str(Name) == str(self.CONTENT[i][0]):
                    self.CONTENT.pop(i)
            except IndexError:
                if str(Name) == str(self.CONTENT[0][0]):
                    self.CONTENT.pop(i)

    def variables(self): return list(self.CONTENT)

# Objects
# object: [subject, class, children, props]
# prop: [name, value, default]

def intType(OBJ):
    try:
        a = OBJ.SUB
        b = OBJ.CLASS
        c = OBJ.PROPS
        d = OBJ.CHILDS
        e = OBJ.PARENT
        return 'instance'
    except:
        try:
            g = OBJ.CONTENT
            return 'house'
        except:
            if OBJ == None: return None
            else: return 'other'

def prop(name, value): return [str(name), value, value]

def dump(Instance):
    try: return [Instance.SUB, Instance.CLASS, Instance.PROPS, Instance.CHILDS, Instance.PARENT]
    except: return [Instance[0].SUB, Instance[0].CLASS, Instance[0].PROPS, Instance[0].CHILDS, Instance[0].PARENT]

def record(Instance):
    archive = None
    if intType(Instance) == 'instance':
        contents = dump(Instance)
        print('SUBJECT: ' + contents[0])
        print('CLASS: ' + contents[1])
        if contents[4] == None: print('PARENT: None')
        else: print('PARENT: ' + dump(contents[4])[0])
    elif intType(Instance) == 'house':
        contents = list(Instance.CONTENT)
        for vm in list(contents):
            print('local variable:', vm[0], '=', vm[1])
    elif intType(Instance) == 'other':
        raise ValueError(recordNone)
    else:
        raise RuntimeError(recordGenral)

class Instance():
    def __init__(self, Subject, Class, Props):
        self.SUB = str(Subject)
        self.CLASS = str(Class)
        self.PROPS = list(Props)
        self.CHILDS = []
        self.PARENT = None

    # Info
    def gitSub(self):
        if self == None: return None
        else: return self.SUB
    def gitClass(self):
        if self == None: return None
        else: return self.CLASS
    def gitProps(self):
        if self == None: return None
        else: return self.PROPS

    def sitSub(self, New): self.SUB = str(New)
    def sitClass(self, New): self.CLASS = str(New)
    def sitProps(self, New): self.PROPS = str(New)

    def findProp(self, Prop):
        for p in list(self.PROPS):
            if p[0] == str(Prop): return p
        return None
    
    def gitProp(self, Prop):
        for p in list(self.PROPS):
            try:
                if p[0] == str(Prop): return p[1]
            except: return p
        return None

    def sitProp(self, Prop, New):
        for p in list(self.PROPS):
            if p[0] == str(Prop):
                p[1] = New
                break

    def ritProp(self, Prop):
        for p in list(self.PROPS):
            if p[0] == str(Prop):
                p[1] = p[2]
                break

    def assignParentAs(self, NewParent): self.PARENT = NewParent

    def parent(self):
        if self.PARENT == None: return None
        else: return self.PARENT

    # Objects
    def newChild(self, Instance):
        if Instance == None:
            raise ValueError(newChildNil)
        else:
            Instance.PARENT = self
            self.CHILDS.append(Instance)

    def clearChild(self, Child):
        for oj in range(int(len(list(self.CHILDS)))):
            if self.CHILDS[oj] == Child:
                self.CHILDS.pop(oj)
                break
    
    def clearChildren(self, Children):
        for oj in range(int(len(list(self.CHILDS)))):
            if self.CHILDS[oj] == Children: self.CHILDS.pop(oj)

    def clearAllChildren(self): self.CHILDS = []

    def replaceChild(self, Child, NewChild):
        for oj in range(int(len(list(self.CHILDS)))):
            if self.CHILDS[oj] == Child:
                self.CHILDS[oj] = NewChild
                self.CHILDS[oj].PARENT = self
                break

    def replaceChildren(self, Children, NewObject):
        for oj in range(int(len(list(self.CHILDS)))):
            if self.CHILDS[oj] == Children:
                self.CHILDS[oj] = NewObject
                self.CHILDS[oj].PARENT = self

    # Find Objects
    # > Get Children
    def getChildren(self): return list(self.CHILDS)

    def getChildbyIndex(self, Index):
        try: return list(self.CHILDS)[int(Index)]
        except ValueError: return list(self.CHILDS)[int(round(float(Index)))]
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

    def locateForChild(self, ChildName, ChildClass):
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
