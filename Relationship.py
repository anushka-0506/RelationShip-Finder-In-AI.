from tkinter import *
from tkinter.ttk import*
import backend
import window2
window = Tk()
window.configure(bg="black")
window.geometry('1050x1500')
style = Style()
style.configure('TButton', font= ('calibri',20,'bold'),borderwidth='4')
style.map('TButton',foreground=[('active','!disabled','red')],
                     background =[('active','black')])
select_tup = NONE                   
def get_selected_row(event):
    try:
        global select_tup
        index=list1.curselection()[0]
        select_tup = list1.get(index)
        e1.delete(0,END)
        e1.insert(END, select_tup[1])
        e2.delete(0,END)
        e2.insert(END, select_tup[2])
        e3.delete(0,END)
        e3.insert(END, select_tup[3])
        
    except IndexError:
        pass


def view_command():
    list1.delete(0,END)
    for row in backend.view():
        list1.insert(END, row)

def search_command():
    list1.delete(0,END)
    for row in backend.search(Name1_text.get(),Name2_text.get()):
        list1.insert(END,row)

def add_Relation():
    backend.insert(Name1_text.get(),Name2_text.get(),Relation_text.get())
    list1.delete(0,END)
    list1.insert(END,(Name1_text.get(),Name2_text.get(),Relation_text.get()))

def delete_Relation():
    backend.delete(select_tup[0])

def update_Relation():
    backend.update(select_tup[0], Name1_text.get(),Name2_text.get(),Relation_text.get())

window.wm_title("Relationship Finder")
#canvas = Canvas(window, width = 300, height = 300)         
img = PhotoImage(file='oo2.png')  
ll=Label(image=img) 
ll.grid(row=1,column=3)   
#canvas.create_image(20,20, anchor=NW, image=img) 
#canvas.grid(row=3,column=2)     

l1 = Label(window, text=" Name 1        ",font= ('helvetica',18,'bold'), background="white")
l1.grid(row=10,column=1,padx=20)

l2 = Label(window, text="Name 2",font= ('helvetica',18,'bold'), background="white")
l2.grid(row=10,column=3,pady=20,padx=20)

l3 = Label(window, text="Relationship",font= ('helvetica',18,'bold'), background="white")
l3.grid(row=11,column=1,padx=20)

Name1_text = StringVar()
e1 = Entry(window, textvariable= Name1_text)
e1.grid(row=10, column=2, padx=50)

Name2_text = StringVar()
e2 = Entry(window, textvariable= Name2_text)
e2.grid(row=10, column=4)

Relation_text = StringVar()
e3 = Entry(window, textvariable= Relation_text)
e3.grid(row=11, column=2)

#isbn_text = StringVar()
#e4 = Entry(window, textvariable= isbn_text)
#e4.grid(row=1, column=3)

list1 = Listbox(window, height=4, width=35)
list1.grid(row=14, column =1, rowspan=6, columnspan=2)

list1.bind("<<ListboxSelect>>", get_selected_row)

sb1 =Scrollbar(window)
sb1.grid(row=14, column=2 ,rowspan = 6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)
# Creating a photoimage object to use image 
photo1 = PhotoImage(file ="3.png") 
  
# Resizing image to fit on button 
photoimage1 = photo1.subsample(13, 13)

b1 =Button(window, text= "View All", width=12,image = photoimage1,compound = LEFT, command=view_command)
b1.grid(row=14, column=3)

photo2 = PhotoImage(file ="search.png") 
  
# Resizing image to fit on button 
photoimage2 = photo2.subsample(13, 13)

b2 =Button(window, text= "Search Relation", width=25,image = photoimage2,compound = LEFT, command=search_command)
b2.grid(row=15, column=3)

photo3 = PhotoImage(file ="add.png") 
  
# Resizing image to fit on button 
photoimage3 = photo3.subsample(13, 13)
b3 =Button(window, text= "Add Relation", width=15,image = photoimage3,compound = LEFT, command=add_Relation)
b3.grid(row=16, column=3)

photo4 = PhotoImage(file ="refresh.png") 
  
# Resizing image to fit on button 
photoimage4 = photo4.subsample(13, 13)

b4 =Button(window, text= "Update", width=25,image = photoimage4,compound = LEFT, command=update_Relation)
b4.grid(row=17, column=3)

photo5 = PhotoImage(file ="4.png") 
  
# Resizing image to fit on button 
photoimage5 = photo5.subsample(13, 13)

b5 =Button(window, text= "Delete", width=12,image=photoimage5,compound = LEFT, command=delete_Relation)
b5.grid(row=18, column=3)

photo6 = PhotoImage(file ="error.png") 
  
# Resizing image to fit on button 
photoimage6 = photo6.subsample(13, 13)

b6 =Button(window, text= "Close", width=25,image=photoimage6, compound = LEFT, command=window.destroy)
b6.grid(row=19, column=3)


window.mainloop()