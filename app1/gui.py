import functions
import PySimpleGUI as sg

label1 = sg.Text("Type in a to-do")
inp_box1 = sg.InputText(tooltip="Enter todo",key="todo")
button = sg.Button("Add")
button_exit = sg.Button("Exit")

window = sg.Window("My To-Do App",
                   layout=[[label1],[inp_box1,button],[button_exit]],
                   font=("Helvetica",20))

while True:
    event,values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values["todo"] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
        case "Exit":
            print("Thank you and good Bye!")
            break
        case sg.WIN_CLOSED:
            break
window.close()