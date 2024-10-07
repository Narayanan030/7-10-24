import tkinter as tk
from tkinter import ttk

LARGEFONT =("Verdana", 35)

class tkinterApp(tk.Tk):
	def __init__(self, *args, **kwargs): 
		tk.Tk.__init__(self, *args, **kwargs)
		container = tk.Frame(self) 
		container.pack(side = "top", fill = "both", expand = True) 
		container.grid_rowconfigure(0, weight = 1)
		container.grid_columnconfigure(0, weight = 1)
		self.frames = {} 
		for F in (StartPage, Page1):
			frame = F(container, self)
			self.frames[F] = frame 
			frame.grid(row = 0, column = 0, sticky ="nsew")
		self.show_frame(StartPage)
	def show_frame(self, cont):
		frame = self.frames[cont]
		frame.tkraise()
class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        user_lb=tk.Label(self,text="username")
        pswd_lb=tk.Label(self,text="password")
        user_entry=tk.Entry(self)
        pswd_entry=tk.Entry(self)
        user_lb.grid(row=0, column=0, padx=10, pady=5, sticky="E")
        user_entry.grid(row=0, column=1, padx=10, pady=5)
        pswd_lb.grid(row=1, column=0, padx=10, pady=5, sticky="E")
        pswd_entry.grid(row=1, column=1, padx=10, pady=5)
        button1 = ttk.Button(self, text ="login",command = lambda : controller.show_frame(Page1))
        button1.grid(row = 2, column = 1, padx = 10, pady = 10)

class Page1(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text ="Hi!!", font = LARGEFONT)
        label.grid(row = 0, column = 1, padx = 10, pady = 5)
        label = ttk.Label(self, text ="Welcome...", font = LARGEFONT)
        label.grid(row = 1, column = 1, padx = 10, pady = 5)
        button1 = ttk.Button(self, text ="back",command = lambda : controller.show_frame(StartPage))
        button1.grid(row = 2, column = 1, padx = 10, pady = 5)

app = tkinterApp()
app.mainloop()
