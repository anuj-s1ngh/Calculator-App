from tkinter import Button
from btn_funs import create_btn, clear_entry, insert_ans, eval_expression


def show_btns(root, input_entry, result_entry):
    r = 2
    c = 0
    count = 0
    for i in range(0, 13):
        if c == 3:
            if count == 0:
                plus_operator_btn = create_btn(root, input_entry, "+")
                plus_operator_btn.grid(
                    row=r,
                    column=c
                )
                count += 1
            elif count == 1:
                minus_operator_btn = create_btn(root, input_entry, "-")
                minus_operator_btn.grid(
                    row=r,
                    column=c
                )
                count += 1
            elif count == 2:
                multiply_operator_btn = create_btn(root, input_entry, "*")
                multiply_operator_btn.grid(
                    row=r,
                    column=c
                )
                count += 1
            elif count == 3:
                divide_operator_btn = create_btn(root, input_entry, "/")
                divide_operator_btn.grid(
                    row=r,
                    column=c
                )
            r += 1
            c = 0

        if i < 10:
            num_btn = create_btn(root, input_entry, i)
            num_btn.grid(
                row=r,
                column=c
            )
        elif i == 10:
            decimal_point_btn = create_btn(root, input_entry, ".")
            decimal_point_btn.grid(
                row=r,
                column=c
            )
        elif i == 11:
            clear_btn = Button(
                root,
                text="C",
                padx=40,
                pady=20,
                command=lambda: clear_entry(input_entry, result_entry)
            )
            clear_btn.grid(
                row=r,
                column=c
            )

        c += 1

    
    equal_btn = create_btn(root, input_entry, "(")
    equal_btn.grid(
        row=r+1,
        column=0,
    )

    equal_btn = create_btn(root, input_entry, ")")
    equal_btn.grid(
        row=r+1,
        column=1,
    )

    
    ans_btn = Button(
        root,
        text="ans",
        padx=33,
        pady=20,
        command=lambda: insert_ans(input_entry, result_entry)
    )
    ans_btn.grid(
        row=r+1,
        column=2,
    )


    equal_btn = Button(
        root,
        text="=",
        padx=40,
        pady=20,
        command=lambda: eval_expression(input_entry, result_entry)
    )
    equal_btn.grid(
        row=r+1,
        column=3,
    )
