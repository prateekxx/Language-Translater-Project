from tkinter import *
from tkinter import ttk,messagebox
import googletrans
import textblob
from PIL import ImageTk, Image

root = Tk()
root.title("Translator")
root.geometry("1080x400")
root.resizable(False,False)
root.configure(background = "#f1faee")

def label_change():
    lang_from = combo1.get()
    lang_to = combo2.get()
    label1.configure(text=lang_from)
    label2.configure(text=lang_to)
    root.after(1000,label_change)

def translate_now():
    global language
    try:
        text_in=text1.get(1.0,END)
        lang_to=combo2.get()
        if(text_in):
            words=textblob.TextBlob(text_in)
            lan=words.detect_language()
            for i,j in language.items():
                if(j==lang_to):
                    lang_code= i
            words=words.translate(from_lang=lan,to=str(lang_code))
            text2.delete(1.0,END)
            text2.insert(END,words)
    except Exception as e:
        messagebox.showerror("Translator","Some Error Occured. Please Try Again")

#icon
image_icon = PhotoImage(file = "logo.png")
root.iconphoto(False,image_icon)

#arrow
arrow_image = ImageTk.PhotoImage(Image.open("arrows.png"))
image_label = Label(root,image=arrow_image,width=150)
image_label.place(x=460,y=50)

language = googletrans.LANGUAGES
languageV = list(language.values())
lang1=language.keys()

#first combo box
combo1=ttk.Combobox(root,values=languageV,font="helvetica",state="r")
combo1.place(x=110,y=20)
combo1.set("English")

label1 = Label(root,text = "English", font = "helvetica 30 bold italic", fg = "#f1faee" , bg = "#1D3557", width=18, bd=5,relief=GROOVE)
label1.place(x=10,y=50)

#second combo box
combo2=ttk.Combobox(root,values=languageV,font="helvetica",state="r")
combo2.place(x=730,y=20)
combo2.set("Select Your Language")

label2 = Label(root,text = "English", font = "helvetica 30 bold italic", fg = "#f1faee" , bg = "#1D3557", width=18, bd=5,relief=GROOVE)
label2.place(x=620,y=50)

#first frame
f1 = Frame(root,bg="Black",bd=5)
f1.place(x=10,y=118,width=440,height=210)

text1=Text(f1,font = "helvetica",bg="white",relief=GROOVE,wrap=WORD)
text1.place(x=0,y=0,width=430,height=200)

scrollbar1=Scrollbar(f1)
scrollbar1.pack(side="right",fill="y")

scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=scrollbar1.set)

#second frame
f2 = Frame(root,bg="Black",bd=5)
f2.place(x=620,y=118,width=440,height=210)

text2=Text(f2,font = "helvetica",bg="white",relief=GROOVE,wrap=WORD)
text2.place(x=0,y=0,width=430,height=200)

scrollbar2=Scrollbar(f2)
scrollbar2.pack(side="right",fill="y")

scrollbar2.configure(command=text2.yview)
text2.configure(yscrollcommand=scrollbar2.set)


#translate button
translate = Button(root,text="TRANSLATE",font=("helvetica 13 bold italic"),activebackground="white",cursor="hand2",bd=5,width=10,height=2,bg="#1D3557",fg="white",command=translate_now)
translate.place(x=476,y=250)

label_change()

root.mainloop()