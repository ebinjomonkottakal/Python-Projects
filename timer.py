import time
from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("250x200")
root.title("Timer")
  
hour=StringVar()
minute=StringVar()
second=StringVar()
  
hour.set("00")
minute.set("00")
second.set("00")
  
hour_entry= Entry(root, width=3, font=("Arial",18,""),
                 textvariable=hour)
hour_entry.place(x=60,y=20)
  
minute_entry= Entry(root, width=3, font=("Arial",18,""),
                   textvariable=minute)
minute_entry.place(x=110,y=20)
  
second_entry= Entry(root, width=3, font=("Arial",18,""),
                   textvariable=second)
second_entry.place(x=160,y=20)
  
 
timer_hour=0
timer_min=0
timer_sec=0

def clock():
        try:
            temp = int(hour.get())*3600 + int(minute.get())*60 + int(second.get())
        except:
            print("Please input the right value")
        while temp >-1 and (switch_1['text'] == 'RESET') and (switch_2['text']=='PAUSE') :           
            mins,secs = divmod(temp,60)
            hours=0
            if mins >60:
                hours, mins = divmod(mins, 60)
            hour.set("{0:2d}".format(hours))
            minute.set("{0:2d}".format(mins))
            second.set("{0:2d}".format(secs))
            root.update()
            time.sleep(1)
            if (temp == 0):
                messagebox.showinfo("Timer", "Time's up ")
            temp -= 1
            
            
def start_and_reset():
    if switch_1['text']=='START':
        switch_1['text']='RESET'
        switch_2['text']='PAUSE'
        global timer_hour
        global timer_min
        global timer_sec
        timer_hour = hour.get()
        timer_min = minute.get()
        timer_sec = second.get()
    else:
        switch_1['text'] = 'START'
        hour.set(timer_hour)
        minute.set(timer_min)
        second.set(timer_sec)
        
def pause_button():
    if switch_2["text"]=='PAUSE':
        switch_2['text']='RESUME'
    else:
        switch_2['text']='PAUSE'


switch_1 = Button(root, text = 'START', bd='3',
             command=lambda: [start_and_reset(),clock()])
switch_1.place(x = 80,y = 100)

switch_2 = Button(root, text='PAUSE', bd='3',
             command=lambda: [pause_button(),clock()])
switch_2.place(x = 130,y = 100)
  
root.mainloop()