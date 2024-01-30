import customtkinter as ctk
import os
import requests
from PIL import Image
import random

wopened = False

def maincloseevent():
    if wopened == True: pass
    else: main.destroy()


main = ctk.CTk()
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")
main.protocol('WM_DELETE_WINDOW', maincloseevent)
main.title('Камень, ножницы, бумага!')
mx = (main.winfo_screenwidth() - main.winfo_reqwidth()) / 2 - 300
my = (main.winfo_screenheight() - main.winfo_reqheight()) / 2 - 150
main.geometry(f'800x500+{int(mx)}+{int(my)}')
main.resizable(0, 0)

try: os.mkdir('images')
except FileExistsError: pass
try:
    with open('images\\ssp.ico', 'xb') as f:
        icourl = requests.get('https://raw.githubusercontent.com/ItsunePy/StoneScissorsPaper/master/images/ssp.ico').content
        f.write(icourl)
except FileExistsError: pass
try:
    with open('images\\mainbackground.png', 'xb') as f:
        bgurl = requests.get('https://raw.githubusercontent.com/ItsunePy/StoneScissorsPaper/master/images/mainbackground.png').content
        f.write(bgurl)
except FileExistsError: pass
try:
    with open('images\\background.png', 'xb') as f:
        bgurl = requests.get('https://raw.githubusercontent.com/ItsunePy/StoneScissorsPaper/master/images/background.png').content
        f.write(bgurl)
except FileExistsError: pass
try:
    with open('images\\stone.png', 'xb') as f:
        stoneurl = requests.get('https://raw.githubusercontent.com/ItsunePy/StoneScissorsPaper/master/images/stone.png').content
        f.write(stoneurl)
except FileExistsError: pass
try:
    with open('images\\scissors.png', 'xb') as f:
        scissorsurl = requests.get('https://raw.githubusercontent.com/ItsunePy/StoneScissorsPaper/master/images/scissors.png').content
        f.write(scissorsurl)
except FileExistsError: pass
try:
    with open('images\\paper.png', 'xb') as f:
        paperurl = requests.get('https://raw.githubusercontent.com/ItsunePy/StoneScissorsPaper/master/images/paper.png').content
        f.write(paperurl)
except FileExistsError: pass

try: os.mkdir('saves')
except FileExistsError: pass

main.iconbitmap('images\\ssp.ico')

a1, dataname, datapass, win, draw, lose = '', '', '', 0, 0, 0

def success():
    global logbtn, regbtn, errorlr, stats, win, draw, lose, dataname, accountname

    welcome.destroy()
    userlogin.destroy()
    userloginenter.destroy()
    logshow.destroy()
    userpassword.destroy()
    userpasswordenter.destroy()
    passshow.destroy()
    logbtn.destroy()
    noacc.destroy()
    noaccbtn.destroy()
    errorlr.destroy()

    mainwindoww.place(relx=0.2, rely=0.1, anchor='center')
    advancementsw.place(relx=0.8, rely=0.1, anchor='center')
    accountname.place(relx=0.5, rely=0.1, anchor='center')

    accountname.configure(text=f'Вы вошли под именем:\n{dataname}')
    stats.configure(text=f'На данный момент у вас:\n{win} побед\n{draw} ничьих\n{lose} поражений')
    advancementslabel1.configure(text=f'Первая победа - {a1}')

    mainbg = ctk.CTkImage(dark_image=Image.open('images\\mainbackground.png'), size=(800, 500))
    bglabel.configure(image=mainbg)

    mainwindow()


# UI

def start():
    global mainwindoww, startbtn, advancementsw, advancementslabel1, advancementslabel2, stoneb, scissorsb, paperb, message1, message2, message3

    startbtn.place_forget()
    mainwindoww.configure(state='disabled', fg_color='gray')
    advancementsw.configure(state='disabled', fg_color='gray')

    message1.place(relx=0.2, rely=0.35, anchor='center')
    message2.place(relx=0.2, rely=0.65, anchor='center')
    message3.place(relx=0.2, rely=0.75, anchor='center')

    stoneb.place(relx=0.07, rely=0.5, anchor='center')
    scissorsb.place(relx=0.2, rely=0.5, anchor='center')
    paperb.place(relx=0.33, rely=0.5, anchor='center')


def continuef():
    global stoneb, scissorsb, paperb, message1, message2, message3, startbtn, dataname, win, draw, lose, continuebtn

    continuebtn.place_forget()

    stoneb.configure(state='normal', fg_color='white')
    paperb.configure(state='normal', fg_color='white')
    scissorsb.configure(state='normal', fg_color='white')

    stoneb.place_forget()
    scissorsb.place_forget()
    paperb.place_forget()
    message1.place_forget()

    message2.configure(text='')
    message3.configure(text='')
    mainwindow()


def scissors():
    global stoneb, scissorsb, paperb

    stoneb.configure(state='disabled')
    paperb.configure(state='disabled')
    scissorsb.configure(state='disabled', fg_color='green')

    system(2)


def paper():
    global stoneb, scissorsb, paperb

    stoneb.configure(state='disabled')
    paperb.configure(state='disabled', fg_color='green')
    scissorsb.configure(state='disabled')

    system(3)


def stone():
    global stoneb, scissorsb, paperb

    stoneb.configure(state='disabled', fg_color='green')
    paperb.configure(state='disabled')
    scissorsb.configure(state='disabled')

    system(1)

def dataf(datanamef):
    global win, draw, lose, dataname, a1, datapass
    data = open("saves\\" + datanamef + '.txt', 'r')
    dataname = datanamef
    datapass = data.readline()[:-1]
    win = data.readline()[:-1]
    draw = data.readline()[:-1]
    lose = data.readline()[:-1]
    a1 = data.readline()[:-1]
    data.close()

    advancementslabel1.configure(text=f'Первая победа - {a1}')


def system(plr):
    global startbtn, stats, advancementsw, advancementslabel1, advancementslabel2, stoneb, scissorsb, paperb, \
        message2, message3, win, draw, lose, dataname, a1, datapass

    systemchoice = random.randint(1, 3)

    draw, win, lose = int(draw), int(win), int(lose)

    if plr == systemchoice: draw += 1
    elif plr == 1 and systemchoice == 2: win += 1
    elif plr == 1 and systemchoice == 3: lose += 1
    elif plr == 2 and systemchoice == 1: lose += 1
    elif plr == 2 and systemchoice == 3: win += 1
    elif plr == 3 and systemchoice == 1: win += 1
    elif plr == 3 and systemchoice == 2: lose += 1

    if systemchoice == 1: message2.configure(text='Система выбрала Камень!')
    elif systemchoice == 2: message2.configure(text='Система выбрала Ножницы!')
    elif systemchoice == 3: message2.configure(text='Система выбрала Бумагу!')

    if plr == systemchoice: message3.configure(text_color='white', text='Система сделала тот же выбор, что и вы.\nНичья!')
    elif plr == 1 and systemchoice == 2: message3.configure(text_color='green', text='Камень сломал Ножницы.\nВы победили!')
    elif plr == 1 and systemchoice == 3: message3.configure(text_color='red', text='Бумага накрыла Камень.\nВы проиграли!')
    elif plr == 2 and systemchoice == 1:message3.configure(text_color='red', text='Камень сломал Ножницы.\nВы проиграли!')
    elif plr == 2 and systemchoice == 3: message3.configure(text_color='green', text='Ножницы разрезали Бумагу.\nВы победили!')
    elif plr == 3 and systemchoice == 1: message3.configure(text_color='green', text='Бумага накрыла Камень.\nВы победили!')
    elif plr == 3 and systemchoice == 2: message3.configure(text_color='red', text='Ножницы разрезали Бумагу.\nВы проиграли!')

    # Advancements

    if int(win) >= 1 and a1 == 'X':
        a1 = 'V'

    data = open("saves\\" + dataname + '.txt', 'w')
    data.write(datapass + '\n' + str(win) + '\n' + str(draw) + '\n' + str(lose) + '\n' + str(a1) + '\n')
    data.close()

    dataf(dataname)

    stats.configure(text=f'На данный момент у вас:\n{win} побед\n{draw} ничьих\n{lose} поражений')
    advancementslabel1.configure(text=f'Первая победа - {a1}')

    continuebtn.place(relx=0.8, rely=0.7, anchor='center')


# Main

def mainwindow():
    global mainwindoww, advancementsw, startbtn, stats, advancementslabel1, advancementslabel2

    mainwindoww.configure(state='disabled', fg_color='gray')
    advancementsw.configure(state='normal', fg_color='blue')

    advancementslabel1.place_forget()
    advancementslabel2.place_forget()

    startbtn.place(relx=0.2, rely=0.5, anchor='center')
    stats.place(relx=0.8, rely=0.5, anchor='center')


def advancements():
    global mainwindoww, advancementsw, advancementslabel1, advancementslabel2, startbtn, stats

    mainwindoww.configure(state='normal', fg_color='blue')
    advancementsw.configure(state='disabled', fg_color='gray')

    startbtn.place_forget()
    stats.place_forget()

    advancementslabel1.configure(text=f'Первая победа - {a1}')
    advancementslabel1.place(relx=0.25, rely=0.6, anchor='center')
    advancementslabel2.place(relx=0.75, rely=0.6, anchor='center')


# Start functions

###

def s_or_h_log():
    if userloginenter.cget('show') == '●': userloginenter.configure(show='')
    else: userloginenter.configure(show='●')

def s_or_h_pass():
    if userpasswordenter.cget('show') == '●': userpasswordenter.configure(show='')
    else: userpasswordenter.configure(show='●')

blacklist = ['а', 'б', 'в', 'г', 'д', 'ё', 'ж', 'з', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я', ' ', 'А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ж', 'З', 'И', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я']

def validate_input(text):
    if len(text) < 19:
        for i in text:
            if i in blacklist: return False
        return True
    else: return False

def loginfunc():

    global errorlr
    dataname = userloginenter.get()
    try: data = open("saves\\" + dataname + '.txt', 'r')
    except FileNotFoundError: errorlr.configure(text='Аккаунт не найден.')
    else:
        with data:
            datapass = userpasswordenter.get()
            data = open("saves\\" + dataname + '.txt', 'r')
            check = data.readline()
            data.close()
            check = check[:-1]
            if check == datapass:
                dataf(dataname)
                success()
            elif check != datapass:
                errorlr.configure(text='Пароли не совпадают.')

###

def registrationscript():
    global mx, my, regbtn, wopened

    noaccbtn.configure(state='disabled')
    logbtn.configure(state='disabled')

    wopened = True

    def s_or_h_log():
        if loginenter.cget('show') == '●': loginenter.configure(show='')
        else: loginenter.configure(show='●')

    def s_or_h_pass():
        if passwordenter.cget('show') == '●': passwordenter.configure(show='')
        else: passwordenter.configure(show='●')

    def s_or_h_pass_2():
        if passwordenter2.cget('show') == '●': passwordenter2.configure(show='')
        else: passwordenter2.configure(show='●')

    def regcloseevent():
        global wopened
        regbtn.configure(state='normal')
        logbtn.configure(state='normal')
        wopened = False
        reg.destroy()

    reg = ctk.CTk()
    reg.title('Регистрация')
    reg.geometry(f'400x500+{int(mx) + 820}+{int(my)}')
    reg.resizable(0, 0)
    reg.iconbitmap('images\ssp.ico')

    def registration():
        global errorlr, wopened
        dataname = loginenter.get()
        try: data = open("saves\\" + dataname + '.txt', 'x')
        except FileExistsError: errorlr.configure(text='Логин занят.')
        else:
            with data:
                if len(dataname) < 4:
                    errorlr.configure(text='Логин слишком короткий.')
                    data.close()
                    os.remove("saves\\" + dataname + '.txt')
                elif len(dataname) > 14:
                    data.close()
                    os.remove("saves\\" + dataname + '.txt')
                else:
                    datapass = passwordenter.get()
                    datapass2 = passwordenter2.get()
                    if datapass2 != datapass:
                        errorlr.configure(text='Пароли не совпадают.')
                        data.close()
                        os.remove("saves\\" + dataname + '.txt')
                    else:
                        if len(datapass) < 4:
                            errorlr.configure(text='Пароль слишком короткий.')
                            data.close()
                            os.remove("saves\\" + dataname + '.txt')
                        else:
                            data.write(datapass + '\n' + '0\n' + '0\n' + '0\n' + 'X\n')
                            data.close()
                            data = open("saves\\" + dataname + '.txt', 'r')
                            check = data.readline()
                            data.close()
                            check = check[:-1]
                            if check == datapass:
                                dataf(dataname)
                                success()
                                wopened = False
                                reg.destroy()
                            else:
                                data.close()
                                os.remove("saves\\" + dataname + '.txt')

    validate_cmd = (reg.register(validate_input), '%P')

    regwelcome = ctk.CTkLabel(master=reg, text='Регистрация', font=('Minecraft Rus', 20), text_color='green')
    login = ctk.CTkLabel(master=reg, text='Логин', font=('Minecraft Rus', 18))
    loginenter = ctk.CTkEntry(master=reg, show='●', validate='key', validatecommand=validate_cmd, width=200, height=50)
    logshow = ctk.CTkSwitch(master=reg, text='', width=50, command=s_or_h_log, height=50)
    password = ctk.CTkLabel(master=reg, text='Пароль', font=('Minecraft Rus', 18))
    passwordenter = ctk.CTkEntry(master=reg, show='●', validate='key', validatecommand=validate_cmd, width=200, height=50)
    passwordenter2 = ctk.CTkEntry(master=reg, show='●', validate='key', validatecommand=validate_cmd, width=200, height=50)
    passshow = ctk.CTkSwitch(master=reg, text='', width=50, command=s_or_h_pass, height=50)
    passshow2 = ctk.CTkSwitch(master=reg, text='', width=50, command=s_or_h_pass_2, height=50)
    regbtn = ctk.CTkButton(master=reg, text='Зарегистрироваться', font=('Minecraft Rus', 13), command=registration, height=50, width=200)

    regwelcome.place(relx=0.5, rely=0.1, anchor='center')
    login.place(relx=0.5, rely=0.21, anchor='center')
    loginenter.place(relx=0.5, rely=0.3, anchor='center')
    logshow.place(relx=0.825, rely=0.3, anchor='center')
    password.place(relx=0.5, rely=0.39, anchor='center')
    passwordenter.place(relx=0.5, rely=0.48, anchor='center')
    passwordenter2.place(relx=0.5, rely=0.59, anchor='center')
    passshow.place(relx=0.825, rely=0.48, anchor='center')
    passshow2.place(relx=0.825, rely=0.59, anchor='center')
    regbtn.place(relx=0.5, rely=0.71, anchor='center')

    reg.protocol('WM_DELETE_WINDOW', regcloseevent)

    reg.mainloop()

bg = ctk.CTkImage(dark_image=Image.open('images\\background.png'), size=(800, 500))
bglabel = ctk.CTkLabel(master=main, image=bg, text='')
bglabel.place(x=0, y=0, relwidth=1, relheight=1)

###

validate_cmd = (main.register(validate_input), '%P')

welcome = ctk.CTkLabel(master=main, text='Добро пожаловать!', font=('Minecraft Rus', 20), bg_color='gray17', text_color='lightblue')
userlogin = ctk.CTkLabel(master=main, text='Логин', font=('Minecraft Rus', 18), bg_color='gray17')
userloginenter = ctk.CTkEntry(master=main, show='●', validate='key', validatecommand=validate_cmd, width=200, height=50)
logshow = ctk.CTkSwitch(master=main, text='', width=50, command=s_or_h_log, height=50, bg_color='gray17')
userpassword = ctk.CTkLabel(master=main, text='Пароль', font=('Minecraft Rus', 18), bg_color='gray17')
userpasswordenter = ctk.CTkEntry(master=main, show='●', validate='key', validatecommand=validate_cmd,width=200, height=50)
passshow = ctk.CTkSwitch(master=main, text='', width=50, command=s_or_h_pass, height=50, bg_color='gray17')
logbtn = ctk.CTkButton(master=main, text='Войти', font=('Minecraft Rus', 18), command=loginfunc, height=50, width=200)

welcome.place(relx=0.815, rely=0.1, anchor='center')
userlogin.place(relx=0.815, rely=0.21, anchor='center')
userloginenter.place(relx=0.815, rely=0.3, anchor='center')
logshow.place(relx=0.975, rely=0.3, anchor='center')
userpassword.place(relx=0.815, rely=0.39, anchor='center')
userpasswordenter.place(relx=0.815, rely=0.48, anchor='center')
passshow.place(relx=0.975, rely=0.48, anchor='center')
logbtn.place(relx=0.815, rely=0.6, anchor='center')

###

noacc = ctk.CTkLabel(master=main, text='Нет аккаунта?', font=('Minecraft Rus', 16), bg_color='gray17', text_color='lightblue')

errorlr = ctk.CTkLabel(master=main, text='', text_color='red', font=('Minecraft Rus', 14), bg_color='gray17')
noaccbtn = ctk.CTkButton(master=main, text='Жми сюда!', command=registrationscript, width=200, font=('Minecraft Rus', 14), fg_color='gray17', text_color='green', hover_color='gray17')

errorlr.place(relx=0.815, rely=0.72, anchor='center')
noaccbtn.place(relx=0.815, rely=0.88, anchor='center')
noacc.place(relx=0.815, rely=0.82, anchor='center')

mainwindoww = ctk.CTkButton(master=main, text='Главное окно', command=mainwindow, font=('Minecraft Rus', 14), height=80, width=150)
advancementsw = ctk.CTkButton(master=main, text='Достижения', command=advancements, font=('Minecraft Rus', 14), height=80, width=150)
accountname = ctk.CTkLabel(master=main, text='', text_color='white', font=('Minecraft Rus', 14), justify='center', height=80, width=200)
startbtn = ctk.CTkButton(master=main, text='Начать', command=start, font=('Minecraft Rus', 14), height=100, width=200)
stats = ctk.CTkLabel(master=main, text='', text_color='green', font=('Minecraft Rus', 14), justify='center', height=100, width=230)

advancementslabel1 = ctk.CTkLabel(master=main, text='Достижения...', text_color='green', font=('Minecraft Rus', 14), justify='left', height=350, width=380)
advancementslabel2 = ctk.CTkLabel(master=main, text='', text_color='green', font=('Minecraft Rus', 14), justify='center', height=350, width=380)

stoneb = ctk.CTkButton(master=main, text='', command=stone, image=ctk.CTkImage(dark_image=Image.open('images\stone.png'), size=(80, 80)), height=100, width=100, font=('Minecraft Rus', 14), fg_color='white')
scissorsb = ctk.CTkButton(master=main, text='', command=scissors, image=ctk.CTkImage(dark_image=Image.open('images\scissors.png'), size=(80, 80)), height=100, width=100, font=('Minecraft Rus', 14), fg_color='white')
paperb = ctk.CTkButton(master=main, text='', command=paper, image=ctk.CTkImage(dark_image=Image.open('images\paper.png'), size=(80, 80)), height=100, width=100, font=('Minecraft Rus', 14), fg_color='white')

message1 = ctk.CTkLabel(master=main, text='Сделайте свой выбор:', text_color='green', font=('Minecraft Rus', 14), justify='center')
message2 = ctk.CTkLabel(master=main, text='', font=('Minecraft Rus', 14), justify='center')
message3 = ctk.CTkLabel(master=main, text='', font=('Minecraft Rus', 12), justify='center')

continuebtn = ctk.CTkButton(master=main, text='Продолжить', command=continuef, height=100, width=230, font=('Minecraft Rus', 14))

main.mainloop()