import PySimpleGUI as sg
import pandas as pd

'''
'rated', 'created_at', 'last_move_at', 'turns', 'victory_status', 'increment_code',
         'white_rating', 'black_rating', 'opening_eco', 'opening_ply'
'''
#sg.theme_previewer()
sg.theme('DarkTeal6')
layout = [
    [sg.Text("Fill out the following fields and click predict when done")],
    
    [sg.Text("Was the game rated? (true/false)")],
    [sg.Input(key="rated")],

    [sg.Text("What time was the game created? (24 hour format ex. 14:43)")],
    [sg.Input(key="created_at")],

    [sg.Text("What time was the last move played? (24 hour format)")],
    [sg.Input(key="last_move_at")],

    [sg.Text("How many turns did the game last?")],
    [sg.Input(key="turns")],

    [sg.Text("How was the game won? (resign, outoftime, or mate)")],
    [sg.Input(key="victory_status")],

    [sg.Text("What increment was played?")],
    [sg.Input(key="increment_code")],

    [sg.Text("What was white's rating?")],
    [sg.Input(key="white_rating")],

    [sg.Text("What was black's rating?")],
    [sg.Input(key="black_rating")],

    [sg.Text("What was the ECO of the opening?")],
    [sg.Input(key="opening_eco")],

    [sg.Text("How many moves were in the opening? (opening ply)")],
    [sg.Input(key="opening_ply")],

    [sg.Button('print')]
]

window = sg.Window("Chess Winner Predictor", layout)

inp = pd.DataFrame()
exit = False
while not exit:
    event, values = window.read()
    print(values)
    if event == sg.WINDOW_CLOSED or event == "Quit":
        exit = True
    
    inp['rated'] =          [bool(values['rated'])]
    inp['created_at'] =     [str(values['created_at'])]
    inp['last_move_at'] =   [str(values['last_move_at'])]
    inp['turns'] =          [int(values['turns'])]
    inp['victory_status'] = [str(values['victory_status'])]
    inp['increment_code'] = [str(values['increment_code'])]
    inp['white_rating'] =   [int(values['white_rating'])]
    inp['black_rating'] =   [int(values['black_rating'])]
    inp['opening_eco'] =    [str(values['opening_eco'])]
    inp['opening_ply'] =    [int(values['opening_ply'])]

    if event == 'print':
        print(inp)


window.close()




# import PySimpleGUI as sg

# # Define the window's contents
# layout = [[sg.Text("What's your name?")],
#           [sg.Input(key='-INPUT-')],
#           [sg.Text(size=(40,1), key='-OUTPUT-')],
#           [sg.Button('Ok'), sg.Button('Quit')]]

# # Create the window
# window = sg.Window('Window Title', layout)

# # Display and interact with the Window using an Event Loop
# while True:
#     event, values = window.read()
#     # See if user wants to quit or window was closed
#     if event == sg.WINDOW_CLOSED or event == 'Quit':
#         break
#     # Output a message to the window
#     window['-OUTPUT-'].update('Hello ' + values['-INPUT-'] + "! Thanks for trying PySimpleGUI")

# # Finish up by removing from the screen
# window.close()