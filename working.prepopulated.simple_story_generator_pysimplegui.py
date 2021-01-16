#!/usr/bin/python

import PySimpleGUI as sg 

import random
import time
#time.struct_time(tm_year=2020, tm_mon=12, tm_mday=21, tm_hour=9, tm_min=35, tm_sec=36, tm_wday=0, tm_yday=356, tm_isdst=0)

# this sets the global size of the UI
sg.SetOptions(font=('arial', 14))


date = f"day_{time.localtime().tm_mday}_hour{time.localtime().tm_hour}_mon{time.localtime().tm_mon}_{time.localtime().tm_year}"
#######################
#QUESTION: How to properly name the headings of the csv file?
# done: read in a list of values to populate a dropdown
#TODO clean up layout
#TODO make it easier for users to make their own stories.
#TODO set default values for testing purposes
#TODO choose the story line e.g. output1 = simple sentence output2=simple story output3 = diff story
#TODO need to catch if input is empty!
#done get the list from a preloaded .CSV
#TODO update variables
#TODO copy code for updating text lines 88-93
##############################


filenames = ('list_adjectives.txt', "list_places.txt", 'list_sizes.txt','list_things.txt')

# dict filenames and contents of files
# create empty dict
word_dict= {}

for filename in filenames:
    with open(filename) as file:
  #     lines = file.readlines()
        # populated dict with stripped words
        word_dict[filename]=[word.strip() for word in file.readlines()]

print(word_dict)


blank_layout =[
                [sg.T('Please enter your name: '),sg.I(key='-your_name-', size=(15,5))],
                #size adjective
                [sg.T('Pick a size adjective'),sg.Combo(key='-drop-down-size-adjective-',values=word_dict['list_sizes.txt'], size=(15,5))],
                # thing adjective
                [sg.T('Pick an adjective for a thing'),sg.Combo(key='-drop-down-adjectives-things-',values=word_dict['list_adjectives.txt'], size=(15,5))],
                # noun
                [sg.T('Pick a thing'),sg.Combo(key='-drop-down-thing-',values=word_dict['list_things.txt'], size=(15,5))],
                # place
                [sg.T('Pick a place'),sg.Combo(key='-drop-down-place-',values=word_dict['list_places.txt'], size=(15,5))],
                
                
                [sg.T("preview your sentence here: "), sg.T('',key='preview-text', size=(40, 4))],
                [sg.Multiline(size=(40,5),key="-nice-key-")],
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
        window['-nice-key-'].update(output)
        continue
    
        #sentence 2
    if event == 'preview the sentence2':
        #your_name = values["-your_name-"]
        output = f'''Hello {values["-your_name-"]}!\nYou have a {values["-drop-down-size-adjective-"]} {values["-drop-down-adjectives-things-"]} {values["-drop-down-thing-"]} climbing out of your {values["-drop-down-place-"]} .'''
        print(output)
        window['preview-text'].update(output)
        window['-nice-key-'].update(output)
        continue
    #this is the only place I need to declare the variables for printing
    # is there a better way? Probably!
    if event == 'OK':
        
        your_name = values["-your_name-"]
        list_size_adjectives = values["-drop-down-size-adjective-"]
        adjective_things = values["-drop-down-adjectives-things-"]
        list_things= values["-drop-down-thing-"]
        list_places= values["-drop-down-place-"]
        
        if list_size_adjectives not in word_dict['list_sizes.txt']:
            with open('list_sizes.txt','a') as f:
                f.write('\n'+list_size_adjectives)
            newlist= word_dict['list_sizes.txt']
            newlist.append(list_size_adjectives)
            window['-drop-down-size-adjective-'].update(values=newlist)

        if adjective_things not in word_dict['list_sizes.txt']:
            with open('list_adjectives.txt','a') as f:
                f.write('\n'+adjective_things)
            newlist= word_dict['list_adjectives.txt']
            newlist.append(adjective_things)
            window['-drop-down-adjectives-things-'].update(values=newlist)

        if list_places not in word_dict['list_places.txt']:
            with open('list_places.txt','a') as f:
                f.write('\n'+list_places)
            newlist= word_dict['list_places.txt']
            newlist.append(list_places)
            window['-drop-down-place-'].update(values=newlist)

        if list_things not in word_dict['list_places.txt']:
            with open('list_things.txt','a') as f:
                f.write('\n'+list_things)
            newlist= word_dict['list_things.txt']
            newlist.append(list_things)
            window['-drop-down-thing-'].update(values=newlist)

        output = f'Hello {your_name} You have a {values["-drop-down-adjectives-things-"]} {values["-drop-down-size-adjective-"]} {values["-drop-down-thing-"]} in your {values["-drop-down-place-"]}.'
        print(output)

        #write to file
        with open(f"{your_name}.{date}.madlibsout.csv",'a' ) as file :
            try:
                file.write('"'+your_name+'","'+list_size_adjectives+'","'+adjective_things+'","'+list_things+'","'+list_places+'",'+output+'"\n')
            except:
                print("there's a problem here")
                
        print(f'finished writing file {your_name}.{date}.madlibsout.csv')
        sg.PopupOK("This program wrote to the csv file."+output, location=(2000,400) )
        window["-drop-down-adjectives-things-"].update('')
        window["-drop-down-place-"].update('')
        window["-drop-down-size-adjective-"].update('')
        window["-drop-down-thing-"].update('')


window.close()