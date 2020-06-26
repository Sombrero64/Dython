# Dython Moclude

# Oprations
class math():
    def expon(num, root):
        ji = float(num)
        for j in range(root - 1):
            ji = float(float(ji) * float(num))
        return ji
    def itemsAdd(var):
        num = 0
        for i in list(var):
            num += float(i)
        return num
    def itemsSub(var):
        num = float(list(var)[0] * 2)
        for i in list(var):
            num -= float(i)
        return num
    def itemsMulti(var):
        num = 1
        for i in list(var):
            num = float(float(num) * float(i))
        return num
    def itemsDivd(var):
        num = float(list(var)[0])
        for i in range(int(len(list(var))) - 1):
            num = float(float(num) / float(var[i + 1]))
        return num
    def joinStrs(strings):
        string = ""
        for i in list(strings):
            string += str(i)
        return str(string)
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
        if bool(con): return true
        else: return false
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
        
# Temp Variables
temps = []
# [ [name, value] ]

class temp():
    def define(name, start):
        b = True
        for i in list(temps):
            if list(i)[0] is str(name):
                b = False
                break
        if bool(b): temps.append([str(name), start])
    def get(name):
        for i in list(temps):
            if list(i)[0] is str(name):
                return list(i)[1]
        return None
    def set(name, value):
        count = 0
        for i in list(temps):
            if list(i)[0] is str(name):
                temps[int(count)] = [str(name), value]
            count += 1
    def remove(name):
        for i in range(int(len(temps))):
            j = list(temps)[i]
            if list(j)[0] is str(name): temps.pop(i)

# Console
class console():
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
