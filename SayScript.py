import argparse
import os
import stat
import sys

voice_parse_error = "Error in line %d: voice lines must look like 'David: zarvox' (without quotes)"
dialog_name_error = "Error in line %d: name '%s' was not assigned a voice"
dialog_parse_error = "Error in line %d: dialogue lines must look like 'David: hello there' (without quotes)"

say_line = "say -v %s \"%s\"\n"

def errorQuit(msg, args):
    print msg % args
    print "Script not generated."
    sys.exit()

def main(filename):
    print "converting..."

    script = open(args.filename)
    outfilename = args.filename + '.out'
    fout = open(outfilename, 'w')

    fout.write("#!/bin/bash \n\n")

    voiceLines = True
    voices = dict()
    lineNumber = 0
    for line in script:
        lineNumber += 1
        if line == "\n":
            voiceLines = False
            continue
            
        if voiceLines:  # are we still in the voices section
            splits = line.strip().split(": ")
            if len(splits) == 2:
                name = splits[0]
                voice = splits[1]
                voices[name] = voice
            else:
                errorQuit(voice_parse_error, (lineNumber))
        else:
            splits = line.strip().split(": ")
            if len(splits) == 2:
                name = splits[0]
                dialogue = splits[1].replace("\"", "").replace("'", "")
                voice = voices.get(name)
                if not voice:
                    errorQuit(dialog_name_error, (lineNumber, name))
                else:
                    fout.write(say_line % (voice, dialogue))
            else:
                errorQuit(dialog_parse_error, (lineNumber))

    script.close()
    fout.close()

    st = os.stat(outfilename)
    os.chmod(outfilename, st.st_mode | stat.S_IEXEC)

    print "Done! run './%s' to play the script!" % outfilename


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Turn your script into a play')
    parser.add_argument('filename', type=str, help='the name of the file containing the script')
    args = parser.parse_args()

    filename = args.filename

    main(filename)