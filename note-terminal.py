import config as cfg
import sys
import datetime
import time

def GetSysInput():
    NoteInput = sys.argv
    NoteInput.remove(sys.argv[0])
    return NoteInput

NoteInputRaw = GetSysInput()

def FormatSysInput(NoteInputRaw):
    NoteConcatenated = ""
    for item in NoteInputRaw:
        NoteConcatenated += "%s " % item
    return NoteConcatenated

NoteConcatenated = FormatSysInput(NoteInputRaw)

def GetDateTime():
    Time = time.time()
    DateTimeVar = datetime.datetime.fromtimestamp(Time).strftime('%Y-%m-%d %H:%M:%S')
    return DateTimeVar

DateTimeVar = GetDateTime()

def NoteReady(NoteConcatenated,DateTimeVar):
    NoteString = "%s\n%s\n\n" % (DateTimeVar,NoteConcatenated)
    return NoteString

NoteToWrite = NoteReady(NoteConcatenated,DateTimeVar)

def NoteWrite(NoteToWrite):
    NotesLocation = cfg.NotesLocation
    with open(NotesLocation, 'r+') as file:
        content = file.read()
        file.seek(0,0)
        file.write(NoteToWrite + content)

NoteWrite(NoteToWrite)
