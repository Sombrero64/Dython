# Oprations
def itemsMerge(var):
    num = None
    for i in list(var):
        num += float(i)
    return num

def itemsMulty(var):
    num = 1
    for i in list(var):
        num *= float(i)
    return num
    
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
