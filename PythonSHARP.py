# Contrants
menuFunctionLow = "argument 'options' should contain at least 2 options to pick from as a list."
menuFunctionLowFalse = "argument 'options' should contain at least 2 options to pick from as a list. In order for one option, you must provide True to the third argument, 'noAnwser'."
menuFunctionGenral = "function 'menu()' encountered an error, please report this iusses."

# Oprations
def itemsMerge(var):
    num = 0
    for i in list(var):
        num += float(i)
    return num

def itemsMulty(var):
    num = 1
    for i in list(var):
        num *= float(i)
    return num

def itemCount(var, item):
    count = 0
    for i in list(var):
        if i is item: count += 1
    return int(count)
    
def rangeLimit(num, MIN, MAX):
    if int(num) > int(MAX): return int(MAX)
    elif int(num) < int(MIN): return int(MIN)
    else: return int(num)
        
def feturn(con, true, false):
    return true if bool(con) else false
    
def listInit(var, item):
    for j in range(len(list(var))):
        if list(var)[j] is item: return int(j)
    return None
    
def listInits(var, item):
    items = []
    for j in range(len(list(var))):
        if list(var)[j] is item: items.append(j)
    if items != []: return list(items)
    else: return None
        
def filterList(var, item):
    items = []
    for j in list(var):
        if not j is item: items.append(j)
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

class localment():
    def __init__(self): self.CONTENT = []

    def new(self, Name):
        for i in list(self.CONTENT):
            if str(list(i)[0]) is str(Name): break
        self.CONTENT.append([str(Name), None])

    def define(self, Name, Value):
        for i in list(self.CONTENT):
            if str(list(i)[0]) is str(Name): break
        self.CONTENT.append([str(Name), Value])

    def set(self, Name, New):
        for i in list(self.CONTENT):
            if str(list(i)[0]) is str(Name): i[1] = New

    def rename(self, Name, New):
        for i in list(self.CONTENT):
            if str(list(i)[0]) is str(Name): i[0] = str(New)

    def get(self, Name):
        for i in list(self.CONTENT):
            if str(list(i)[0]) is str(Name): return i[1]

    def find(self, Index):
        for i in range(len(self.CONTENT)):
            if int(i) == int(Index): return self.CONTENT[Index][0]
        return None

    def remove(self, Name):
        for i in range(len(self.CONTENT)):
            try:
                if str(Name) is str(self.CONTENT[i][0]):
                    self.CONTENT.pop(i)
            except IndexError:
                if str(Name) is str(self.CONTENT[0][0]):
                    self.CONTENT.pop(i)

    def items(self): return list(self.CONTENT)

# Objects
# object: [subject, class, children, props]
# prop: [name, value, default]

def prop(name, value): return [str(name), value, value]

def dump(Instance):
    try: return [Instance.SUB, Instance.CLASS, Instance.PROPS, Instance.CHILDS, Instance.PARENT]
    except: return [Instance[0].SUB, Instance[0].CLASS, Instance[0].PROPS, Instance[0].CHILDS, Instance[0].PARENT]

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
            if p[0] is str(Prop): return p
        return None
    
    def gitProp(self, Prop):
        for p in list(self.PROPS):
            try:
                if p[0] is str(Prop): return p[1]
            except: return p
        return None

    def sitProp(self, Prop, New):
        for p in list(self.PROPS):
            if p[0] is str(Prop):
                p[1] = New
                break

    def ritProp(self, Prop):
        for p in list(self.PROPS):
            if p[0] is str(Prop):
                p[1] = p[2]
                break

    def assignParentAs(self, NewParent): self.PARENT = NewParent

    def parent(self):
        if self.PARENT == None: return None
        else: return self.PARENT

    # Objects
    def newChild(self, Instance):
        Instance.PARENT = self
        self.CHILDS.append(Instance)

    def clearChild(self, Child):
        for oj in range(int(len(list(self.CHILDS)))):
            if self.CHILDS[oj] is Child:
                self.CHILDS.pop(oj)
                break
    
    def clearChildren(self, Children):
        for oj in range(int(len(list(self.CHILDS)))):
            if self.CHILDS[oj] is Children: self.CHILDS.pop(oj)

    def clearAllChildren(self): self.CHILDS = []

    def replaceChild(self, Child, NewChild):
        for oj in range(int(len(list(self.CHILDS)))):
            if self.CHILDS[oj] is Child:
                self.CHILDS[oj] = NewChild
                self.CHILDS[oj].PARENT = self
                break

    def replaceChildren(self, Children, NewObject):
        for oj in range(int(len(list(self.CHILDS)))):
            if self.CHILDS[oj] is Children:
                self.CHILDS[oj] = NewObject
                self.CHILDS[oj].PARENT = self

    # Find Objects
    def getChildren(self): return list(self.CHILDS)

    def findChild(self, ChildName):
        for o in list(self.CHILDS):
            if dump(o)[0] is str(ChildName): return o
        return None

    def findFirstChild(self, ChildClass):
        for o in list(self.CHILDS):
            if dump(o)[1] is str(ChildClass): return o
        return None

    def locateForChild(self, ChildName, ChildClass):
        for o in list(self.CHILDS):
            if dump(o)[0] is str(ChildName) and dump(o)[1] is str(ChildClass): return o
        return None

    def findFirstChildren(self, ChildrenClass):
        op = []
        for o in list(self.CHILDS):
            if dump(o)[1] is str(ChildrenClass): op.append(o)
        return list(op)

    def findRelatedChildren(self, ChildrenName):
        op = []
        for o in list(self.CHILDS):
            if dump(o)[0] is str(ChildrenName): op.append(o)
        return list(op)

    def locateRelatedChildren(self, Name, Class):
        op = []
        for o in list(self.CHILDS):
            if dump(o)[0] is str(Name) and dump(o)[1] is str(Class): op.append(o)
        return list(op)
