import re

#p = re.compile('ab*')
#Result = p.match('abbbb')
#print(Result)

#p2 = re.match('ab*', 'abbbb')
#print(p2)

#pattern = re.compile("d")
#result = pattern.search("dog")
#result = pattern.search("dog", 1)
#print(result)

#p3 = re.search("\\\\", "C:\\test")
#p4 = re.search(r"\\", "C:\\test")
#print(p3)
#print(p4)

#str = '''Sample1.
#Sample2.
#Sample3.'''

#p5 = re.compile('^.*', re.S)
#result2 = p5.search(str);
#print(result2.group())

pattern3 = re.compile("o[gh]")
result2 = pattern3.fullmatch("dog")
print(result2)
result2 = pattern3.fullmatch("ogre")
print(result2)
result2 = pattern3.fullmatch("doggie",1,3)
print(result2)

#pattern = re.compile("\W+")
#result = pattern.split('words, words, words.')
#result = pattern.split('words, words, words.', 1)
#print(result)

#pattern2 = re.compile("x*")
#result2 = pattern.split('axbc')
#print(result2)

#result = re.sub(r'\W','','a:b:c, d.')
#print(result)

#pattern = re.compile("o")
#result = pattern.search("dog")
#result.group()
#print(result.group())

str = '<a href="index.html">HERE</a><font size="10">'
result = re.search(r'href="(.*?)">', str)
print(result)
print(result.group(1))

#주민등록번호 패턴이 맞는지 확인하고 앞부분 뒷부분 따로 출력
result = re.match("(\d{6})-(\d{7})", '123456-1234567')
print(result)
print(result.group(1))
print(result.group(2))
result2 = re.match("(\d{6})-(\d{7})", '1234556-12354567')
print(result2)
