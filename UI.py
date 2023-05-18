import tkinter as tk
root=tk.Tk()
root.title("LasevIX_'s Raiding Tool")
root.geometry("720x480")
root.resizable(width=False, height=False)
top_navigation=tk.Frame(root,height=64,width=720,background='#0f0f10')
top_navigation.pack()
menu_image=tk.PhotoImage(file="media/menu.png")
menu_button=tk.Button(top_navigation,image=menu_image)
menu_button.pack()

root.mainloop()