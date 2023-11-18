import PySimpleGUI as sg
import hashlib as hash
import os
from pydub import AudioSegment
from pydub.playback import play
from pydub import effects as e

samples = {}

def hashToCol(input):
    h = hash.md5(input.encode())
    return "#" + str(h.hexdigest())[0:6]

def addSound(key, file):
    if not os.path.isfile(file):
        print("Error: No such file found: " + file)
        return
    samples[key] = AudioSegment.from_wav(file)

def playSound(key):
    play(samples[key])

view = []
def generateButtons(perRow):
    row = []
    currentRow = 0
    keys = list(samples.keys())
    numSamples = len(samples.keys())
    print("number of samples : " + str(numSamples))
    i = 0
    while i < numSamples:
        if i - currentRow*perRow >= perRow:
            view.append(row)
            row = []
            currentRow += 1
        bt = sg.Button(keys[i], key=keys[i], font =('Arial Bold', 16), size = (int(142/perRow), 7), button_color=hashToCol(keys[i]))
        row.append(bt)
        i += 1
    view.append(row)

### Add Sounds here like this
addSound("Sound 1", "1.wav")
addSound("Sound 2", "1.wav")
addSound("Sound 3", "1.wav")
addSound("Sound 4", "1.wav")
addSound("Sound 5", "1.wav")
addSound("Sound 6", "1.wav")
addSound("Sound 7", "1.wav")
addSound("Sound 8", "1.wav")
addSound("Sound 9", "1.wav")
addSound("Sound 10", "1.wav")
addSound("Sound 11", "1.wav")
addSound("Sound 12", "1.wav")
addSound("Sound 13", "1.wav")
addSound("Sound 14", "1.wav")
addSound("Sound 15", "1.wav")
addSound("Sound 16", "1.wav")
addSound("Sound 17", "1.wav")
addSound("Sound 18", "1.wav")
addSound("Sound 19", "1.wav")
addSound("Sound 20", "1.wav")

generateButtons(6)
# Create window
window = sg.Window(title="Soundboard", layout=view, resizable=True).Finalize()
window.maximize()

# Catch button events
while True:
    event, values = window.read()

    if event in samples.keys():
        playSound(event)

    if event in (sg.WIN_CLOSED, 'Exit'):
      break
window.close()