import urllib.request, urllib.parse, urllib.error
#텍스트 파일 읽기
fhand=urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand:
    print(line.decode().strip())
print('\n\n')
#딕셔너리 사용
import urllib.request, urllib.parse, urllib.error
fhand=urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
counts=dict()
for line in fhand:
    words=line.decode().split()
    for word in words:
        counts[word]=counts.get(word,0)+1
print(counts)
print('\n\n')
#웹페이지 읽기
import urllib.request, urllib.parse, urllib.error
fhand=urllib.request.urlopen('http://www.dr-chuck.com/page1.htm')
for line in fhand:
    print(line.decode().strip())
