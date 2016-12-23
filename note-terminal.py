import config as cfg
import sys
import datetime
import time

NotesLocation = cfg.NotesLocation

def GetSysInput():
    NoteInput = sys.argv
    NoteInput.remove(sys.argv[0])
    return NoteInput

NoteInputRaw = GetSysInput()

def FormatSysInput(NoteInputRaw):
    NoteConcatenated = ""
    for item in NoteInputRaw:
        NoteConcatenated += "%s " % item
    NoteConcatenated = NoteConcatenated[:-1]
    return NoteConcatenated

NoteConcatenated = FormatSysInput(NoteInputRaw)

def GetDateTime():
    Time = time.time()
    DateTimeVar = datetime.datetime.fromtimestamp(Time).strftime('%Y-%m-%d %H:%M:%S')
    DateTimeVar = "[%s]" %DateTimeVar
    return DateTimeVar

DateTimeVar = GetDateTime()

def NoteReady(NoteConcatenated,DateTimeVar):
    NoteString = "%s\n%s\n\n" % (DateTimeVar,NoteConcatenated)
    return NoteString

NoteToWrite = NoteReady(NoteConcatenated,DateTimeVar)

def NoteWrite(NoteToWrite):
    with open(NotesLocation, 'r+') as file:
        content = file.read()
        file.seek(0,0)
        file.write(NoteToWrite + content)
    print "Writing \"%s\" to Notes" % NoteConcatenated

def ClearDoc():
    ArgParseForClear = sys.argv[0].lower()
    # print ArgParseForClear[0]
    if ArgParseForClear == "clearnotes":
        ClearCheck = raw_input("You have typed in \"clearnotes\", which is a command to clear your current notes. Please confirm by typing \"clearnotes\": ")
        if ClearCheck == "clearnotes":
            print "Cleared Notes. "
            with open(NotesLocation, "w") as file:
                file.write("")
            sys.exit()
        else:
            "No notes have been cleared. Program Ending"
            sys.exit()

def TerminalPrint():
    ArgParseForPrint = sys.argv[0].lower()
    print "Passing here"
    if ArgParseForPrint == "printnotes":
        with open(NotesLocation, "r") as file:
            print "Your Notes:\n%s" % file.read()
        sys.exit()
    else:
        pass



ClearDoc()
TerminalPrint()
NoteWrite(NoteToWrite)
