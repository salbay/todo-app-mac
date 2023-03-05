import functions
import PySimpleGUI as sg

label1 = sg.Text("Type in a to-do")
inp_box1 = sg.InputText(tooltip="Enter todo")
button = sg.Button("Add")


window = sg.Window("My To-Do App",layout=[[label1],[inp_box1,button]])
window.read()
window.close()