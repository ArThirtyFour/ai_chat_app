
from tkinter import *
from tkinter import scrolledtext
from open_ai import get_promt

app = Tk()

def main():
    text.delete('1.0',END)
    api_key1 , promt1 , text1 = api_key.get() , promt.get(), request.get()
    try:
        result = get_promt(api_key=api_key1, promt=promt1, text=text1)
    except:
        result = 'Ошибка!'
    finally:
        text.insert(END,result)


app.title('Нейросеть)')
app.geometry('500x900')
app['bg'] = '#78A8E2'
text = scrolledtext.ScrolledText(app , width=60, height=20)
text.grid(column=0 , row=0,padx=5,pady=5)

Label(app,text='Ключ API',bg='#78DBE2',fg='black').grid(column=0,row=1,padx=5,pady=5)
api_key = Entry(app,width=40)
api_key.grid(column=0 , row = 2,padx=5,pady=5)

Label(app,text='Описание',bg='#78DBE2',fg='black').grid(column=0,row=3,padx=5,pady=5)
promt = Entry(app,width=40)
promt.grid(column=0 , row = 4,padx=5,pady=5)

Label(app,text='Что вы хотите?',bg='#78DBE2',fg='black').grid(column=0,row=5,padx=5,pady=5)
request = Entry(app,width=40)
request.grid(column=0 , row = 6,padx=5,pady=5)


Button(app , text='Задать запрос',bd=5,bg='#78DBE2',fg='black',command=main).grid(row=7,column=0,padx=5,pady=10)

app.mainloop()