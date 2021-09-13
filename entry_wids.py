from tkinter import Entry

def show_entries(root):
    input_entry = Entry(
        root,
        width=40,
        borderwidth=2
    )
    input_entry.focus_set()
    input_entry.grid(
        row=0,
        column=1,
        columnspan=3,
        padx=10,
        pady=10
    )

    result_entry = Entry(
        root,
        width=40,
        borderwidth=2
    )
    result_entry.grid(
        row=1,
        column=1,
        columnspan=3,
        padx=10,
        pady=10
    )

    return input_entry, result_entry
