from tkinter import Label


def show_labels(root):
    input_label = Label(
        root,
        text="Input"
    )
    input_label.grid(
        row=0,
        column=0
    )

    result_label = Label(
        root,
        text="Result"
    )
    result_label.grid(
        row=1,
        column=0
    )