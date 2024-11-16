#
# Program by Melanie
#

# Importing Modules
import time
import random
import tkinter as tk
from tkinter import ttk


# Functions
def hoveredLabel(label):
	print(label)
	label.place(x=2,y=500)
	time.sleep(1)
	label.destroy()

# Classes
class tover():
	def __init__(self,root):
		self.root = root
		self.root.title("Tover")
		self.menu()
	def menu(self):
		for widget in self.root.winfo_children():
			widget.destroy()
		self.root.configure(bg="#aaaaaa")
		nextButton = tk.Button(self.root, text="Play", command=self.inGame)
		nextButton.pack()
	
	# Game Stuff
	def inGame(self):
		for widget in self.root.winfo_children():
			widget.destroy()
		self.root.configure(bg="#bbbbbb")
		
		hoverLabel = tk.Label(self.root, text="Hover!")
		hoverLabel.place(x=random.randint(1,500),y=random.randint(1,500))
		hoverLabel.bind("<Enter>",self.print())


# Main
root = tk.Tk()
tover(root)
root.mainloop()
