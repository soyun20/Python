asd=-1
qwe=10
ghj=[50,13,54,82,16,40,3,51,54,58,65,95,751,20,32,4,2]
for zxc in ghj:
#qwe에 가장 작은값을 저장하고싶다.
    if zxc < qwe: #zxc가 더 작어?
        qwe = zxc #더 작은값 저장
        print("qwe",zxc)
#asd에 큰 값을 저장하고 싶다
    if zxc > asd: #zxc가 더 커?
        asd = zxc # 더 큰값 저장
        print("asd",asd)
llll=qwe+asd
print("sum",llll)
