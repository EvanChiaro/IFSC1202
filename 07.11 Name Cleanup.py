def ProperCase(s):
    a = s.casefold()
    a = s.capitalize()
    return a
def RemoveNewLine(s):
    b = s.replace('\n', '')
    return b
def Trim(s):
    c = s.strip()
    return c
def FirstNames(s):
    stop = s.find(' ')
    d = ProperCase(s[:stop])
    return d
def LastNames(s):
    start = s.rfind(' ')
    e = ProperCase(s[start+1:])
    return e
def MiddleNames(s):
    start = s.find(' ')+1
    stop = s.find(' ', s.find(' ')+1)
    if stop == -1:
        f = ''
    else:
        f = ProperCase(s[start:stop])
    return f
print('First'.ljust(10) + ' ' + 'Middle'.ljust(10) + ' ' + 'Last'.ljust(10))
print('----------'.ljust(10) + ' ' + '----------'.ljust(10) + ' ' + '----------'.ljust(10))
names = open("07.11 Names.txt")
s = names.readline()
while s != '':
    out = RemoveNewLine(Trim(s))
    print(FirstNames(out).ljust(10) + ' ' + MiddleNames(out).ljust(10) + ' ' + LastNames(out).ljust(10))
    s = names.readline()