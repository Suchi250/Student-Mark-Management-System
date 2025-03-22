#import tkinter
#print(dir(tkinter))
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import csv
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

from pymysql import *
conobj=connect(host='localhost',user='root',password='Suchi@867')
curobj=conobj.cursor()
curobj.execute('use project;')

root1=Tk()#Tk is used to create a window Tk is a class
#------------------------------------------------------------------------------------

def AdminLogin():
	root1.destroy()
	Aroot=Tk()
#-------------------------------------------------------------------------------
	def ALogin():
		#print(AUser.get(),APwd.get())
		r='select * from Admin where Username="{}" and APwd="{}";' .format(AUser.get(),APwd.get())
		curobj.execute(r)
		record=curobj.fetchall()
		if len(record):
			messagebox.showinfo("valid","Welcome To Admin Operation Page")
			Aroot.destroy()
			Aroot2=Tk()
			#----------------------------------------------------------------------
			def Certificate():
					global file_path1
					global file_path2
					global file_path3
			#----------------------------------------------------------------------------------------------------
					fobj=open("Attendance.csv","r")
					cobj=csv.reader(fobj)
					Regnolist,AugTotal, AugPre,SepTotal,SepPre=[],[],[],[],[]
					for data in cobj:
							Regnolist.append(data[0])
							AugTotal.append(data[1])
							AugPre.append(data[2])
							SepTotal.append(data[3])
							SepPre.append(data[4])
	
					if str(Regno.get()) in Regnolist:
							index=Regnolist.index(str(Regno.get()))
							#print(AugTotal[index],AugPre[index])
					sub1,sub2,sub3=[],[],[]
					fobj1=open("ClassTest.csv","r")
					cobj1=csv.reader(fobj1)
					for mark in cobj1:
						sub1.append(mark[1])
						sub2.append(mark[2])
						sub3.append(mark[3])
		
					Isub1,Isub2,Isub3=[],[],[]
					fobj2=open("Internal.csv","r")
					cobj2=csv.reader(fobj2)
					for mark in cobj2:
						Isub1.append(mark[1])
						Isub2.append(mark[2])
						Isub3.append(mark[3])


					
					#------------------------------------------------------------------------------------------
					fname=Regno.get()
					pdffile="fname.pdf"
					c=canvas.Canvas(pdffile,pagesize=letter)
					c.setFont("Helvetica",15)
					c.drawString(250,700,"Student Report Card")
					c.setFont("Helvetica",15)
					c.drawString(50,620,"Student Regno:"+str.rjust (Regno.get(),15))
					c.drawString(50,600,"Student name:"+ str.rjust(Sname.get(),15))
					c.drawString(50,580,"Academic year:"+ str.rjust(Acyear.get(),15))
					c.drawString(50,560,"Student dept Name:"+str.rjust(Dept.get(),15))

					c.setFont("Helvetica",15)
					c.drawString(250,510,"Attendance Report Card")
					c.setFont("Helvetica",12)
					c.drawString(50,470,"Month Name" + str.rjust("Total number of class",30)+ str.rjust("Total number present",30))
					c.drawString(50,450,"August" + str.rjust(AugTotal[index],30)+ str.rjust(AugPre[index],30))
					c.drawString(50,430,"September" + str.rjust(SepTotal[index],30)+ str.rjust(SepPre[index],30))

					c.setFont("Helvetica",15)
					c.drawString(250,400,"Class Test  Report")
					c.setFont("Helvetica",12)
					c.drawString(50,380,"Subject name" + str.rjust("Total class mark",30)+ str.rjust("Total Secure mark",30))
					c.drawString(50,360,"Math" + str.rjust("15",30)+ str.rjust(sub1[index],30))
					c.drawString(50,340,"phy" + str.rjust("15",30)+ str.rjust(sub2[index],30))
					c.drawString(50,320,"che" + str.rjust("15",30)+ str.rjust(sub3[index],30))

					c.setFont("Helvetica",15)
					c.drawString(250,290,"Internal Test Report")
					c.setFont("Helvetica",12)
					c.drawString(50,270,"Subject name" + str.rjust("Total Internal mark",30)+ str.rjust("Total Secure mark",30))
					c.drawString(50,250,"Math" + str.rjust("20",35)+ str.rjust(Isub1[index],30))
					c.drawString(50,230,"phy" + str.rjust("20",35)+ str.rjust(Isub2[index],30))
					c.drawString(50,210,"che" + str.rjust("20",35)+ str.rjust(Isub3[index],30))

					c.setFont("Helvetica",10)
					c.drawString(50,110,"Date" + str.rjust("Principal Signature ",150))

					




	
					c.save()
					print(Regno.get(),Sname.get(),Acyear.get(),Dept.get())
					
					messagebox.showinfo("Certificate Create")
					Aroot2.destroy()
			#---------------------------------------------------------------------------
			def Reset():
					Regno.delete(0,END)
					Sname.delete(0,END)
					Acyear.set("select Acc year")
					Dept.set("select Dept name")
			#---------------------------------------------------------------------------
			def Attendance():
					global file_path1
					file_path1=filedialog.askopenfilename(defaultextension=".csv",filetypes=[("CSV files","*.csv")])
					fobj1=open(file_path1,"r")
					cobj1=csv.reader(fobj1)
					
			#---------------------------------------------------------------------------
			def ClassTest():
					global file_path2
					file_path2=filedialog.askopenfilename(defaultextension=".csv",filetypes=[("CSV files","*.csv")])
					fobj2=open(file_path2,"r")
					cobj1=csv.reader(fobj2)
					

	
			#------------------------------------------------------------------------------
			def Internal():
					global file_path3
					file_path3=filedialog.askopenfilename(defaultextension=".csv",filetypes=[("CSV files","*.csv")])
					fobj3=open(file_path3,"r")
					cobj1=csv.reader(fobj3)
					

			#------------------------------------------------------------------------------------
			def Exit():
					Aroot2.destroy()
			
			Aroot2.maxsize(500,500)
			Aroot2.minsize(500,500)
			Aroot2.title("Admin Operation Page")
			Aroot2.configure(bg="#84fc03")
			#-------------------------------------------------------------------------------------------------
			Label(Aroot2,text="Student Reg. No.",font=('Constantia',15),relief="groove",width=17,height=1,fg="black",bg="#800080").place(x=35,y=50)
			Regno=Entry(Aroot2,font=("Constantia",15),relief="sunken",width=16)
			Regno.place(x=280,y=50)
	
			Label(Aroot2,text="Student Name",font=('Constantia',15),relief="groove",width=17,height=1,fg="black",bg="#800080").place(x=35,y=100)
			Sname=Entry(Aroot2,font=("Constantia",15),relief="sunken",width=16)
			Sname.place(x=280,y=100)

			Label(Aroot2,text="Student Academic Year",font=('Constantia',15),relief="groove",width=17,height=1,fg="black",bg="#800080").place(x=35,y=150)
			Acyear=StringVar()
			Acyear.set("Select Academic Year")
			OM1=OptionMenu(Aroot2,Acyear,"2020-2024","2021-2025","2022-2026","2023-2027","2024-2028","2025-2029")
			OM1.place(x=290,y=150)
	
			Label(Aroot2,text="Student Dept Name",font=('Constantia',15),relief="groove",width=17,height=1,fg="black",bg="#800080").place(x=35,y=200)
			Dept=StringVar()
			Dept.set("Select Dept Name")
			OM2=OptionMenu(Aroot2,Dept,"CSE","CIVIL","ME","EEE","ECE","SCE-IT","CS","Bsc-ITM","BCA","CSE-AI")
			OM2.place(x=300,y=200)

			Label(Aroot2,text="upload Attendance File",font=('Constantia',15),relief="groove",width=17,height=1,fg="black",bg="#800080").place(x=35,y=250)
			Button (Aroot2,text="Select Attendance file",font=('Constantia',12),relief="groove",width=18,height=1,fg="black",command=Attendance).place(x=285,y=250)
	
			Label(Aroot2,text="Upload class Test file",font=('Constantia',15),relief="groove",width=17,height=1,fg="black",bg="#800080").place(x=35,y=300)
			Button (Aroot2,text="Select Class Test file",font=('Constantia',12),relief="groove",width=18,height=1,fg="black",command=ClassTest).place(x=285,y=300)
	
			Label(Aroot2,text="Upload Internal test file",font=('Constantia',15),relief="groove",width=18,height=1,fg="black",bg="#800080").place(x=35,y=350)
			Button (Aroot2,text="Select Internal Test file",font=('Constantia',12),relief="groove",width=18,height=1,fg="black",command=Internal).place(x=285,y=350)
	
			Button (Aroot2,text="Certificate",font=('Constantia',12),relief="groove",command=Certificate,width=12,height=1,fg="black",bg="green").place(x=35,y=410)
			
			Button (Aroot2,text="Reset",font=('Constantia',12),relief="groove",command=Reset,width=12,height=1,fg="black",bg="green").place(x=190,y=410)

			Button (Aroot2,text="Exit",font=('Constantia',12),relief="groove",command=Exit,width=12,height=1,fg="black",bg="green").place(x=340,y=410)






			Aroot2.mainloop()
		else:
			messagebox.showinfo("invalid","Given username & password invalid")
			Aroot.destroy()
#-----------------------------------------------------------------------
	def AExit():
		Aroot.destroy()
#---------------------------------------------------------------------------
	Aroot.maxsize(500,500)
	Aroot.minsize(500,500)#it set the height and width of the window
	Aroot.title("Admin Login Page")#it  set the title of window
	Aroot.configure(bg="#84fc03")#it set the admin login window background color.
	
	Label(Aroot,text="Admin UserName",font=('Constantia',15),relief="groove",width=17,height=1,fg="black",bg="#800080").place(x=35,y=50)
	AUser=Entry(Aroot,font=("Constantia",15),relief="sunken",width=16)
	AUser.place(x=280,y=50)
	
	Label(Aroot,text="Admin Password",font=('Constantia',15),relief="groove",width=17,height=1,fg="black",bg="#800080").place(x=35,y=100)
	APwd=Entry(Aroot,font=("Constantia",15),relief="sunken",width=16,show="*")
	APwd.place(x=280,y=100)

	Button(Aroot,text="Login",font=("Franklin Gothic",20),width=10,height=1,bd=4,bg="green",fg="black",activebackground="#ffbeee",relief="raised", command=ALogin).place(x=35,y=200)#command is used to active the button
	
	Button(Aroot,text="Exit",font=("Franklin Gothic",20),width=10,height=1,bd=4,bg="red",fg="black",activebackground="#ffbeee",relief="raised",command=AExit).place(x=250,y=200)#command is used to active the button


	
	




	Aroot.mainloop()
#....................................
def StudentLogin():
	root1.destroy()
	Sroot1=Tk()
	Sroot1.maxsize(500,600)
	Sroot1.minsize(500,600)
	Sroot1.title("Student Login Page")
	Sroot1.configure(bg="#84fc03")
	Label(Sroot1,text="Student Reg. No.",font=('Constantia',15),relief="groove",width=17,height=1,fg="black",bg="#800080").place(x=35,y=50)
	Entry(Sroot1,font=("Constantia",15),relief="sunken",width=16).place(x=280,y=50)
	
	Label(Sroot1,text="Student Name",font=('Constantia',15),relief="groove",width=17,height=1,fg="black",bg="#800080").place(x=35,y=100)
	Entry(Sroot1,font=("Constantia",15),relief="sunken",width=16).place(x=280,y=100)

	Label(Sroot1,text="Student Academic Year",font=('Constantia',15),relief="groove",width=17,height=1,fg="black",bg="#800080").place(x=35,y=150)
	Acyear=StringVar()
	Acyear.set("Select Academic Year")
	OM1=OptionMenu(Sroot1,Acyear,"2020-2024","2021-2025","2022-2026","2023-2027","2024-2028","2025-2029")
	OM1.place(x=290,y=150)
	
	Label(Sroot1,text="Student Dept Name",font=('Constantia',15),relief="groove",width=17,height=1,fg="black",bg="#800080").place(x=35,y=200)
	Dept=StringVar()
	Dept.set("Select Dept Name")
	OM2=OptionMenu(Sroot1,Dept,"CSE","CIVIL","ME","EEE","ECE","SCE-IT","CS","Bsc-ITM","BCA","CSE-AI")
	OM2.place(x=300,y=200)
	

	Label(Sroot1,text="Password",font=('Constantia',15),relief="groove",width=17,height=1,fg="black",bg="#800080").place(x=35,y=250)
	Entry(Sroot1,font=("Constantia",15),relief="sunken",width=16,show="*").place(x=280,y=250)

	Button(Sroot1,text="Login",font=("Franklin Gothic",20),width=10,height=1,bd=4,bg="green",fg="black",activebackground="#ffbeee",relief="raised").place(x=35,y=350)#command is used to active the button
	
	Button(Sroot1,text="Exit",font=("Franklin Gothic",20),width=10,height=1,bd=4,bg="red",fg="black",activebackground="#ffbeee",relief="raised").place(x=250,y=350)#command is used to active the button










	Sroot1.mainloop()

#------------------------------------------------------------------------------------
#root1.geometry('600x400')
root1.maxsize(500,500)
root1.minsize(500,500)#it set the height and width of the window
root1.title("Home Page")#it set the title of the window
root1.configure(bg="#84fc03")

Button(root1,text="Admin Login",font=("Franklin Gothic",20),width=16,height=1,bd=4,bg="#800080",fg="black",activebackground="#ffbeee",relief="raised",command=AdminLogin).place(x=120,y=125)#command is used to active the button

Button(root1,text="Student Login",font=("Franklin Gothic",20),width=16,height=1,bd=4,bg="#800080",fg="black",activebackground="#ffbeee",relief="raised",command=StudentLogin).place(x=120,y=250)



root1.mainloop()#it is also used for create a window

