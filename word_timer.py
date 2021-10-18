import tkinter as tk     ## Python 3.x
from tkinter import font

class Timer_Test() :
     def __init__(self, master=None, word_length=4) :
        self.master = master
        self.word_length=word_length
        self.app_font = font.Font(name='Cursor', size=12)
        self.ctr=15
        self.word=""
        self.time_left=tk.IntVar()
        self.start_timer()
        self.init_window()

     def init_window(self):
        self.time_left.set(f"Enter scrabble word of length {self.word_length}\nYou have 15 seconds")
        tk.Label(self.master, textvariable=self.time_left,
                bg="yellow", font=self.app_font).grid(sticky="nsew")
        self.ent=tk.Entry(self.master, bg="lightblue", font=self.app_font)
        self.ent.grid(row=1, column=0)
        tk.Button(self.master, text="Click here to submit word", font=self.app_font,
                 command=self.word_entered, activebackground="LightSalmon2",
                 bg="lightyellow").grid(row=10, column=0, sticky="nsew")
        self.ent.focus_set()

     def word_entered(self):
        """ button calls this function which stores the word entered and quits
        """
        self.word=self.ent.get()
        self.master.quit()
        self.master.destroy()

     def start_timer(self):
        top=tk.Toplevel()
        self.lbl=tk.Label(top, bg="orange", font=self.app_font, width=10)
        self.lbl.grid()
        self.update_timer()

     def update_timer(self):
        self.time_left.set(f"Enter scrabble word of length {self.word_length}\nYou have {self.ctr} seconds")
        self.master.update()
        self.ctr -= 1
        if self.ctr > 0:  ## 10 seconds
            self.master.after(1000, self.update_timer)  ## 1/2 second
        else:             ## time is up
            self.master.quit()
            self.master.destroy()

def get_word(word_length):
    root = tk.Tk()
    app = Timer_Test(root, word_length)
    root.mainloop()
    # print(app.word, app.ctr, "wORD timer")
    return app.word, app.ctr

if __name__ == '__main__':
    get_word()