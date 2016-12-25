import config as cfg
import sys
import datetime
import time


#Functions Defined ---------

#Errors
def NoArgErrorCheck():
    #Check if 0 args were provided
    if len(sys.argv) == 1:
        print "You have not written down anything."
        sys.exit()

def configNotesLocationExistsCheck():
    try:
        from config import NotesLocation
    except ImportError,ErrorMessage:
        ErrorMessage = str(ErrorMessage)
        if "cannot import name" in ErrorMessage:
            print "Your \"NotesLocation\" variable seems to be missing from your config file. Please review and then try again."
            sys.exit()

def configNotesLocationFilePathCheck():
    try:
        with open (cfg.NotesLocation, "r+") as file:
            return file
    except IOError,ErrorMessage:
        ErrorMessage = str(ErrorMessage)
        if "[Errno 2] No such file or directory: '/Users/Afaks/GitHub/note-proj/notes'" in ErrorMessage:
            print ErrorMessage
            print "The file path you have put for NotesLocation in your config file does not exist. Please review and try again."
            sys.exit()

#Main Functions
def GetSysInput():
    #Stripping to just the Note
    NoteInput = sys.argv
    NoteInput.remove(sys.argv[0])
    return NoteInput

def FormatSysInput(NoteInputRaw):
    #Format the list of arguments into a concatenated string
    NoteConcatenated = ""
    for item in NoteInputRaw:
        NoteConcatenated += "%s " % item
    NoteConcatenated = NoteConcatenated[:-1]
    return NoteConcatenated

def GetDateTime():
    Time = time.time()
    DateTimeVar = datetime.datetime.fromtimestamp(Time).strftime('%Y-%m-%d %H:%M:%S')
    DateTimeVar = "[%s]" %DateTimeVar
    return DateTimeVar

def NoteReady(NoteConcatenated,DateTimeVar):
    #Combining the note and the DateTime into a single string, making it ready to be written onto the .txt file
    NoteString = "%s\n%s\n\n" % (DateTimeVar,NoteConcatenated)
    return NoteString

def NoteWrite(NoteToWrite):
    with open(NotesLocation, 'r+') as file:
        content = file.read()
        file.seek(0,0)
        file.write(NoteToWrite + content)
    print "Wrote \"%s\" to Notes" % NoteConcatenated


#Functions for specific word commands
def ClearDoc():
    #Command to clear the .txt document
    ArgParseForClear = sys.argv[0].lower()
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
    #Command to print the .txt document
    ArgParseForPrint = sys.argv[0].lower()
    if ArgParseForPrint == "printnotes":
        with open(NotesLocation, "r") as file:
            print "Your Notes:\n%s" % file.read()
        sys.exit()
    else:
        pass

#Functions Called --------

#Variables (via function call)
NotesLocation = cfg.NotesLocation
NoteInputRaw = GetSysInput()
NoteConcatenated = FormatSysInput(NoteInputRaw)
DateTimeVar = GetDateTime()
NoteToWrite = NoteReady(NoteConcatenated,DateTimeVar)

#Error Checks
NoArgErrorCheck
configNotesLocationExistsCheck()
configNotesLocationFilePathCheck()

#Bonus Commands
ClearDoc()
TerminalPrint()

#Main
NoteWrite(NoteToWrite)
