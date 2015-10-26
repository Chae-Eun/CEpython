import re
import os
import glob
import urllib.request

str = '''Window
Unix
Linux
Solaris'''
p = re.compile('^.+', re.M)
print(p.findall(str))

p = re.compile('^.+', re.S)
#p = re.compile('^.+', re.M)
result = p.search(str)
print(result)

#띄어쓰기 안하면 왜 Malcolm, m이 나올까? 왜 m이 나오지?!
m = re.match(r"(?P<first_name>\w+) (?P<last_name>\w+)","Malcolm Reynolds")
print(m.group('first_name', 'last_name'))
print(m.groups())
print(m.group('last_name'))

#어려우..
m = re.match(r"(\d+)\.?(\d+)?", "24")
print(m.groups())
print(m.groups(0))

m = re.match(r"(?P<first_name>\w+) (?P<last_name>\w+)", "Malcolm Reynolds")
print(m.groupdict())

p = re.compile(".+:")
m = p.search("http://google.com")
print(m.group())

p = re.compile(".+(?=:)")
m = p.search("http://google.com")
print(m.group())

p = re.compile('.*[.](?!bat$|exe$).*$')
os.chdir('C:\\')
print(os.getcwd())
list = glob.glob('.*[.](?!bat$|exe$).*$')
print(list)
#for i in list :
#    m = p.match(i)
#    print(m.groups())

p = re.compile("(?<=abc)def")
m = p.search("abcdef")
print(m.group())

m = re.search('(?<=-)\w+', 'spam-egg')
print(m.group())

email = "tony@tiremove_thisger.net"
m = re.search("remove_this", email)
result = email[:m.start()] + email[m.end():]
result1 = email[:m.start()]
result2 = email[m.end():]
result3 = email[:m.end()]
print(result)
print(result1)
print(result2)
print(result3)

def displaymatch(match):
    if match is None:
        return None
    return '<Match: %r, groups=%r>' % (match.group(), match.groups())

valid = re.compile(r"^[a2-9tjqk]{5}$")
print(displaymatch(valid.match("akt5q")))
print(displaymatch(valid.match("akt5e")))
print(displaymatch(valid.match("akt")))
print(displaymatch(valid.match("727ak")))

text = """Ross: McFluff: 834.345.1254: 155 Elm Street
Ronald: Heathmore: 892.345.3428 436: Finley Avenue
Frank: Burger: 925.541.7625 662: South Dogwood Way
Heather: Albrecht: 548.326.4584 919: Park Place"""

entries = re.split("\n", text)
result = [re.split(":?", entry, 4) for entry in entries]
print(result)

#title 안에 값 찾기
with urllib.request.urlopen('http://www.naver.com/') as f:
    #print(f.read())
    str = f.read()
    m = re.search(r'<title>"(.*)"</title>', str)
    #print(f.read(300))
    #print(f.read(300).decode("utf-8"))