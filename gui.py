import functions
import PySimpleGUI as sg
import time

sg.theme("DarkBlue")

label_clock = sg.Text("",key="clock")
label1 = sg.Text("Type in a to-do")
inp_box1 = sg.InputText(tooltip="Enter todo",key="todo")
button_add = sg.Button(size=2,image_source="add.png",
                       mouseover_colors="LightBlue2",
                       tooltip="Add Todo",key="Add")
button_exit = sg.Button("Exit")
button_delete = sg.Button("Delete")
list_box = sg.Listbox(values = functions.get_todos(), key = "todos",
                      enable_events=True,
                      size=[45,10])
edit_button = sg.Button("Edit",size=9)
layout= [[label_clock,],[label1],[inp_box1,button_add],[list_box,edit_button],[button_exit,button_delete]]
window = sg.Window("My To-Do App",
                   layout=layout,
                   font=("Helvetica",20))

while True:
    event,values = window.read(timeout=100)
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))

    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values["todo"] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window["todos"].update(values=todos)
        case "Edit":
            try:
                inp_box1=values["todos"]
                todo_to_edit = values["todos"][0]
                edited_todo = values["todo"]
                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = edited_todo+"\n"
                functions.write_todos(todos)
                window["todos"].update(values=todos)
            except IndexError:
                sg.popup("Please select an item first.",font=("Helvetica",20))

        case "Delete":
            try:
                print(values["todos"][0])
                functions.delete_todos(values["todo"])
                window["todos"].update(functions.get_todos())
                print("salimmm")
            except IndexError:
                sg.popup("Please select an item first.", font=("Helvetica", 20))

        case "todos":
            window["todo"].update(value=values["todos"][0])

        case "complete":
            pass

        case "Exit":
            print("Thank you and good Bye!")
            break
        case sg.WIN_CLOSED:
            break
window.close()