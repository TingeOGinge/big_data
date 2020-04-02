import re

str1 = '3.14159,425,-dalin,Big2.3Data,small5data.64132.432 !dsad?2020.ab 123.456.789.0'
reS1 = '\d+\.\d+'
pattern1 = re.compile(reS1)
reMatch1 = pattern1.findall(str1)
print(reMatch1)

str2 = '<a href="/study/courses/bsc-hons-business-information-systems" \
data-gtm-vis-has-fired-9152982_32="1">Business Information Systems BSc (Hons)</a>'
reS2 = '<a href=.*>(.*?)</a>'
pattern2 = re.compile(reS2)
reMatch2 = pattern2.findall(str2)
print(reMatch2)

str31 = '123! dalin ?zhoudalin 111dalin222'
str32 = 'dalin123! dalin ?zhoudalin 111dalin222'
str33 = '123! dalin ?zhoudalin 111dalin222dalin'
#compare ^ and $
reS31 = '^dalin'
reS32 = 'dalin$'
pattern31 = re.compile(reS31)
pattern32 = re.compile(reS32)
reMatch31 = pattern31.findall(str31)
reMatch32 = pattern32.findall(str31)
print(reMatch31)
print(reMatch32)
reMatch33 = pattern31.findall(str32)
reMatch34 = pattern32.findall(str32)
print(reMatch33)
print(reMatch34)
reMatch35 = pattern31.findall(str33)
reMatch36 = pattern32.findall(str33)
print(reMatch35)
print(reMatch36)

#str4 = 
#compare .* and .*?
str4 = 'ddnaaddndnlinnn'
reS41 = 'd.*n'
reS42 = 'd.*?n'
pattern41 = re.compile(reS41)
reMatch41 = pattern41.findall(str4)
print(reMatch41)
pattern42 = re.compile(reS42)
reMatch42 = pattern42.findall(str4)
print(reMatch42)

#str5 = 
#use of {}
str5 = 'abcddd aabbccddd 12313 222 223344 dalin dalindalin !?'
reS51 = '\d{2}'
reS52 = 'dalin{2}'
reS53 = 'a{1,3}'
pattern51 = re.compile(reS51)
reMatch51 = pattern51.findall(str5)
print(reMatch51)
pattern52 = re.compile(reS52)
reMatch52 = pattern52.findall(str5)
print(reMatch52)
pattern53 = re.compile(reS53)
reMatch53 = pattern53.findall(str5)
print(reMatch53)