from tkinter import *
from tkinter import ttk,messagebox
import googletrans
import textblob



root=Tk()
root.title("Google trans")
root.geometry("1080*400")


def label_change():
    c=combol.get()
    c1=combol2.get()
    label1.configure(text=c)
    label2.configure(text=c1)
    root.after(1000,label_change)


def translate_now():
    global language
    try:
        text_text1.get(1.0,END)
        c2=combol.get()
        c3=combol2.get()
        if(text_):
            word=textblob.TextBlob(text_)
            lan=words.detect_language()
            for i,j in language.items():
                if(j==c3):
                    lan_=iwords=words.translate(from_lang=lan,to=str(lan_))
                    text2.delete(1.0,END)
                    text2.insert(END,words)
    except Exception as e:
        messagebox.showerror("googletrans","please try again ")
   


#icon
image=PhotoImage(file="google.png")
root.iconphoto(False,image)

arrowi=PhotoImage(file="arrow.png")
image=Label(root,image=arrowi,width=150)
image.place.place(x=460,y=50)

language=googletrans.LANGUAGES
languagev=list(language.value())
lang1=language.keys()

combol=ttk.combobox(root,value=languagev,font="Roboto 14",state="r")
combol.place(x=110,y=20)
combol.set("ENGLISH")

label1=Label(root,text="ENGLISH",font="segoe 30 bold",bg=white,width=18,bd=5,relief=GROOVE)
label1.place(x=10,y=50)

f=Frame(root,bg="Black",bd=5)
f.place(x=10,y=118,width=440,height=210)


text1=Text(f,font="Roboto 20",bg="white",relief=GROOVE,wrap=WORD)
text1.place(x=0,y=0,width=430,height=200)

Scrollbar1=Scrollbar(f)
Scrollbar1.pack(side="right",fill="y")
Scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=Scrollbar1.set)


combol2=ttk.Combobox(root,values=languagev,font="Roboto 14",state="r")
combol2.place(x=730,y=20)
combol2.set("SELECT LANGUAGE")


label2=Label(root,text="ENGLISH" ,font="segos 30 bold",bg="white",width=18,bd=5,relief=GROOVE)
label2.place(x=620,y=50)



f1=Frame(root,bg="Black",bd=5)
f1.place(x=620,y=118,width=440,height=210)


text2=Text(f1,font="Roboto 20",bg="white",relief=GROOVE,wrap=WORD)
text2.place(x=0,y=0,width=430,height=200)

Scrollbar2=Scrollbar(f1)
Scrollbar2.pack(side="right",fill="y")
Scrollbar2.configure(command=text2.yview)
text2.configure(yscrollcommand=Scrollbar2.set)

#trans button 

translate=Button(root,text="Translate",font="Robot 15 bold italic",activebackground="purple",cursor="hand2",bd=5,bg='red',fg="white")
translate.place(x=400,y=250)


label_change()

root.configure(bg="White")
root.mainloop()
