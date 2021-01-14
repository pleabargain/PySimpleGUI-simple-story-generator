#!/usr/bin/python

import PySimpleGUI as sg 
import random
import time
#time.struct_time(tm_year=2020, tm_mon=12, tm_mday=21, tm_hour=9, tm_min=35, tm_sec=36, tm_wday=0, tm_yday=356, tm_isdst=0)

date = f"day_{time.localtime().tm_mday}_hour{time.localtime().tm_hour}_mon{time.localtime().tm_mon}_{time.localtime().tm_year}"
#######################
#QUESTION: How to properly name the headings of the csv file?
# done: read in a list of values to populate a dropdown
#TODO clean up layout
#TODO make it easier for users to make their own stories.
#TODO set default values for testing purposes
#TODO choose the story line e.g. output1 = simple sentence output2=simple story output3 = diff story
#TODO need to catch if input is empty!
#TODO get the list from a preloaded .CSV
##############################
#lists for dropdowns
list_size_adjectives = list(['tiny','huge']) #-drop-down-size-adjective-
list_adjectives_things = list(['slow','fast','syrupy']) #-drop-down-adjectives-things-
list_things = list(['cat','dog','fish','whale','computer','pencil']) # -drop-down-thing-
list_places = list(['hospital','office']) # -drop-down-place-



blank_layout =[
                [sg.T('Please enter your name: '),sg.I(key='-your_name-', size=(15,5))],
                #size adjective
                [sg.T('Pick a size adjective'),sg.Combo(key='-drop-down-size-adjective-',values=list_size_adjectives, size=(15,5))],
                # thing adjective
                [sg.T('Pick an adjective for a thing'),sg.Combo(key='-drop-down-adjectives-things-',values=list_adjectives_things, size=(15,5))],
                # noun
                [sg.T('Pick a thing'),sg.Combo(key='-drop-down-thing-',values=list_things, size=(15,5))],
                # place
                [sg.T('Pick a place'),sg.Combo(key='-drop-down-place-',values=list_places, size=(15,5))],
                
                
                [sg.T("preview your sentence here: "), sg.T('',key='preview-text', size=(40, 4))],
                [sg.OK(),sg.Button("preview the sentence1"),sg.Button("preview the sentence2"),sg.Cancel()]
                ]

window = sg.Window('Welcome to your basic sentence generator.', blank_layout,location=(2000,400))

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == 'Cancel':

        break
        #sentence 1
    if event == 'preview the sentence1':
        #your_name = values["-your_name-"]
        output = f'''Hello {values["-your_name-"]}!\nYou have a {values["-drop-down-size-adjective-"]} {values["-drop-down-adjectives-things-"]} {values["-drop-down-thing-"]} in your {values["-drop-down-place-"]} .'''
        print(output)
        window['preview-text'].update(output)
        continue
    
        #sentence 2
    if event == 'preview the sentence2':
        #your_name = values["-your_name-"]
        output = f'''Hello {values["-your_name-"]}!\nYou have a {values["-drop-down-size-adjective-"]} {values["-drop-down-adjectives-things-"]} {values["-drop-down-thing-"]} climbing out of your {values["-drop-down-place-"]} .'''
        print(output)
        window['preview-text'].update(output)
        continue
    #this is the only place I need to declare the variables for printing
    # is there a better way? Probably!
    if event == 'OK':
        # print("this will prod keys: ", values.keys())
        # print("this will prod values: ", values.values())
        # print("this will prod items key,value pair tuple wrapped with parens: ",values.items())
        your_name = values["-your_name-"]
        list_size_adjectives = values["-drop-down-size-adjective-"]
        adjective_things = values["-drop-down-adjectives-things-"]
        list_things= values["-drop-down-thing-"]
        list_places= values["-drop-down-place-"]
        
        output = f'Hello {your_name} You have a {values["-drop-down-adjectives-things-"]} {values["-drop-down-size-adjective-"]} {values["-drop-down-thing-"]} in your {values["-drop-down-place-"]}.'
        print(output)

        #write to file
        with open(f"{your_name}.{date}.madlibsout.csv",'a' ) as file :
            try:
                file.write('"'+your_name+'","'+list_size_adjectives+'","'+adjective_things+'","'+list_things+'","'+list_places+'",'+output+'"\n')
            except:
                print("there's a problem here")
                
        print(f'finished writing file {your_name}.{date}.madlibsout.csv')
        sg.PopupOK("Program wrote to the csv file."+output, location=(2000,400) )
        #print({f'{your_name}.{date}.madlibsout.csv')
        window["-drop-down-size-adjective-"].update('')
        window["-drop-down-adjectives-things-"].update('')
        window["-drop-down-thing-"].update('')
        #window["-adjective-"].update('')
        window["-drop-down-place-"].update('')


window.close()