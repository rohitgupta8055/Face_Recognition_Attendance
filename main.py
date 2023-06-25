from tkinter import *

# for stylish toolkit google entry field
from tkinter import ttk

# for inserting images,for image crop
from PIL import Image,ImageTk

from student import Student


class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0") #for setting display size
        self.root.title("face recognition System") #for display title

        #first image
        img=Image.open(r"C:\Users\gupta\OneDrive\Desktop\Face Recognition System\img_collection\face_img.png")
        img=img.resize((500,130),Image.ANTIALIAS) #antilias higher img ko low level img me convert krta ha
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)

        
        #second image
        img1=Image.open(r"C:\Users\gupta\OneDrive\Desktop\Face Recognition System\img_collection\img_top1.jpeg")
        img1=img1.resize((530,130),Image.ANTIALIAS) #antilias higher img ko low level img me convert krta ha
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=530,height=130)


        #second image 
        img2=Image.open(r"C:\Users\gupta\OneDrive\Desktop\Face Recognition System\img_collection\img_top2.jpg")
        img2=img2.resize((500,130),Image.ANTIALIAS) #antilias higher img ko low level img me convert krta ha
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1030,y=0,width=500,height=130)
        
        
        
        #background image 
        img3=Image.open(r"C:\Users\gupta\OneDrive\Desktop\Face Recognition System\img_collection\back_img.jpg")
        img3=img3.resize((1530,710),Image.ANTIALIAS) #antilias higher img ko low level img me convert krta ha
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710)

        #label name
        title_lbl=Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSYTEM SOFTWARE",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)


        #student button 
        img4=Image.open(r"C:\Users\gupta\OneDrive\Desktop\Face Recognition System\img_collection\std_corner.jpg")
        img4=img4.resize((220,220),Image.ANTIALIAS) #antilias higher img ko low level img me convert krta ha
        self.photoimg4=ImageTk.PhotoImage(img4)
        
        b1=Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=200,y=100,width=220,height=220)


        b1_1=Button(bg_img,command=self.student_details,text="Student Details",font=("times new roman",15,"bold"),bg="dark blue",fg="white",cursor="hand2")
        b1_1.place(x=200,y=300,width=220,height=40)


        #Detect face button 
        img5=Image.open(r"C:\Users\gupta\OneDrive\Desktop\Face Recognition System\img_collection\face_detect.jpg")
        img5=img5.resize((220,220),Image.ANTIALIAS) #antilias higher img ko low level img me convert krta ha
        self.photoimg5=ImageTk.PhotoImage(img5)
        
        b1=Button(bg_img,image=self.photoimg5,cursor="hand2")
        b1.place(x=500,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Detect Face",font=("times new roman",15,"bold"),bg="dark blue",fg="white",cursor="hand2")
        b1_1.place(x=500,y=300,width=220,height=40)


        #Attendace face button 
        img6=Image.open(r"C:\Users\gupta\OneDrive\Desktop\Face Recognition System\img_collection\attendance.png")
        img6=img6.resize((220,220),Image.ANTIALIAS) #antilias higher img ko low level img me convert krta ha
        self.photoimg6=ImageTk.PhotoImage(img6)
        
        b1=Button(bg_img,image=self.photoimg6,cursor="hand2")
        b1.place(x=800,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Attendace",font=("times new roman",15,"bold"),bg="dark blue",fg="white",cursor="hand2")
        b1_1.place(x=800,y=300,width=220,height=40)


        #Help face button 
        img7=Image.open(r"C:\Users\gupta\OneDrive\Desktop\Face Recognition System\img_collection\help.png")
        img7=img7.resize((220,220),Image.ANTIALIAS) #antilias higher img ko low level img me convert krta ha
        self.photoimg7=ImageTk.PhotoImage(img7)
        
        b1=Button(bg_img,image=self.photoimg7,cursor="hand2")
        b1.place(x=1100,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="HelpDesk",font=("times new roman",15,"bold"),bg="dark blue",fg="white",cursor="hand2")
        b1_1.place(x=1100,y=300,width=220,height=40)


        #Train face button 
        img8=Image.open(r"C:\Users\gupta\OneDrive\Desktop\Face Recognition System\img_collection\train.jpg")
        img8=img8.resize((220,220),Image.ANTIALIAS) #antilias higher img ko low level img me convert krta ha
        self.photoimg8=ImageTk.PhotoImage(img8)
        
        b1=Button(bg_img,image=self.photoimg8,cursor="hand2")
        b1.place(x=200,y=400,width=220,height=220)

        b1_1=Button(bg_img,text="Train Data",font=("times new roman",15,"bold"),bg="dark blue",fg="white",cursor="hand2")
        b1_1.place(x=200,y=600,width=220,height=40)



        #Photos face button 
        img9=Image.open(r"C:\Users\gupta\OneDrive\Desktop\Face Recognition System\img_collection\pic.jpeg")
        img9=img9.resize((220,220),Image.ANTIALIAS) #antilias higher img ko low level img me convert krta ha
        self.photoimg9=ImageTk.PhotoImage(img9)
        
        b1=Button(bg_img,image=self.photoimg9,cursor="hand2")
        b1.place(x=500,y=400,width=220,height=220)

        b1_1=Button(bg_img,text="Photos",font=("times new roman",15,"bold"),bg="dark blue",fg="white",cursor="hand2")
        b1_1.place(x=500,y=600,width=220,height=40)


        #developer face button 
        img10=Image.open(r"C:\Users\gupta\OneDrive\Desktop\Face Recognition System\img_collection\developer.png")
        img10=img10.resize((220,220),Image.ANTIALIAS) #antilias higher img ko low level img me convert krta ha
        self.photoimg10=ImageTk.PhotoImage(img10)
        
        b1=Button(bg_img,image=self.photoimg10,cursor="hand2")
        b1.place(x=800,y=400,width=220,height=220)

        b1_1=Button(bg_img,text="Developer",font=("times new roman",15,"bold"),bg="dark blue",fg="white",cursor="hand2")
        b1_1.place(x=800,y=600,width=220,height=40)


        #Exit face button 
        img11=Image.open(r"C:\Users\gupta\OneDrive\Desktop\Face Recognition System\img_collection\exit.png")
        img11=img11.resize((220,220),Image.ANTIALIAS) #antilias higher img ko low level img me convert krta ha
        self.photoimg11=ImageTk.PhotoImage(img11)
        
        b1=Button(bg_img,image=self.photoimg11,cursor="hand2")
        b1.place(x=1100,y=400,width=220,height=220)

        b1_1=Button(bg_img,text="Exit",font=("times new roman",15,"bold"),bg="dark blue",fg="white",cursor="hand2")
        b1_1.place(x=1100,y=600,width=220,height=40)


#======================functions button==================
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

 


if __name__=="__main__": #for calling main
    root=Tk()  #root ko tk se call karna hota ha
    obj=Face_Recognition_System(root) #pass root
    root.mainloop() #main loop close