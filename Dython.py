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
        
# Local Variables
class local():
    def __init__(self): self.locals = []

    def add(self, name, start):
        b = True
        for i in list(self.locals):
            if list(i)[0] is str(name):
                b = False
                break
        if bool(b): self.locals.append([str(name), start])

    def set(self, name, value):
        for j in range(int(len(self.locals))):
            if list(self.locals[j])[0] is str(name): self.locals[int(j)] = [str(name), value]
            break

    def get(self, name):
        for i in list(self.locals):
            if list(i)[0] is str(name):
                return list(i)[1]
        return None

    def sup(self, name):
        for i in range(len(list(self.locals))):
            if list(self.locals[i])[0] is str(name):
                self.locals.pop(i)
                
        

# Console
def menu(caption, options, noAnwser):
    print('')
    if caption != "" and caption != None: print(str(caption))
    if int(len(options)) <= 1:
        print("error in a menu() function")
        exit
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
                    print("error in a menu() function")
                    exit
        if mest == "int" or mest == "float":
            if mest == "float": testAnwser = int(round(float(testAnwser)))
            optionAnswer = testAnwser
            if int(optionAnswer) >= 0 and int(optionAnswer) < int(len(options)): return int(optionAnswer)
        elif mest == "str":
            if bool(noAnwser) and str(optionAnwser) == "": return None

# Objects
# object: [subject, class, children, props]
# prop: [name, value, default]

def prop(name, value): return [str(name), value, value]

def dump(Instance):
    try: return [Instance.SUB, Instance.CLASS, Instance.PROPS, Instance.CHILDS]
    except: return [Instance[0].SUB, Instance[0].CLASS, Instance[0].PROPS, Instance[0].CHILDS]

class Instance():
    def __init__(self, Subject, Class, Props):
        self.SUB = str(Subject)
        self.CLASS = str(Class)
        self.PROPS = list(Props)
        self.CHILDS = []

    # Info
    def gitSub(self): return self.SUB
    def gitClass(self): return self.CLASS
    def gitProps(self): return self.PROPS

    def sitSub(self, New): self.SUB = str(New)
    def sitClass(self, New): self.CLASS = str(New)
    def sitProps(self, New): self.PROPS = str(New)

    def findProp(self, Prop):
        for p in list(self.PROPS):
            if p[0] is str(Prop): return p
        return None
    
    def gitProp(self, Prop):
        for p in list(self.PROPS):
            if p[0] is str(Prop): return p[1]
        return None

    def sitProp(self, Prop, New):
        for p in list(self.PROPS):
            if p[0] is str(Prop):
                p[1] = New
                break

        
    # Objects
    def newChild(self, Instance): self.CHILDS.append(Instance)

    def clearChild(self, Child):
        for oj in range(int(len(list(self.CHILDS)))):
            if self.CHILDS[oj] is Child:
                self.CHILDS.pop(oj)
            break

    def clearAllChildren(self): self.CHILDS = []

    def replaceChild(self, Child, NewChild):
        for oj in range(int(len(list(self.CHILDS)))):
            if self.CHILDS[oj] is Child:
                self.CHILDS[oj] = NewChild
                break

    # Find Objects
    def children(self): return list(self.CHILDS)

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
            if dump(o)[1] is str(ChildClass): op.append(o)
        return list(op)
