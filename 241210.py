from tkinter import *
#버튼 클릭 이벤트 함수
def button_click(value):
    """
    숫자 또는 연산자를 입력창에 추가하는 함수.
    :param value: 버튼 클릭 시의 값 (문자열)
    """
    current = ent.get() #현재 입력창의 값을 가져오기
    ent.delete(0, END) #입력창 초기화
    ent.insert(0, current + value) #기존 값에 클릭한 값을 추가하여 입력창에 다시 삽입

#= 버튼 클릭 시 계산 수행  입력창의 수식(eval을사용) 결과를 계산하는 함수
def cal():
    try:
        result = eval(ent.get())
        ent.delete(0, END)
        ent.insert(0, str(result))
    except Exception as e:
        ent.delete(0,END)
        ent.insert(0,"수식을 입력해주세요")

#C 버튼 클릭 시 입력 초기화
def clear():
    ent.delete(0,END) #입력창 초기화

#
def backsp():
    back = ent.get()
    ent.delete(len(back)-1, END)







#Tkinter 창 설정
win = Tk() #Tkinter 기본 창 생성
win.title("계산기") # 창 제목
win.geometry("350x400") #창 크기

ent = Entry(
    win,#부모 윈도우
    width = 20,#입력창 너비
    font=("돋움", 20),#폰트, 크기
    borderwidth=5,#테두리 두께
    justify="right"# 텍스트 오른쪽 정렬
)
ent.grid(row=0, column=0, columnspan=4, padx=10, pady=10) #그리드 배치


buttons = [
    'C', '<-', '%', '/',
    '7', '8', '9', '*',
    '4', '5', '6', '-',
    '1', '2', '3', '+',
    '+-', '0', '.', '='
]

col_val = 0
row_val = 1

for i in buttons: #버튼 리스트 순회
    if i == "=":
        btn = Button(win, text=i, width=5, height=2, command=cal, font=("돋움", 16, "bold"), relief="raised", bg="#FA58D0", fg="#FFFFFF")
    elif i == "C":
        btn = Button(win, text=i, width=5, height=2, command=clear, font=("돋움", 16, "bold"), relief="raised", bg="#F7819F", fg="#FFFFFF")
    elif i == "<-":
        btn = Button(win, text=i, width=5, height=2, command=backsp, font=("돋움", 16, "bold"), relief="raised", bg="#DA81F5", fg="#FFFFFF")
    else:
        btn = Button(win, text=i, width=5, height=2, command=lambda b = i: button_click(b), font=("돋움", 16, "bold"), relief="flat", bg="#ffffff", fg="#424242") #숫자 버튼
    #btn = Button(win, text=i, width=5, height=2, )
    btn.grid(row=row_val, column=col_val, padx=5, pady=5) #버튼 배치
    col_val += 1 #다음 열 이동
    if col_val > 3: #열값이 3 이상이면 다음 행 이동
        col_val= 0
        row_val += 1

win.mainloop()