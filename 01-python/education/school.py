from PIL import Image, ImageDraw
import PySimpleGUI as sg
import os
import tkinter
import io


def draw_school():
    img=Image.open(os.getcwd()+"/school.jpeg")
    img.thumbnail((1200,800))
    bio=io.BytesIO()
    img.save(bio, format="PNG")

    layout=[[[sg.Text("School:",font=("Arial",25)),],
             [sg.Image(data=bio.getvalue())]],
            [sg.Button("Dont't Show me Anymore")]]

    window =sg.Window("Image",layout, size=(1200,800))

    #Closing the window conditions
    while True:
        event, values=window.read()
        if event == "Don't Show Me Anymore" or sg.WIN_CLOSED:
            break
    window.close()




