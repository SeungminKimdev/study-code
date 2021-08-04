import tkinter as tk

win = tk.Tk()
win.title('계산기')

def number_click(value):
    print(value)
def operator_click(value):
    print(value)
#버튼 클릭
def button_click(value):
    print(value)
    try:
        value = int(value)
        number_click(value)
    except:
        operator_click(value)


disValue = 0
str_value = tk.StringVar()
str_value.set(str(disValue))
dis = tk.Entry(win, textvariable=str_value, justify='right', bg = 'white',fg = 'red')
#justify=글자 위치, columnspan = 몇개를 차지 할 것이냐
dis.grid(column = 0, row = 0, columnspan = 4, ipadx=80, ipady=30)

calItem = [['1','2','3','4'],
            ['5','6','7','8'],
            ['9','0','+','-'],
            ['/','*','C','=']]

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


win.mainloop()