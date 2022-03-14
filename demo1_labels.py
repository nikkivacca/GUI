import tkinter

class MyGUI:

    def __init__(self):
        self.main_window = tkinter.Tk()

## confugure the main window 
        self.main_window.geometry('500x200')
        self.main_window.title('Label Demo')


        self.label1 = tkinter.Label(self.main_window, text = 'Hello World!')
        
        self.label2 = tkinter.Label(self.main_window, text = "This is my GUI program")

## the deafult is top 
## left does side by side (to the left of the next avilable space)
        self.label1.pack(side = 'top')
        self.label2.pack(side = 'bottom')

        tkinter.mainloop()



my_GUI = MyGUI()


## doesnt print until you close or wuit the window that appears due to the mainloop 
print("moving on.....")
