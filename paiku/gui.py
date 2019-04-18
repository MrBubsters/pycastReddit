from paiku import HaikuCast
import tkinter as tk


def cast():
	HaikuCast.cast(HaikuCast.get_data(_n.get(), _sub.get()),_cast.get())


if __name__ == '__main__':
	root = tk.Tk()
	_n = tk.IntVar()
	_sub = tk.StringVar()
	_cast = tk.StringVar()
	tk.Label(root,text='Subreddit:').grid(row=0)
	tk.Label(root,text='Number of Posts:').grid(row=1)
	tk.Label(root,text='Name of ChromeCast').grid(row=2)

	e0 = tk.Entry(root,textvariable=_sub)
	e0.grid(row=0,column=1)
	e1 = tk.Entry(root,textvariable=_n)
	e1.grid(row=1,column=1)
	e2 = tk.Entry(root,textvariable=_cast)
	e2.grid(row=2,column=1)

	button1 = tk.Button(root,text='Cast your favorite subreddit',command=lambda : cast())
	button1.grid(row=3,column=1)
	root.mainloop()
