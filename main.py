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
		self.menu()
	def menu(self):
		for widget in self.root.winfo_children():
			widget.destroy()
		self.root.configure(bg="#aaaaaa")
		nextButton = tk.Button(self.root, text="Play", command=self.inGame)
		nextButton.pack()
	def inGame(self):
		for widget in self.root.winfo_children():
			widget.destroy()
		self.root.configure(bg="#bbbbbb")

		

# Main
root = tk.Tk()
tover(root)
root.mainloop()
