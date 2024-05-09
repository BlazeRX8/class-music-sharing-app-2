import socket
from threading import Thread
from tkinter import *
from tkinter import ttk
import ftplib
import os
import time
import ntpath #This is used to extract filename from path



from tkinter import filedialog
from pathlib import Path

from playsound import playsound
import pygame
from pygame import mixer

listbox = None

IP_ADDRESS = '127.0.0.1'
PORT = 8080
SERVER = None
BUFFER_SIZE = 4096

global song_counter
song_counter = 0

for file in os.listdir('shared_files'):
    filename = os.fscode(file)
    listbox.insert(song_counter, filename)
    song_counter = song_counter+1

def play():
    global song_selected
    song_selected=listbox.get(ANCHOR)

    pygame
    mixer.init()
    mixer.music.load('shared_files/'+song_selected)
    mixer.music.play()
    if(song_selected != "") :
        infoLabel.configure(text="Now Playing: "+song_selected)
    else:
        infoLabel.configure(text="")
    

PlayButton = Button(window, text = "Play", width=10, bd=1, bg="SkyBlue",font=("Calibri,10"),command=play)
PlayButton.place(x=30,y=200)

def stop():
    global song_selected
    pygame
    mixer.init()
    mixer.music.load('shared_files/'+song_selected)
    mixer.music.pause()
    infoLabel.configure(text="")

Stop = Button(window, text = "Play", width=10, bd=1, bg="SkyBlue",font=("Calibri,10"),command=stop)
Stop.place(x=200,y=200)



