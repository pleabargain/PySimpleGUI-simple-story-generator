#!/usr/bin/python

import PySimpleGUI as sg 
import random
import time
#time.struct_time(tm_year=2020, tm_mon=12, tm_mday=21, tm_hour=9, tm_min=35, tm_sec=36, tm_wday=0, tm_yday=356, tm_isdst=0)

date = f"day_{time.localtime().tm_mday}_hour{time.localtime().tm_hour}_mon{time.localtime().tm_mon}_{time.localtime().tm_year}"
#######################
#QUESTION: How to properly name the headings of the csv file?
#TODO set default values for testing purposes
#TODO need to catch if input is empty!
##############################


blank_layout =[
                [sg.T('enter your name: '),sg.I(key='-your_name-')],
                
                [sg.T('enter a size adjective: e.g. huge, small,etc.'),sg.I(key='-size-adjective-')],
                [sg.T('Enter an adjective:'),sg.I(key='-adjective-')],
                [sg.T('Enter a thing noun: e.g. dog, fish'),sg.I(key='-noun-')],
                [sg.T('Enter a place noun: e.g. office, home'),sg.I(key='-place-noun-')],    
                [sg.T("preview your sentence here: "), sg.T('',key='preview-text', size=(40, 4))],
                [sg.OK(),sg.Button("preview the sentence1"),sg.Button("preview the sentence2"),sg.Cancel()]
                ]

window = sg.Window('some longer text here at the top of the box with more text', blank_layout,location=(2000,400))

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == 'Cancel':
        break
    if event == 'preview the sentence1':
        #your_name = values["-your_name-"]
        output = f'Hello {values["-your_name-"]}!\nYou have a {values["-size-adjective-"]} {values["-adjective-"]} {values["-noun-"]} in your {values["-place-noun-"]} .'
        print(output)
        window['preview-text'].update(output)
        continue
    # do I need to declare sentence 2 somewhere?
    if event == 'preview the sentence2':
        #your_name = values["-your_name-"]
        output = f'Hello {values["-your_name-"]}!\nThere is a {values["-size-adjective-"]} {values["-adjective-"]} {values["-noun-"]} climbing out of your {values["-place-noun-"]} .'
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
        size_adjective = values["-size-adjective-"]
        adjective = values["-adjective-"]
        noun = values["-noun-"]
        place_noun = values["-place-noun-"]
        output = f'Hello {your_name}!\n You have a {values["-size-adjective-"]} {values["-adjective-"]} {values["-noun-"]} in your {values["-place-noun-"]}.'
        print(output)

        #write to file
        with open(f"{your_name}.{date}.madlibsout.csv",'a' ) as file :
            try:
                file.write('"'+your_name+'","'+size_adjective+'","'+adjective+'","'+noun+'","'+place_noun+'",'+output+'"\n')
            except:
                print("there's a problem here")
                
        print(f'finished writing file {your_name}.{date}.madlibsout.csv')
        sg.PopupOK("Program wrote to the csv file."+output, location=(2000,400) )
        
        #this will clear the input
        window["-size-adjective-"].update('')
        window["-noun-"].update('')
        window["-adjective-"].update('')
        window["-place-noun-"].update('')


window.close()