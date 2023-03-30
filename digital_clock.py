
##importing whole module
from tkinter import *

# importing datetime module to
# retrieve system's time
import datetime

##importing pyglet module
##to style digital clock so that clock
# will look more attractive
import pyglet
pyglet.font.add_file('digital-7.ttf')

##creating tkinter window
##that will output the clock
window = Tk()
window.geometry('430x350')
window.resizable(False, False)
window.configure(bg='black')



##Creating digital clock label and placing them on the tkinter window for:
##hours and minutes
my_label = Label(window, text='', font=('digital-7',120, 'bold'), fg='green', bg='black', pady=100)
my_label.place(relx=0.5, rely=0.5, anchor = CENTER)

##weekday
my_label2 = Label(window, text='', font=('digital-7',14,'bold'), bg='black', fg='green')
my_label2.place(relx=0.7, rely=0.8)

##seconds
my_label3 = Label(window, text='', font=('digital-7',14,'bold'), bg='black', fg='green')
my_label3.place(relx=0.9, rely=0.7)

##am_pm
my_label4 = Label(window, text='', font=('digital-7',12,'bold'), bg='black', fg='green')
my_label4.place(relx=0.9, rely=0.2)


##date_now
my_label5 = Label(window, text='', font=('digital-7',14,'bold'), bg='black', fg='green')
my_label5.place(relx=0.1, rely=0.8)

##Defining the Time and Date function

def time():
    """This function is used to
display time and date on the label"""
    
##constructing time and date text
##by using the format code  
    dt = datetime.datetime.now()
    current = dt.strftime('%I: %M')
    seconds = dt.strftime('%S')
    weekday = dt.strftime('%A')
    am_pm = dt.strftime('%p')
    date_now = dt.strftime('%B, %d, %Y')

##updating the digital clock label with the time and date text constructed
    my_label.configure(text=current)

    my_label2.configure(text=weekday)

    my_label3.configure(text=seconds)

    my_label4.configure(text=am_pm)

    my_label5.configure(text=date_now)
    my_label.after(1000, time)


time()
window.mainloop()
