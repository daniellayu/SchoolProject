from tkinter import *
from PIL import ImageTk, Image


img_adress = "refresh_btn.png"
img_refresh = Image.open(img_adress)
resized = img_refresh.resized((35, 35), Image.Resampling.LANCZOS)
refresh = ImageTK.PhotoImage




#if __name__ == "__main__":
     #o = InsertLesson()
     #o.mainloop()
    #today_date = date.today()
    #print(today_date)
