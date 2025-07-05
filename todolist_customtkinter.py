from customtkinter import *
from datetime import *
import time
from tkinter import messagebox


app=CTk()
app.title("ToDo  List")
app.geometry("600x700")
app.maxsize(600,700)
app.minsize(600,700)

# Get date
date_now=datetime.today().date()

#----------functions-------------------------------------------------------
# show time in label and update in 1000m/s
def time_update():
    time_now=time.strftime("%H:%M:%S")
    time_label.configure(text=f'Time: {time_now}')
    app.after(1000,time_update)

#ADD Task in labels-----------------
def add_plans(event=None):
    
    input_box = input_plan.get()
    # erorr 
    if not input_box:
        messagebox.showerror("Error", "Pleas enter somthing")
        return
    
    # labels list
    lis=[plan_label_1,plan_label_2,plan_label_3,plan_label_4,plan_label_5,plan_label_6,plan_label_7]
    for i in lis:

        if i.cget('text') == "":
            i.configure(text=input_plan.get())
            input_plan.delete(0,END)
            continue

# Clear all label--------------------
def clear_all_task():
    lis=[plan_label_1,plan_label_2,plan_label_3,plan_label_4,plan_label_5,plan_label_6,plan_label_7]
    for i in lis:
        i.configure(text="")


#----------row_configure----------------------------------------------------
app.grid_rowconfigure(0,weight=0)
app.grid_rowconfigure(1,weight=0)
app.grid_rowconfigure(2,weight=0)
app.grid_rowconfigure(3,weight=4)
app.grid_rowconfigure(4,weight=0)

#----------column_configure-------------------------------------------------
app.grid_columnconfigure(0,weight=1)
app.grid_columnconfigure(1,weight=1)

#----------Frame-------------------------------------------------------------

fram_date_time=CTkFrame(app,fg_color='#e8f5e9')
fram_date_time.grid(column=0,row=0,columnspan=3,padx=1,pady=1,sticky='nsew')
fram_date_time.grid_columnconfigure((0,1),weight=1)

fram_top_text=CTkFrame(app,height=100,fg_color='#e8f5e9')
fram_top_text.grid(column=0,row=1,columnspan=3,padx=1,pady=1,sticky='nsew')
fram_top_text.grid_columnconfigure((0,1,2),weight=1)         

fram4=CTkFrame(app,fg_color='#66bb8f')
fram4.grid(column=0,row=3,columnspan=2,padx=1,pady=1,sticky='nsew')
fram4.grid_columnconfigure(0,weight=3)
fram4.grid_columnconfigure(1,weight=1)  
fram4.grid_rowconfigure((0,1,2,3,4,5,6,7),weight=1)   

fram5=CTkFrame(app,fg_color='#66bb8f')
fram5.grid(column=0,row=4,columnspan=2,padx=2,pady=1,sticky='nsew')
fram5.grid_columnconfigure(0,weight=1)
fram5.grid_rowconfigure(0,weight=1)
#----------Widget------------------------------------------------------------

# date and Time labels
date_label=CTkLabel(fram_date_time,text=f'Date: {date_now}',corner_radius=2,text_color='black',fg_color='#66bb6a',font=CTkFont(size=20,weight='bold'))
date_label.grid(column=0,row=0,sticky='nsew')

time_label=CTkLabel(fram_date_time,text='',text_color='black',corner_radius=2,fg_color='#66bb6a',font=CTkFont(size=20,weight='bold'))
time_label.grid(column=1,row=0,sticky='nsew')

# Top Text---
top_label=CTkLabel(fram_top_text,text='-------ToDo List-----',text_color='black',width=600,fg_color='#66bb6a',height=40,font=CTkFont(size=35,weight="bold"))
top_label.grid(column=1,row=1,sticky='nsew')

# Input_Entry plan
input_plan=CTkEntry(fram4,width=400,height=3,corner_radius=2,text_color="black",fg_color='#ffffff',font=CTkFont(family='Aria',size=25,weight="bold"),justify=RIGHT,placeholder_text='Please enter your plan')
input_plan.grid(column=0,row=0,columnspan=2,padx=5,pady=5,sticky='nw')
input_plan.bind('<Return>',command=add_plans)

# add button
add_button=CTkButton(fram4,text="ADD",text_color='black',font=CTkFont(family='Aria',size=20,weight="bold"),fg_color='#66bb6a',corner_radius=2,hover_color='#558b2f',width=150,height=40,command=add_plans)
add_button.grid(column=1,row=0,sticky='ne',padx=20,pady=5)

# del button plan label
del_btn_1=CTkButton(fram4,width=80,height=15,corner_radius=1,text="DEL",text_color='black',font=CTkFont(family='Aria',size=18,weight="bold"),hover_color='#558b2f',fg_color='#66bb6a',command=lambda :plan_label_1.configure(text=""))
del_btn_1.grid(column=1,row=1,pady=3,padx=5,sticky='nse')

del_btn_2=CTkButton(fram4,width=80,height=25,corner_radius=1,text="DEL",text_color='black',font=CTkFont(family='Aria',size=18,weight="bold"),hover_color='#558b2f',fg_color='#66bb6a',command=lambda :plan_label_2.configure(text=""))
del_btn_2.grid(column=1,row=2,pady=3,padx=5,sticky='nse')

del_btn_3=CTkButton(fram4,width=80,height=25,corner_radius=1,text="DEL",text_color='black',font=CTkFont(family='Aria',size=18,weight="bold"),hover_color='#558b2f',fg_color='#66bb6a',command=lambda :plan_label_3.configure(text=""))
del_btn_3.grid(column=1,row=3,pady=3,padx=5,sticky='nse')

del_btn_4=CTkButton(fram4,width=80,height=25,corner_radius=1,text="DEL",text_color='black',font=CTkFont(family='Aria',size=18,weight="bold"),hover_color='#558b2f',fg_color='#66bb6a',command=lambda :plan_label_4.configure(text=""))
del_btn_4.grid(column=1,row=4,pady=3,padx=5,sticky='nse')

del_btn_5=CTkButton(fram4,width=80,height=25,corner_radius=1,text="DEL",text_color='black',font=CTkFont(family='Aria',size=18,weight="bold"),hover_color='#558b2f',fg_color='#66bb6a',command=lambda :plan_label_5.configure(text=""))
del_btn_5.grid(column=1,row=5,pady=3,padx=5,sticky='nse')

del_btn_6=CTkButton(fram4,width=80,height=25,corner_radius=1,text="DEL",text_color='black',font=CTkFont(family='Aria',size=18,weight="bold"),hover_color='#558b2f',fg_color='#66bb6a',command=lambda :plan_label_6.configure(text=""))
del_btn_6.grid(column=1,row=6,pady=3,padx=5,sticky='nse')

del_btn_7=CTkButton(fram4,width=80,height=25,corner_radius=1,text="DEL",text_color='black',font=CTkFont(family='Aria',size=18,weight="bold"),hover_color='#558b2f',fg_color='#66bb6a',command=lambda :plan_label_7.configure(text=""))
del_btn_7.grid(column=1,row=7,pady=3,padx=5,sticky='nse')

# plan label text
plan_label_1=CTkLabel(fram4,text="",text_color="black",fg_color='#66bb6a',font=CTkFont(family="Aria",size=25))
plan_label_1.grid(column=0,row=1,sticky='nse',padx=50,pady=3)

plan_label_2=CTkLabel(fram4,text="",text_color="black",fg_color='#66bb6a',font=CTkFont(family="Aria",size=25))
plan_label_2.grid(column=0,row=2,sticky='nse',padx=50,pady=3)

plan_label_3=CTkLabel(fram4,text="",text_color="black",fg_color='#66bb6a',font=CTkFont(family="Aria",size=25))
plan_label_3.grid(column=0,row=3,sticky='nse',padx=50,pady=3)

plan_label_4=CTkLabel(fram4,text="",text_color="black",fg_color='#66bb6a',font=CTkFont(family="Aria",size=25))
plan_label_4.grid(column=0,row=4,sticky='nse',padx=50,pady=3)

plan_label_5=CTkLabel(fram4,text="",text_color="black",fg_color='#66bb6a',font=CTkFont(family="Aria",size=25),)
plan_label_5.grid(column=0,row=5,sticky='nse',padx=50,pady=3)

plan_label_6=CTkLabel(fram4,text="",text_color="black",fg_color='#66bb6a',font=CTkFont(family="Aria",size=25))
plan_label_6.grid(column=0,row=6,sticky='nse',padx=50,pady=3)

plan_label_7=CTkLabel(fram4,text="",text_color="black",fg_color='#66bb6a',font=CTkFont(family="Aria",size=25))
plan_label_7.grid(column=0,row=7,sticky='nse',padx=50,pady=3)

#cleaer all label button
clear_all_btn=CTkButton(fram5,text="CLEAR ALL TASK",text_color='black',font=CTkFont(family='Aria',size=20,weight="bold"),hover_color='#558b2f',fg_color='#66bb6a',command=clear_all_task)
clear_all_btn.grid(column=0,row=1,pady=3,padx=5,sticky='nse')

# calling update time function
time_update()

app.mainloop()
