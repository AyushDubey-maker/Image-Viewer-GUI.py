from tkinter import *
from PIL import ImageTk,Image

root=Tk()
root.title('Image Viewer')

myImage1=ImageTk.PhotoImage(Image.open('ayush_pic.jpg'))
myImage2=ImageTk.PhotoImage(Image.open('chatcord.png'))
myImage3=ImageTk.PhotoImage(Image.open('database.jpg'))
# Resizing the Images in Tkinter
myImage4=Image.open('doc.png')
Image4=myImage4.resize((200,200),Image.ANTIALIAS)  #(width,height)
resizedImage4=ImageTk.PhotoImage(Image4)

# Resizing the Images in Tkinter
myImage5=Image.open('ExcerciseTracker.png')
Image5=myImage5.resize((400,400),Image.ANTIALIAS)
resizedImage5=ImageTk.PhotoImage(Image5)

myImage6=ImageTk.PhotoImage(Image.open('instagram_logo.jpg'))
myImage7=ImageTk.PhotoImage(Image.open('instagram_pic.png'))
myImage8=ImageTk.PhotoImage(Image.open('linkedIn.png'))

# Storing all the images in a ImageList.
image_list=[myImage1,myImage2,myImage3,resizedImage4,resizedImage5,myImage6,myImage7,myImage8]

# Status Bar

status=Label(root,text="Image 1 of "+ str(len(image_list)),bd=1,relief=SUNKEN,anchor=E)

my_label=Label(image=myImage1)
my_label.grid(row=0,column=0,columnspan=3)

# Function to move to next image.
def forward(image_number):
    global my_label
    global button_next
    global button_back
    my_label.grid_forget()
    my_label=Label(image=image_list[image_number-1])
    button_next=Button(root,text="⏩",command=lambda:forward(image_number+1))
    button_back=Button(root,text="⏪",command=lambda: back(image_number-1))
    
    if image_number==8:
        button_next=Button(root,text="⏩",state=DISABLED)

    button_back.grid(row=1,column=0)
    button_next.grid(row=1,column=2)
    my_label.grid(row=0,column=0,columnspan=3)
    status=Label(root,text="Image "+str(image_number)+" of "+ str(len(image_list)),bd=1,relief=SUNKEN,anchor=E)
    status.grid(row=2,column=0,columnspan=3,sticky=W+E)

# Function to move to previous image
def back(image_number):
    global my_label
    global button_next
    global button_back
    my_label.grid_forget()
    my_label=Label(image=image_list[image_number-1])
    button_next=Button(root,text="⏩",command=lambda:forward(image_number+1))
    button_back=Button(root,text="⏪",command=lambda: back(image_number-1))
    if image_number==1:
        button_back=Button(root,text="⏪",state=DISABLED)

    button_back.grid(row=1,column=0)
    button_next.grid(row=1,column=2)
    my_label.grid(row=0,column=0,columnspan=3)
    status=Label(root,text="Image "+str(image_number)+" of "+ str(len(image_list)),bd=1,relief=SUNKEN,anchor=E)
    status.grid(row=2,column=0,columnspan=3,sticky=W+E)
    
# Initial states of all the buttons.    
button_next=Button(root,text="⏩",command=lambda:forward(2))
button_back=Button(root,text="⏪",command=back,state=DISABLED)
button_exit=Button(root,text="Exit App",command=root.quit)

button_back.grid(row=1,column=0)
button_next.grid(row=1,column=2,pady=10)
button_exit.grid(row=1,column=1)
status.grid(row=2,column=0,columnspan=3,sticky=W+E)

root.mainloop()