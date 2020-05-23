import pyttsx3
from gtts import gTTS
from tkinter import *
from tkinter import filedialog
engine = pyttsx3.init()
David = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-GB_HAZEL_11.0'
engine.setProperty('rate', 150)
engine.setProperty('volume', 1.0)
engine.setProperty('voice', David)

voices={'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0',
        'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-GB_HAZEL_11.0',
        'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN - US_ZIRA_11.0'}

class text_speech_converter():
    filedialog=''
    global content


    def read_template(self,filename):

        with open(filename, 'r', encoding='utf-8') as template_file:
            template_file_content = template_file.read()
            return template_file_content

    def speak(self):
        global content
        content=self.read_template(str(filedialogue))
        print("Jarvis: " + str(content))
        engine.say(str(content))
        engine.runAndWait()

    def make_mp3(self):
        global content
        content = self.read_template(str(filedialogue))
        ttmp3 = gTTS(str(content))
        name_mp3=enter_file_name.get()
        song = ttmp3.save(str(name_mp3)+".mp3")

    def file_dialogue(self):
        global filedialogue, MY_ADDRESS
        filedialogue = filedialog.askopenfilename(initialdir='/', title='select the file',
                                                  filetype=(('text', '*.txt'), ('All Files', '*.*')))
        file = (filedialogue.split('/'))[-1]
        file_name = Label(frame1, text=file, font=('arial', 10), fg='cyan', bg='gray25').grid(row=1, column=2, sticky=E)

convert=text_speech_converter()

#GUI Programming
win=Tk()
win.config(bg='black')
win.title("Text2Speech")

label=Label(win)
label.pack()

frame1=Frame(label,relief=SUNKEN,bg="gray25",bd=10)
frame1.pack()

text_file=Label(frame1,text='Text File:',font=('arial',15,'bold'),fg='cyan',bg='gray25').grid(row=1,column=1,sticky=W)
browse_text_file=Button(frame1,text='Select',bd=5,fg='white',bg='black',font=('arial',15,'bold'),relief=SUNKEN,padx=12,pady=4,command=lambda:convert.file_dialogue())
browse_text_file.grid(row=1,column=2,sticky=W)

play=Button(frame1,text='Play',bd=5,fg='white',bg='black',font=('arial',15,'bold'),relief=SUNKEN,padx=25,pady=4,command=lambda:convert.speak())
play.grid(row=3,column=2,sticky=W)

save_file=Button(frame1,text='Make MP3',bd=5,fg='white',bg='green2',font=('arial',15,'bold'),relief=SUNKEN,padx=4,pady=4,command=lambda:convert.make_mp3())
save_file.grid(row=3,column=2,sticky=E)

file_name=Label(frame1,text='MP3 Name: ',font=('arial',15,'bold'),fg='cyan',bg='gray25').grid(row=2,column=1,sticky=W)
enter_file_name = Entry(frame1,bg='gray14',fg='cyan',font=('arial',15,'bold'),relief=SUNKEN,bd=10)
enter_file_name.grid(row=2,column=2)

win.mainloop()