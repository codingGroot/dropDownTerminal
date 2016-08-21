import os
import sys

#end of current working directory so the terminal
#will not display a ton of directories like
#/home/user/documents/anotherfolder/morefolders
def print_end_of_cwd():
    cwd = os.getcwd().split("/")
    print(cwd[-1], end="")



#"Main Statement"
while (True):
    try:
        print_end_of_cwd()
        print(': # ', end="")
        command = input()
        if(command[:2] == 'cd'):
            os.chdir(command[3:])
        else:
            os.system(command)
        print()
    except KeyboardInterrupt:
        print('\nProgram Exiting\n')
        sys.exit()
    except OSError as e:
        print('File not Found\n')
        continue
