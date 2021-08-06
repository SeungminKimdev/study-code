import urllib.request
import re
import unicodedata
import tkinter as tk

disValue = 0
operator = {'C':1,'=':2}
musicName = '노래 제목'

def number_click(value):
    global disValue
    disValue = (disValue*10)+value
    str_value.set(disValue)

def clear():
    global disValue, musicName
    disValue = 0
    musicName = '노래 제목'
    str_value.set(disValue)
    mus_value.set(musicName)

#버튼 클릭
def button_click(value):
    #print(value)
    try:
        value = int(value)
        number_click(value)
    except:
        operator_click(value)

#노래 찾기
def search_music():
    global musicName
    url = "http://www.melon.com/chart/index.htm"
    user_agent = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'
    request = urllib.request.Request(url, None, {'User-Agent':user_agent})
    data = urllib.request.urlopen(request).read().decode('utf-8')
    str1 = ' 곡 선'
    num = 1
    serchName = ''
    for iterate in re.finditer('<td><div class="wrap t_right"><input type="checkbox" title="',data):
        a = iterate.end()
        b = ''
        i = 0
        while data[a+i] != '택':
            b = b+data[a+i]
            i += 1
        if num == disValue:
            serchName = b.replace(' 곡 선','')
            break
        num += 1
    musicName = serchName
    mus_value.set(musicName)

#문자가 들어왔을 때(명령문)
def operator_click(value):
    global disValue,operator, musicName
    op = operator[value]
    if op == 1:
        clear()
    elif disValue > 100:
        mus_value.set('Error: 100 초과!!')
        disValue = 0
    elif op == 2:
        search_music()
        str_value.set(str(disValue))
        disValue = 0
    else:
        clear()

win = tk.Tk()
win.title('Music Search')
win.resizable(False, False) #창 크기 조절 불가 (상하, 좌우)

#순위 숫자 표시
str_value = tk.StringVar()
str_value.set(str(disValue))
dis = tk.Entry(win, width = 10, textvariable=str_value, justify='center', bg = 'white',fg = 'red')
#justify=글자 위치, columnspan = 몇개를 차지 할 것이냐
dis.grid(column = 0, row = 0, columnspan = 1, ipadx=0, ipady=15)

#노래 제목 표시
mus_value = tk.StringVar()
mus_value.set(musicName)
disM = tk.Entry(win, width = 30, textvariable=mus_value, justify='center', bg = 'white', fg = 'blue')
disM.grid(column = 1, row = 0, columnspan = 3, ipadx=0, ipady=15)

calItem = [['1','2','3','4'],
            ['5','6','7','8'],
            ['9','0','C','=']]

#버튼 값과 버튼 위치 설정
for i,items in enumerate(calItem):
    for k,item in enumerate(items):
        #버튼 색깔 설정
        try:
            color = int(item)
            color = 'gray'
        except:
            color = 'yellow'
        bt = tk.Button(win, 
        text=item, 
        width = 10, 
        height = 5,
        bg = color,
        fg = 'black',
        command = lambda cmd = item: button_click(cmd)
        )
        bt.grid(column = k, row = i+1)

win.mainloop() #윈도우 종료될때까지 실행