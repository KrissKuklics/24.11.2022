#1 teksta lauks 2 pogas submit un cancel
import PySimpleGUI as sg

layout = [[sg.T("Vārds", size=(15,1), background_color="white"), sg.InputText()], 
         [sg.Submit(), sg.Cancel()] 


          ]

logs=sg.Window("something", layout, background_color="white")


notikumi, vertibas = logs.read()


logs.close()

if notikumi == "Submit":
    try:
        vards = input("Faila nosaukums:")
        file=open(vards,"r+")
        
    except FileNotFoundError:
        file=open(vards, "w+")
        
    dati = vertibas.values()
    text="\n".join(dati)
    file.write(text)
    
    file.close()            

