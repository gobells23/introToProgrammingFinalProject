# Sources: Mr. Cozort Datetime: https://www.geeksforgeeks.org/get-current-date-using-python/#:~:text=now(),defined%20under%20the%20DateTime%20module.

# Fridge Project 2022
# 1 Input Item, Category, Expiration Date
# 2 Add Data to a Dictionary
# 3 Import Data to txt file
# 4 Sort Dictionary by Expiration Date
# 5 Visual Component

# using os to create file, using tkinter for window
from tkinter import *
from tkinter import ttk
import uuid
import os
from pathlib import Path
import datetime as dt

#Create an instance of tkinter frame
win = Tk()
#Set the geometry of tkinter frame
win.geometry("750x400")

fridge = []

#Define a function to show a message
# def myclick():
#    message= "Hello "+ fooditem.get()
#    label= Label(frame, text= message, font= ('Times New Roman', 14, 'italic'))
#    fooditem.delete(0, 'end')
#    label.pack(pady=30)

#Creates a Frame
frame = LabelFrame(win, width= 400, height= 180, bd=5)
frame.pack()
#Stop the frame from propagating the widget to be shrink or fit
frame.pack_propagate(False)

#Create an Entry widget in the Frame
fooditem= ttk.Entry(frame, width= 40)
fooditem.insert(INSERT, "Enter Food")
fooditem.pack()
category= ttk.Entry(frame, width= 40)
category.insert(INSERT, "Enter Category")
category.pack()
ExDate= ttk.Entry(frame, width= 40)
ExDate.insert(INSERT, "Enter Expiry Date as mm/dd/yy")
ExDate.pack()

#Define a function to show a message
def add_item():
   # calendar convert date into integer for sorting
   date = str(ExDate.get())
   day = date[3:5]
   month = date[0:2]
   year = date[6:8]
   numdate = int(day) + int(month) * 10 + int(year) * 100
   print(numdate)
   # turn today's date into an integer
   now = dt.date.today()

   todayyear = now.strftime("%Y")
   print("year:", todayyear)

   todaymonth = now.strftime("%m")
   print("month:", todaymonth)

   todayday = now.strftime("%d")
   print("day:", todayday)

   time = now.strftime("%H:%M:%S")
   print("time:", time)

   date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
   print("date and time:",date_time)
   print(todaymonth[0:2])	
   print(todayyear[2:4])
   print(todayday[0:2])
   numtoday = int(todayday[0:2]) + int(todaymonth[0:2]) * 10 + int(todayyear[2:4]) * 100
   print(numtoday)
   # days until ExDate
   print(numdate - numtoday)

   contents = str({"UID":str(uuid.uuid1()), "fooditem": fooditem.get(), "category": category.get(), "ExDate": numdate})
   label = Label(frame, text= contents, font= ('Times New Roman', 9, 'italic'))
   # fooditem.delete(0, 'end')
   label.pack(pady=30)
   # print current working directory
   # print(Path.cwd())
   # change current working directory
   os.chdir('C:/github')
   # print(Path.cwd())
   dirname = "dataFolder"
   # dirname = str(uuid.uuid1())
   type(dirname)
   if os.path.exists('C:/github/dataFolder'):
      print("folder already exists")
   else:
      os.makedirs('C:/github/' + dirname)
   os.chdir('C:/github/' + dirname)
   # print(Path.cwd())

   # instantiate Path and create file
   # up = str(uuid.uuid1())

   p = Path("data.txt")
   print(p.exists(), 'the file exists...')
   # write content into the file...
   # fridge.append({"UID":uuid.uuid1(), "name": fooditem.get(), "ftype": category.get(), "ExDate": ExDate.get()})
   if not p.exists():
      print("the file didn't exist...") 
      p.write_text(contents)
   # p.write_text(ExDate.get())
   else:
      with p.open('a') as f:
         f.write(contents)

   # print(fridge)
   # # p.read_text()

def sort():
   os.chdir('C:/github')
   # print(Path.cwd())
   dirname = "dataFolder"
   # dirname = str(uuid.uuid1())
   type(dirname)
   if os.path.exists('C:/github/dataFolder'):
      print("folder already exists")
   else:
      os.makedirs('C:/github/' + dirname)
   os.chdir('C:/github/' + dirname)
   # print(Path.cwd())
   p = Path("data.txt")
   print(p)
   sortlist = []
   with p.open("r") as f:
         lines = f.readlines()
         # print(type(lines))
         dobject = ""
         for i in lines:
            for l in i:
               if l == '}':
                  print('BANG')
                  dobject+=l
                  sortlist.append(dobject)
                  dobject = ""
               else:
                  dobject += l
   print(sortlist)
   # for i in sortlist:
   #    print(i)
   #    print(i.ExDate)
   #    print(sortlist.index(i))

#Create a Button
# ttk.Button(win, text= "Click", command= myclick).pack(pady=20)
ttk.Button(win, text= "Add Item", command= add_item).pack(pady=20)
ttk.Button(win, text= "Sort", command = sort).pack(pady=20)
win.mainloop()

# turn today's date into an integer
# now = dt.date.today()

# todayyear = now.strftime("%Y")
# print("year:", todayyear)

# todaymonth = now.strftime("%m")
# print("month:", todaymonth)

# todayday = now.strftime("%d")
# print("day:", todayday)

# time = now.strftime("%H:%M:%S")
# print("time:", time)

# date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
# print("date and time:",date_time)
# print(todaymonth[0:2])	
# print(todayyear[2:4])
# print(todayday[0:2])
# numtoday = int(todayday[0:2]) + int(todaymonth[0:2]) * 10 + int(todayyear[2:4]) * 100
# print(numtoday)
