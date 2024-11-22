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
	
	# Menu
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
		def buttonEnter(e):
			hoverLabel.place(x=random.randint(10,200),y=random.randint(10,200))

		hoverLabel.place(x=random.randint(10,200),y=random.randint(10,200))
		hoverLabel.bind("<Enter>", buttonEnter)


# Main
root = tk.Tk()
tover(root)
root.mainloop()
