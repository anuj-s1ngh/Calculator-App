from tkinter import *
from entry_wids import show_entries
from btn_wids import show_btns
from label_wids import show_labels


root = Tk()
root.title("Calculator App")
root.iconbitmap("icon-calculator-24.ico")


show_labels(root)

input_entry, result_entry = show_entries(root)

show_btns(root, input_entry, result_entry)

root.mainloop()
