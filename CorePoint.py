from tkinter import *
import tkinter as tk
from typing import Union
from typing import List
from PIL import Image, ImageTk
from tkinter import PhotoImage
from tkinter import Canvas, Scrollbar
import time, json
import datetime
import OpenAInya
import CoreFlash
import Plagiarisme

sekarang = datetime.datetime.now()

gui = Tk()
gui.title("CorePoint")

lebar = gui.winfo_screenwidth()
tinggi = gui.winfo_screenheight()
gui.geometry(f"{lebar}x{tinggi}")

bg_awal = Image.open("home.webp")
if bg_awal.width < lebar or bg_awal.height < tinggi:
    bg_awal = bg_awal.resize((lebar, tinggi), Image.ANTIALIAS)
get_bg_awal = ImageTk.PhotoImage(bg_awal)

bg_home = Image.open("home.webp")
if bg_home.width < lebar or bg_home.height < tinggi:
    bg_home = bg_home.resize((lebar, tinggi), Image.ANTIALIAS)
bg_homenya = ImageTk.PhotoImage(bg_home)

post_img1 = Image.open("solarsystem.jpg")
get_post_img1 = ImageTk.PhotoImage(post_img1.resize((200,500), Image.ANTIALIAS))
post_img2 = Image.open("search.png")
get_post_img2 = ImageTk.PhotoImage(post_img2.resize((200,200), Image.ANTIALIAS))
post_img3 = Image.open("search.png")
get_post_img3 = ImageTk.PhotoImage(post_img3.resize((200,200), Image.ANTIALIAS))
post_img4 = Image.open("search.png")
get_post_img4 = ImageTk.PhotoImage(post_img4.resize((200,200), Image.ANTIALIAS))

canvas = Canvas(gui, bg="black", width=lebar, height=tinggi)
canvas.pack()

class ScrollableCanvas(Canvas):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.bind("<Configure>", self.on_configure)
        self.frame = tk.Frame(self)
        self.create_window((0, 0), window=self.frame, anchor="nw")

    def on_configure(self, event):
        self.configure(scrollregion=self.bbox("all"))

def temp_text(canvasss, text_id):
    canvasss.delete(text_id)

def copy_text(event):
    event.widget.event_generate("<<Copy>>")

def paste_text(event):
    event.widget.event_generate("<<Paste>>")

def show_ep_text():
    canvas.itemconfig(teks_ep, state=NORMAL)

def animate_text():
    text = "CorePoint"
    for i in range(len(text) + 1):
        canvas.itemconfig(teks_CorePoint, text=text[:i])
        gui.update()
        time.sleep(0.1)
    time.sleep(1)
    reset_screen()
    create_login_view()

def reset_screen():
    canvas.delete("all")
def reset_gui():
    for widget in gui.winfo_children():
            widget.destroy()

def create_login_view():
    global entry_username
    global entry_password

    canvas.create_image(0, 0, anchor=NW, image=get_bg_awal)
    canvas.create_text(150, 60, text="CorePoint", fill="white", font=("Segoe Print", 36))
    canvas.create_text(690, 230, text="Login", fill="white", font=("Helvetica", 18))
    canvas.create_text(580, 300, text="Username", fill="white", font=("Helvetica", 10))
    canvas.create_text(580, 355, text="Password", fill="white", font=("Helvetica", 10))
    canvas.create_text(600, 470, text="Belum punya akun?", fill="white", font=("Helvetica", 10))

    entry_username = Entry(gui, width=30)
    entry_password = Entry(gui, width=30)
    entry_username.place(x=620, y=300, anchor="w")
    entry_password.place(x=620, y=355, anchor="w")

    label_button_signup = Button(gui, text="Sign Up")
    label_button_login = Button(gui, text="Login", command=get_logged)
    label_button_login.place(x=805, y=425, anchor="e")
    label_button_signup.place(x=670, y=460)
    
def loading(a,b):
    for _ in range(4):
        canvas.delete("loading_tag")
        canvas.create_text(a, b, text="Loading" + "." * _, font=("Helvetica", 12), tag="loading_tag")
        gui.update()
        time.sleep(0.5)

def get_logged():
    if entry_username.get() == "q":
        if entry_password.get() == "q":
            loading(715,425)
            main()
def start_animation():
    global canvas

    create_new_window()
    gui.after(500, show_ep_text)
    gui.after(1500, animate_text)

def create_new_window():
    global teks_ep
    global teks_CorePoint

    teks_ep = canvas.create_text(lebar/2, tinggi/2 - 50, text="CP", font=("Segoe Print", 48), fill="white", anchor="center")
    canvas.itemconfig(teks_ep, state=HIDDEN)
    teks_CorePoint = canvas.create_text(lebar/2, tinggi/2 + 50, text="", font=("Segoe Print", 18), fill="white", anchor="center")

def on_entry_click(event):
    if entry_search.get() == "Searching on CorePoint":
        entry_search.delete(0, "end")
        entry_search.configure(fg="black") 

def on_entry_leave(event):
    if not entry_search.get():
        entry_search.insert(0, "Searching on CorePoint")
        entry_search.configure(fg="gray") 

def search():
    keyword = entry_search.get()
    if keyword == "Searching in CorePoint":
        keyword = ""

    print("Keyword pencarian:", keyword)
def GoToBack():
    main()

def req_openai():
    global y

    text = entry_openai.get()
    tentang_n = text.find("\n")
    scroll_openai.create_text(10,y, text="You :", font=("arial", 12), fill="black", anchor="nw")
    y+=25

    if len(text) >=120 and tentang_n < 0:
        parag1 = paragraf(text)
        for teks in parag1:
            scroll_openai.create_text(10,y, text=teks, font=("arial", 12), fill="black", anchor="nw")
            y+=25
    elif tentang_n <= 120:
        scroll_openai.create_text(10,y, text=text, font=("arial", 12), fill="black", anchor="nw")
        y+=25
    else:
        kumpul = []
        kumpul_sementara = []
        for revisi_kalimat in text.splitlines():
            revisi = paragraf(revisi_kalimat)
            kumpul.append(revisi)
        for hasil_revisi in kumpul[0]:
            scroll_openai.create_text(10,y, text=hasil_revisi, font=("arial", 12), fill="black", anchor="nw")
            y+=25
    gui.update_idletasks()
    get_respon(text)
def get_respon(q):
    global y

    scroll_openai.create_text(10,y, text="Respon : ", font=("arial", 12), fill="black", anchor="nw")
    y+=25
    get_res = OpenAInya.getting(q)
    tentang_n = get_res.find("\n")
    if len(get_res) >=120 and tentang_n < 0:
        parag1 = paragraf(get_res)
        for teks in parag1:
            scroll_openai.create_text(10,y, text=teks, font=("arial", 12), fill="black", anchor="nw")
            y+=25
    elif tentang_n <= 120:
        scroll_openai.create_text(10,y, text=get_res, font=("arial", 12), fill="black", anchor="nw")
        y += len(get_res.splitlines()) * 25
    else:
        kumpul = []
        kumpul_sementara = []
        for revisi_kalimat in get_res.splitlines():
            revisi = paragraf(revisi_kalimat)
            kumpul.append(revisi)
        for hasil_revisi in kumpul[0]:
            scroll_openai.create_text(10,y, text=hasil_revisi, font=("arial", 12), fill="black", anchor="nw")
            y+=25
def clear_openai():
    OpenAI()
def OpenAI():
    global canvas_main_openai
    global canvas_openai
    global scroll_openai
    global scrollbar_openai
    global entry_openai
    global y

    reset_gui()

    canvas_main_openai = Canvas(gui, bg="black", width=lebar, height=tinggi)
    canvas_main_openai.pack()
    canvas_main_openai.create_image(0, 0, anchor=NW, image=bg_homenya)
    Label(bg="black", text="   OpenAI", fg="white", font=("Segoe Print", 24), width=194, height=1, anchor="w").place(x=2, y=3)

    button_back = Button(gui, text="<", command=GoToBack, bg="white", font=("Arial Bold", 12), width=5)
    button_back.place(x=50, y=80)

    Canvas(gui, bg="black", width=1030, height=520).place(x=140,y=140)
    canvas_openai = Canvas(gui, bg="black", width=4000, height=50)
    canvas_openai.place(x=150,y=150)

    scroll_openai = ScrollableCanvas(canvas_openai)
    scroll_openai.pack(side="top", fill="y", expand=True)

    scrollbar_openai = Scrollbar(canvas_openai, orient="vertical", command=scroll_openai.yview)
    scrollbar_openai.place(x=996, y=0, height=430)

    scroll_openai.config(yscrollcommand=scrollbar_openai.set, height=500, width=1010)
    
    entry_openai = Entry(canvas_openai, width=100, fg="black", font=("arial", 12), highlightthickness=10, highlightbackground="white", borderwidth=0)
    entry_openai.place(x="0", y="450")
    entry_openai.bind("<Control-c>")
    entry_openai.bind("<Control-v>")
    
    send_button_openai = Button(scroll_openai, text=">",command=lambda: req_openai(), font=("Arial Bold", 16), width="5")
    send_button_openai.place(x="925", y="450")
    clear_button_openai = Button(gui, text="clear",command=clear_openai, font=("Arial Bold", 15), width="13",fg="white", bg="black")
    clear_button_openai.place(x="1177", y="155")

    y = 15
    entry_openai.focus_set()

def paragraf(text_input):
    max_karakter = 120
    kumpulan = []
    kumpulan_saat_ini = []

    for kata in text_input.split():
        if len(" ".join(kumpulan_saat_ini + [kata])) <= max_karakter:
            kumpulan_saat_ini.append(kata)
        else:
            kumpulan.append(" ".join(kumpulan_saat_ini))
            kumpulan_saat_ini = [kata]

    if kumpulan_saat_ini:
        kumpulan.append(" ".join(kumpulan_saat_ini))

    return kumpulan

def post_coreflash():
    global y_coreflash

    text = entry_coreflash.get()
    if "\n" in text and text.find("\n") <= 120 :
        scroll_coreflash.create_text(10,y_coreflash, text=text, font=("arial", 12), fill="black", anchor="nw")
        y_coreflash += len(text.splitlines() * 20)
    else:
        parag = paragraf(text)
        for teks in parag:
            scroll_coreflash.create_text(10,y_coreflash, text=teks, font=("arial", 12), fill="black", anchor="nw")
            y_coreflash+=25
    get_res = CoreFlash.PostCoreFlash(text)
    text_sukses_post = scroll_coreflash.create_text(370, 3, text=get_res, font=("arial", 12), fill="black", anchor="nw")
    scroll_coreflash.after(2000, temp_text, scroll_coreflash, text_sukses_post)
    baris = len(get_res.splitlines()) * 20
    y_coreflash+=baris
def get_coreflash():
    global y_coreflash

    text = entry_coreflash.get()
    if "\n" in text:
        tentang_n = text.find("\n")
        if tentang_n <= 120:
            scroll_coreflash.create_text(10,y_coreflash, text="Keyword : "+text, font=("arial", 12), fill="black", anchor="nw")
            y_coreflash += 25
        else:
            kumpul = []
            for revisi_kalimat in text.splitlines():
                revisi = paragraf(revisi_kalimat)
                kumpul.append(revisi)
            for hasil_revisi in kumpul:
                scroll_coreflash.create_text(10,y_coreflash, text="Keyword : "+hasil_revisi, font=("arial", 12), fill="black", anchor="nw")
                y_coreflash+=25
    else:
        parag1 = paragraf(text)
        for teks1 in parag1:
            scroll_coreflash.create_text(10,y_coreflash, text="Keyword : "+teks1, font=("arial", 12), fill="black", anchor="nw")
            y_coreflash+=25

    get_res = CoreFlash.GetCoreFlash(text)
    for resnya in get_res:
        tentang_n = resnya.find("\n")
        if len(resnya) >= 120 and tentang_n < 0:
            parag1 = paragraf(" ".join(get_res))
            for teksnya in parag1:
                scroll_coreflash.create_text(10,y_coreflash, text=teksnya, font=("arial", 12), fill="black", anchor="nw")
                y_coreflash += 25
        elif tentang_n <= 120:
            scroll_coreflash.create_text(10,y_coreflash, text=resnya, font=("arial", 12), fill="black", anchor="nw")
            y_coreflash += len(resnya.splitlines() * 20)
        else:
            kumpul = []
            kumpul_sementara = []
            for revisi_kalimat in resnya.splitlines():
                revisi = paragraf(revisi_kalimat)
                kumpul.append(revisi)
            for hasil_revisi in kumpul[0]:
                scroll_coreflash.create_text(10,y_coreflash, text=hasil_revisi, font=("arial", 12), fill="black", anchor="nw")
                y_coreflash+=25

def clear_coreflash():
    coreflash()
def coreflash():
    global canvas_main_coreflash
    global canvas_coreflash
    global scroll_coreflash
    global scrollbar_coreflash
    global entry_coreflash
    global y_coreflash

    reset_gui()

    canvas_main_coreflash = Canvas(gui, bg="black", width=lebar, height=tinggi)
    canvas_main_coreflash.pack()
    canvas_main_coreflash.create_image(0, 0, anchor=NW, image=bg_homenya)
    Label(bg="black", text="   CoreFlash", fg="white", font=("Segoe Print", 24), width=194, height=1, anchor="w").place(x=2, y=3)

    button_back = Button(gui, text="<", command=GoToBack, bg="white", font=("Arial Bold", 12), width=5)
    button_back.place(x=50, y=80)

    Canvas(gui, bg="black", width=1030, height=520).place(x=140,y=140)
    canvas_coreflash = Canvas(gui, bg="black", width=4000, height=50)
    canvas_coreflash.place(x=150,y=150)

    scroll_coreflash = ScrollableCanvas(canvas_coreflash)
    scroll_coreflash.pack(side="top", fill="y", expand=True)

    scrollbar_coreflash = Scrollbar(canvas_coreflash, orient="vertical", command=scroll_coreflash.yview)
    scrollbar_coreflash.place(x=996, y=0, height=430)

    scroll_coreflash.config(yscrollcommand=scrollbar_coreflash.set, height=500, width=1010)
    
    entry_coreflash = Entry(canvas_coreflash, width=88, fg="black", font=("arial", 12), bg="white", highlightthickness=10, borderwidth=0)
    entry_coreflash.place(x="91", y="450")
    entry_coreflash.bind("<Control-c>")
    entry_coreflash.bind("<Control-v>")

    send_button_coreflash = Button(scroll_coreflash, text="submit",command=post_coreflash, font=("Arial Bold", 15), width="5", bg="blue")
    send_button_coreflash.place(x="5", y="450")
    send_button_coreflash = Button(scroll_coreflash, text="search",command=get_coreflash, font=("Arial Bold", 15), width="5")
    send_button_coreflash.place(x="925", y="450")
    clear_button_coreflash = Button(gui, text="clear",command=clear_coreflash, font=("Arial Bold", 15), width="13",fg="white", bg="black")
    clear_button_coreflash.place(x="1177", y="155")

    y_coreflash = 15
    entry_coreflash.focus_set()

def GetHasilPlag():
    global y_plagiarisme
    
    text = entry_plagiarisme.get()
    get_hasil = Plagiarisme.CekPlag(text)
    ngelist = get_hasil["highlight"]
    HighL=[]
    for i,x in enumerate(text.split()):
        status_HL = False
        for j in ngelist:
            if int(i) >= int(j[0]) and int(i) <= int(j[1]):
                HighL.append(x.upper())
                status_HL = True
                break
        if not status_HL:
            HighL.append(x)
    if get_hasil["error_code"] == 0 and get_hasil["error"] == "":
        Text = f"{text}"
        Unik = f"{float(get_hasil['percent'])}%"
        Plagiat = f"{100 - float(get_hasil['percent']):.1f}%"
        Highlight = f"{' '.join(HighL)}"
        Jumlah_kata = f"{len(text.split())}"

        scroll_plagiarisme.create_text(10,y_plagiarisme, text="============================================================================", font=("arial", 12), fill="black", anchor="nw")
        y_plagiarisme+=20
        scroll_plagiarisme.create_text(10,y_plagiarisme, text=f"Jumlah Kata : {Jumlah_kata}", font=("arial", 12), fill="black", anchor="nw")
        y_plagiarisme+=20
        scroll_plagiarisme.create_text(10,y_plagiarisme, text=f"Unik          : {Unik}", font=("arial", 12), fill="blue", anchor="nw")
        y_plagiarisme+=20
        scroll_plagiarisme.create_text(10,y_plagiarisme, text=f"Plagiat       : {Plagiat}", font=("arial", 12), fill="red", anchor="nw")
        y_plagiarisme+=20
        scroll_plagiarisme.create_text(10,y_plagiarisme, text="============================================================================", font=("arial", 12), fill="black", anchor="nw")
        y_plagiarisme+=20
        scroll_plagiarisme.create_text(10,y_plagiarisme, text=f"Highlight Plagiat :", font=("arial", 12), fill="red", anchor="nw")
        y_plagiarisme+=20
        for revisi_list in paragraf(str(ngelist)):
            scroll_plagiarisme.create_text(10,y_plagiarisme, text=f"{revisi_list}", font=("arial", 12), fill="red", anchor="nw")
            y_plagiarisme+=20
        scroll_plagiarisme.create_text(10,y_plagiarisme, text="============================================================================", font=("arial", 12), fill="black", anchor="nw")
        y_plagiarisme+=20
        scroll_plagiarisme.create_text(10,y_plagiarisme, text=f"Sumber Plagiat: ", font=("arial", 12), fill="red", anchor="nw")
        y_plagiarisme+=20
        for sumber in get_hasil["matches"]:
            scroll_plagiarisme.create_text(10,y_plagiarisme, text=f"{sumber.get('url')}", font=("arial", 12), fill="red", anchor="nw")
            y_plagiarisme+=20
        scroll_plagiarisme.create_text(10,y_plagiarisme, text="============================================================================", font=("arial", 12), fill="black", anchor="nw")
        y_plagiarisme+=40
        parag = paragraf(Highlight)
        for tek in parag:
            scroll_plagiarisme.create_text(10,y_plagiarisme, text=tek, font=("arial", 12), fill="black", anchor="nw")
            y_plagiarisme+=20

    else:
        print("gagal")
def clear_plag():
    plagiarisme()
def plagiarisme():
    global canvas_main_plagiarisme
    global canvas_plagiarisme
    global scroll_plagiarisme
    global scrollbar_plagiarisme
    global entry_plagiarisme
    global y_plagiarisme

    reset_gui()

    canvas_main_plagiarisme = Canvas(gui, bg="black", width=lebar, height=tinggi)
    canvas_main_plagiarisme.pack()
    canvas_main_plagiarisme.create_image(0, 0, anchor=NW, image=bg_homenya)
    Label(bg="black", text="   Plagiarism", fg="white", font=("Segoe Print", 24), width=194, height=1, anchor="w").place(x=2, y=3)

    button_back = Button(gui, text="<", command=GoToBack, bg="white", font=("Arial Bold", 12), width=5)
    button_back.place(x=10, y=80)

    Canvas(gui, bg="black", width=1170, height=600).place(x=90,y=90)
    canvas_plagiarisme = Canvas(gui, bg="black", width=4000, height=5000)
    canvas_plagiarisme.place(x=100,y=100)

    scroll_plagiarisme = ScrollableCanvas(canvas_plagiarisme)
    scroll_plagiarisme.pack(side="top", fill="y", expand=True)

    scrollbar_plagiarisme = Scrollbar(canvas_plagiarisme, orient="vertical", command=scroll_plagiarisme.yview)
    scrollbar_plagiarisme.place(x=1140, y=0, height=580)

    scroll_plagiarisme.config(yscrollcommand=scrollbar_plagiarisme.set, height=590, width=1150)
    
    entry_plagiarisme = Entry(canvas_plagiarisme, width=100, fg="black", font=("arial", 12), bg="white", highlightthickness=10, borderwidth=0)
    entry_plagiarisme.place(x="10", y="550")
    entry_plagiarisme.bind("<Control-c>")
    entry_plagiarisme.bind("<Control-v>")

    send_button_plagiarisme = Button(scroll_plagiarisme, text="CEK Plagiarism",command=GetHasilPlag, font=("Arial Bold", 15), width="15", bg="blue")
    send_button_plagiarisme.place(x="943", y="549")
    clear_button_plagiarisme = Button(gui, text="clear",command=clear_plag, font=("Arial Bold", 15), width="5",fg="white", bg="black")
    clear_button_plagiarisme.place(x="1275", y="110")

    y_plagiarisme = 15
    entry_plagiarisme.focus_set()
def main():
    global entry_search
    global canvas_main

    reset_gui()

    canvas_main = Canvas(gui, bg="black", width=lebar, height=tinggi)
    canvas_main.pack()

    canvas_main.create_image(0, 0, anchor=NW, image=bg_homenya)
    Label(bg="black", text="   CorePoint", fg="white", font=("Segoe Print", 24), width=194, height=1, anchor="w").place(x=2, y=3)
    Label(bg="white", width=153, height=2, anchor="w").place(x=50, y=110)

    entry_search = Entry(gui, font=("Simplified Arabic Fixed", 12), width=97, fg="black",borderwidth=0)
    entry_search.place(x=56, y=128, anchor="w")
    entry_search.insert(0, "Searching on CorePoint")
    entry_search.configure(fg="gray") 
    entry_search.bind("<FocusIn>", on_entry_click)
    entry_search.bind("<FocusOut>", on_entry_leave)

    button_search = Button(gui, text="🔍", font=("Arial Bold", 14), width=7, borderwidth=0, bg="white", command=search)
    button_search.place(x=1037, y=127, anchor="w")

    filternya = Menubutton(gui, text="Filter ▼", font=("Arial Bold", 20), width=10, borderwidth=0, anchor="c", fg="black", bg="blue")
    filternya.place(x=100,y=200)
    filternya_menu = Menu(filternya, tearoff=0, borderwidth=0, bg="blue")
    filternya.config(menu=filternya_menu)
    filternya_menu.add_command(label="    Terbaru", command=lambda: print("Terbaru"))
    filternya_menu.entryconfig(0, background="white", foreground="blue", font=("Times New Roman", 14, "bold"))
    filternya_menu.add_command(label="  Terpopuler ", command=lambda: print("Terpopuler"))
    filternya_menu.entryconfig(1, background="white", foreground="blue", font=("Times New Roman", 14, "bold"))
    filternya_menu.add_command(label="   Poin Besar ", command=lambda: print("Poin besar"))
    filternya_menu.entryconfig(2, background="white", foreground="blue", font=("Times New Roman", 14, "bold"))

    tool = Menubutton(gui, text="Tools ▼", font=("Arial Bold", 20), width=10, borderwidth=0, anchor="c", fg="black", bg="blue")
    tool.place(x=320,y=200)
    toolnya_menu = Menu(tool, tearoff=0, borderwidth=0, bg="blue")
    tool.config(menu=toolnya_menu)
    toolnya_menu.add_command(label=" Plagiarisme  ", command=plagiarisme)
    toolnya_menu.entryconfig(0, background="white", foreground="blue", font=("Times New Roman", 14, "bold"))
    toolnya_menu.add_command(label="    OpenAI ", command=OpenAI)
    toolnya_menu.entryconfig(1, background="white", foreground="blue", font=("Times New Roman", 14, "bold"))
    toolnya_menu.add_command(label="  CoreFlash ", command=coreflash)
    toolnya_menu.entryconfig(2, background="white", foreground="blue", font=("Times New Roman", 14, "bold"))
    toolnya_menu.add_command(label="  Pengingat ", command=lambda: print("Pengingat"))
    toolnya_menu.entryconfig(3, background="white", foreground="blue", font=("Times New Roman", 14, "bold"))
    toolnya_menu.add_command(label="      Notes", command=lambda: print("Notes"))
    toolnya_menu.entryconfig(4, background="white", foreground="blue", font=("Times New Roman", 14, "bold"))

    helping = Menubutton(gui, text="Help", font=("Arial Bold", 20), width=10, borderwidth=0, anchor="c", fg="black", bg="blue")
    helping.place(x=540,y=200)
    informasi()
    chat()
def post_img(x):
    bg_awal = PhotoImage(file=x)
    return bg_awal

def informasi():
    global scroll

    canvas_informasi = Canvas(gui, bg="black", width=4000, height=5000)
    canvas_informasi.place(x=56,y=270)

    scroll = ScrollableCanvas(canvas_informasi)
    scroll.pack(side="top", fill="y", expand=True)

    scrollbar = Scrollbar(canvas_informasi, orient="vertical", command=scroll.yview)
    scrollbar.place(x=996, y=0, height=430)

    scroll.config(yscrollcommand=scrollbar.set, height=440, width=1010)

    hari = sekarang.strftime("%A")
    tanggal = sekarang.strftime("%Y-%m-%d")
    waktu = sekarang.strftime("%H:%M")


    #background_image = PhotoImage(file="solarsystem.jpg")

    background_label = Label(scroll.frame, image=get_bg_awal)
    #background_label.place(relwidth=1, relheight=1)
    #background_label.lower()
    
    Label(scroll.frame, text=f"{hari}, {tanggal}", font=("arial", 10), fg="blue",anchor="sw").pack(fill="x")
    Label(scroll.frame, text=f"NAMA KEGIATAN", font=("Times New Roman", 18), fg="blue",anchor="sw").pack(fill="x")
    Label(scroll.frame, text=f"Deadline :", font=("arial", 12), fg="blue",anchor="sw").pack(fill="x")
    Label(scroll.frame, text=f"Sumber :", font=("Times New Roman", 12), fg="blue",anchor="sw").pack(fill="x")
    Label(scroll.frame, text=f"Point 500", font=("arial", 10), fg="blue",anchor="sw").place(x=400,y=0)
    
    Button(scroll.frame, text="Detail", width=70).place(x=0,y=125)
    Label(scroll.frame, text="", height=2).pack()

    Label(scroll.frame, text=f"Point 500", font=("arial", 10), fg="blue",anchor="sw").pack()
    Label(scroll.frame, text=f"{hari}, {tanggal}", font=("arial", 10), fg="blue",anchor="sw").pack(fill="x")
    Label(scroll.frame, text=f"NAMA KEGIATAN", font=("Times New Roman", 18), fg="blue",anchor="sw").pack(fill="x")
    Label(scroll.frame, text=f"Deadline :", font=("arial", 12), fg="blue",anchor="sw").pack(fill="x")
    Label(scroll.frame, text=f"Sumber :", font=("Times New Roman", 12), fg="blue",anchor="sw").pack(fill="x")
    Label(scroll.frame, text=f"Point 500", font=("arial", 10), fg="blue",anchor="sw").place(x=400,y=160)

    Button(scroll.frame, text="Detail", width=70).place(x=0,y=285)
    Label(scroll.frame, text="", height=2).pack()

    Label(scroll.frame, text=f"Point 500", font=("arial", 10), fg="blue",anchor="sw").pack()
    Label(scroll.frame, text=f"{hari}, {tanggal}", font=("arial", 10), fg="blue",anchor="sw").pack(fill="x")
    Label(scroll.frame, text=f"NAMA KEGIATAN", font=("Times New Roman", 18), fg="blue",anchor="sw").pack(fill="x")
    Label(scroll.frame, text=f"Deadline :", font=("arial", 12), fg="blue",anchor="sw").pack(fill="x")
    Label(scroll.frame, text=f"Sumber :", font=("Times New Roman", 12), fg="blue",anchor="sw").pack(fill="x")
    Label(scroll.frame, text=f"Point 500", font=("arial", 10), fg="blue",anchor="sw").place(x=400,y=320)

    Button(scroll.frame, text="Detail", width=70).place(x=0,y=445)
    Label(scroll.frame, text="", height=2).pack()

    Label(scroll.frame, text=f"Point 500", font=("arial", 10), fg="blue",anchor="w").pack()
    Label(scroll.frame, text=f"{hari}, {tanggal}", font=("arial", 10), fg="blue",anchor="sw").pack(fill="x")
    Label(scroll.frame, text=f"NAMA KEGIATAN", font=("Times New Roman", 18), fg="blue",anchor="sw").pack(fill="x")
    Label(scroll.frame, text=f"Deadline :", font=("arial", 12), fg="blue",anchor="sw").pack(fill="x")
    Label(scroll.frame, text=f"Sumber :", font=("Times New Roman", 12), fg="blue",anchor="sw").pack(fill="x")
    Label(scroll.frame, text=f"Point 500", font=("arial", 10), fg="blue",anchor="sw").place(x=400,y=480)

    Button(scroll.frame, text="Detail", width=70).place(x=0,y=700)
    Label(scroll.frame, text="", height=2, width=950).pack()
    canvas_informasi.create_text(0, 0, text="text", font=("Arial", 48), anchor="w")
    ###############################################

    canvas_main2 = Canvas(scroll.frame, width=4, height=5000)
    canvas_main2.place(x=500,y=0)

    Label(canvas_main2, text=f"{hari}, {tanggal}", font=("arial", 10), fg="blue",anchor="sw").pack(fill="x")
    Label(canvas_main2, text=f"NAMA KEGIATAN", font=("Times New Roman", 18), fg="blue",anchor="sw").pack(fill="x")
    Label(canvas_main2, text=f"Deadline :", font=("arial", 12), fg="blue",anchor="sw").pack(fill="x")
    Label(canvas_main2, text=f"Sumber :", font=("Times New Roman", 12), fg="blue",anchor="sw").pack(fill="x")
    Label(canvas_main2, text=f"Point 500", font=("arial", 10), fg="blue",anchor="sw").place(x=400,y=0)

    Label(canvas_main2, height=3).pack()
    Button(canvas_main2, text="Detail", width=70).place(x=0,y=125)

    Label(canvas_main2, text=f"{hari}, {tanggal}", font=("arial", 10), fg="blue",anchor="sw").pack(fill="x")
    Label(canvas_main2, text=f"NAMA KEGIATAN", font=("Times New Roman", 18), fg="blue",anchor="sw").pack(fill="x")
    Label(canvas_main2, text=f"Deadline :", font=("arial", 12), fg="blue",anchor="sw").pack(fill="x")
    Label(canvas_main2, text=f"Sumber :", font=("Times New Roman", 12), fg="blue",anchor="sw").pack(fill="x")
    Label(canvas_main2, text=f"Point 500", font=("arial", 10), fg="blue",anchor="sw").place(x=400,y=160)

    Label(canvas_main2, height=4, width=70).pack()
    Button(canvas_main2, text="Detail", width=70).place(x=0,y=285)


    Label(canvas_main2, text=f"{hari}, {tanggal}", font=("arial", 10), fg="blue",anchor="sw").pack(fill="x")
    Label(canvas_main2, text=f"NAMA KEGIATAN", font=("Times New Roman", 18), fg="blue",anchor="sw").pack(fill="x")
    Label(canvas_main2, text=f"Deadline :", font=("arial", 12), fg="blue",anchor="sw").pack(fill="x")
    Label(canvas_main2, text=f"Sumber :", font=("Times New Roman", 12), fg="blue",anchor="sw").pack(fill="x")
    Label(canvas_main2, text=f"Point 500", font=("arial", 10), fg="blue",anchor="sw").place(x=400,y=320)

    Label(canvas_main2, height=3, width=70).pack()
    Button(canvas_main2, text="Detail", width=70).place(x=0,y=445)

    Label(canvas_main2, text=f"{hari}, {tanggal}", font=("arial", 10), fg="blue",anchor="sw").pack(fill="x")
    Label(canvas_main2, text=f"NAMA KEGIATAN", font=("Times New Roman", 18), fg="blue",anchor="sw").pack(fill="x")
    Label(canvas_main2, text=f"Deadline :", font=("arial", 12), fg="blue",anchor="sw").pack(fill="x")
    Label(canvas_main2, text=f"Sumber :", font=("Times New Roman", 12), fg="blue",anchor="sw").pack(fill="x")
    Label(canvas_main2, text=f"Point 500", font=("arial", 10), fg="blue",anchor="sw").place(x=400,y=480)

    Button(canvas_main2, text="Detail", width=70).place(x=0,y=285)
    Label(canvas_main2, height=3, width=70).pack()
    #image1 = get_post_img1
    #image2 = get_post_img2
    #image3 = get_post_img3
    #image4 = get_post_img4
    #frame_canvas.create_image(56, 300, anchor=tk.NW, image=image1)
    #frame_canvas.create_image(56, 530, anchor=tk.NW, image=image2)
    #frame_canvas.create_image(56, 760, anchor=tk.NW, image=image3)
    #frame_canvas.create_image(56, 990, anchor=tk.NW, image=image4)

def send_chat(x):
    text = x.get()
    create_chat(text)
    print(text)

def create_chat(text):
    global letak_chat
    label_text = Label(canvas_chat, text=text, font=("Arial", 10), fg="black")
    label_text.place(x=20, y=letak_chat[0])
    canvas_chat.create_text(1090, letak_chat, text=text, font=("Arial", 10), anchor="w")
    letak_chat += 20  # Menambahkan jarak antara label-label

def chat():
    global canvas_chat
    global scroll_chat
    global entry_chat
    global letak_chat

    canvas_chat = Canvas(gui, bg="white", width=400, height=790)
    canvas_chat.place(x=1080,y=200)

    scroll_chat = ScrollableCanvas(canvas_chat)
    scroll_chat.pack(side="top", fill="y", expand=True)

    scrollbar_chat = Scrollbar(canvas_chat, orient="vertical", command=scroll_chat.yview)
    scrollbar_chat.place(x=220, y=0, height=430)

    scroll_chat.config(yscrollcommand=scrollbar_chat.set, height=490, width=233)

    entry_chat = Entry(canvas_chat, width=20, fg="black", font=("arial", 12), highlightthickness=10, highlightbackground="white", borderwidth=0)
    entry_chat.place(x="0", y="450")
    send_button = Button(canvas_chat, text="send", command=lambda: send_chat(entry_chat))
    send_button.place(x="200", y="457")

    letak_chat = 0


start_animation()

gui.mainloop()
