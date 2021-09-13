from tkinter import Button


def create_btn(root, input_entry, btn_text):
    btn = Button(
        root,
        text=btn_text,
        padx=40,
        pady=20,
        command=lambda: insert_in_entry(input_entry, btn_text)
    )
    return btn


def insert_ans(input_entry, result_entry):
    ans = str(result_entry.get())
    if ans != "":
        if int(float(ans)) == float(ans):
            ans = int(ans)
        else:
            ans = float(ans)
        clear_entry(input_entry, result_entry)
        input_entry.insert(len(input_entry.get()), ans)


def clear_entry(input_entry, result_entry):
    input_entry.delete(0, "end")
    result_entry.delete(0, "end")


def eval_expression(input_entry, result_entry):
    eval_str = str(input_entry.get())
    if eval_str != "":
        result = eval(eval_str)
        result_entry.delete(0, "end")
        if int(float(result)) == float(result):
            result = int(result)
        else:
            result = float(result)
        result_entry.insert(0, result)


def insert_in_entry(input_entry, text_to_insert):
    input_entry.insert(len(input_entry.get()), text_to_insert)
