import tkinter
import tkinter.messagebox

from pip import main

class AverageGrade:

    def __init__(self):

        self.main_window = tkinter.Tk()
        #3self.main_window.configure(bg = 'green', fg= 'yellow')
        self.top_frame = tkinter.Frame(self.main_window)
        self.second_frame = tkinter.Frame(self.main_window)
        self.third_frame = tkinter.Frame(self.main_window)
        self.fourth_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)


        # make test 1 label and entry and pack 
        self.test1_label = tkinter.Label(self.top_frame, text = 'Enter the score for test 1: ')
        self.test1_entry = tkinter.Entry(self.top_frame, width = 4)

        self.test1_label.pack(side = 'left')
        self.test1_entry.pack(side = 'left')


        # make test 2 label and entry and pack 
        self.test2_label = tkinter.Label(self.second_frame, text = 'Enter the score for test 2: ')
        self.test2_entry = tkinter.Entry(self.second_frame, width = 4)

        self.test2_label.pack(side = 'left')
        self.test2_entry.pack(side = 'left')

        # make test 3 label and entry and pack 
        self.test3_label = tkinter.Label(self.third_frame, text = 'Enter the score for test 3: ')
        self.test3_entry = tkinter.Entry(self.third_frame, width = 4)

        self.test3_label.pack(side = 'left')
        self.test3_entry.pack(side = 'left')


        # average label
        self.average_label = tkinter.Label(self.fourth_frame, text = 'Average')
        self.average_variable = tkinter.StringVar()
        self.calc_average = tkinter.Label(self.fourth_frame, textvariable= self.average_label)

        self.average_label.pack()
        self.calc_average.pack(side ='left')

        # average and quit button 
        self.average_button = tkinter.Button(self.bottom_frame, text = "Average", command = self.get_average)
        self.quitbutton = tkinter.Button(self.main_window, text= "Quit", command= self.main_window.destroy)


        self.average_button.pack()
        self.quitbutton.pack(side = 'left')

        self.top_frame.pack('top')
        self.second_frame.pack('top')
        self.third_frame.pack('top')
        self.fourth_frame.pack('top')
        self.bottom_frame.pack('bottom')

        tkinter.mainloop()



    def get_average(self):

        test1 = int(self.test1_entry.get())
        test2 = int(self.test2_entry.get())
        test3 = int(self.test3_entry.get())

        average = round(((test1 + test2 + test3) // 3),0)

        self.average_variable.set(average)


my_GUI = AverageGrade()