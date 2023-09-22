import functions
import PySimpleGUI as sg
print("git deneme1")
label1 = sg.Text("Type in a to-do")
inp_box1 = sg.InputText(tooltip="Enter todo",key="todo")
button_add = sg.Button("Add")
button_exit = sg.Button("Exit")
button_delete = sg.Button("Delete")
list_box = sg.Listbox(values = functions.get_todos(), key = "todos",
                      enable_events=True,
                      size=[45,10])
edit_button = sg.Button("Edit")
layout= [[label1],[inp_box1,button_add],[list_box,edit_button],[button_exit,button_delete]]
window = sg.Window("My To-Do App",
                   layout=layout,
                   font=("Helvetica",20))

while True:
    event,values = window.read()
    print(1,event)
    print(2,values)
    print(3,values["todos"])
    print(4,values["todo"])

    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values["todo"] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window["todos"].update(values=todos)
        case "Edit":
            inp_box1=values["todos"]
            todo_to_edit = values["todos"][0]
            edited_todo = values["todo"]

            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = edited_todo+"\n"
            functions.write_todos(todos)
            window["todos"].update(values=todos)

        case "Delete":
            print(values["todo"])
            functions.delete_todos(values["todo"])
            window["todos"].update(functions.get_todos())
            print("salimmm")

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