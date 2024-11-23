#
# Program by Melanie
#

# Importing Modules
import time
import random
import tkinter as tk
from tkinter import ttk


# Classes
class tover():
	def __init__(self,root):
		self.root = root
		self.root.title("Tover")

		self.counter = 0
		self.timeTak = 0
		self.gameTrue = False
		
		self.menu()



	# Menu
	def menu(self):
		for widget in self.root.winfo_children():
			widget.destroy()

		self.root['bg'] = "#aaaaaa"
		nextButton = tk.Button(self.root, text="Play", command=self.inGame)
		nextButton.pack()
		self.counter = 0

		# Display completion time
		timeLab = tk.Label(self.root, text=f'Time completed: {self.timeTak}s')
		timeLab.pack()


	# Game Stuff
	def inGame(self):
		self.gameTrue = True
		self.timeTak = time.time()
		for widget in self.root.winfo_children():
			widget.destroy()
		self.root['bg']= "#bbbbbb"
		
		hoverLabel = tk.Label(self.root, text="Hover!")
		def buttonEnter(e):
			self.counter += 1
			hoverLabel.place(x=random.randint(10,200),y=random.randint(10,200))
			print(self.counter)
			# Game End
			if self.counter >= 10:
				self.timeTak = round(time.time()-self.timeTak, 3)
				self.menu()

		hoverLabel.place(x=random.randint(10,200),y=random.randint(10,200))
		hoverLabel.bind("<Enter>", buttonEnter)
		



# Main
root = tk.Tk()
tover(root)
root.mainloop()
