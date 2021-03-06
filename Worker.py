import pyperclip
import secrets
import string

PASS_SIZE = 20
FILE_NAME = 'pass.txt'

def generator():
    return ''.join(secrets.choice(string.ascii_letters + string.digits) for _ in range(PASS_SIZE))

def createNewPass(platform):
    with open(FILE_NAME, 'r') as file:
        lines = file.readlines()

        for line in lines:
            if (line.split(':')[0] == platform):
                copyPass(platform)
                print('A password for this platform already exists, I copied it to the clipboard.')

                return

    with open(FILE_NAME, 'a') as file:
        file.write('{}:{}\n'.format(platform, generator()))
    
    copyPass(platform)
    print('New password created and copied to clipboard.')

    return

def copyPass(platform, mainFlag=0):
    with open(FILE_NAME, 'r') as file:
        lines = file.readlines()

        for line in lines:
            if (line.split(':')[0] == platform):
                pyperclip.copy(line.split(':')[1])

                if mainFlag == 1:
                    print('Password copied to clipboard.')

                return

    prompt = input('A password for this platform does not exist. Would you like to create a new one? ')
    if (prompt == 'Y' or prompt == 'y'):
        createNewPass(platform)

    return

def deletePass(platform):
    flag = False

    with open(FILE_NAME, 'r') as file:
        lines = file.readlines()

    with open(FILE_NAME, 'w') as file:
        for line in lines:
            if (line.split(':')[0] != platform):
                file.write(line)
            else:
                flag = True

    if flag == True:
        print('Password deleted successfully.')
    else:
        print('Password not found.')

    return

def listPass():
    flag = False

    with open(FILE_NAME, 'r') as file:
        lines = file.readlines()

    for line in lines:
        flag = True
        print(line.split(':')[0])

    if not flag:
        print('There are no existing passwords.')

    return

def help():
    print('---------------- Help ----------------')
    print('Commands:')
    print('cn [args]  -- Create a new password with label [args]')
    print('cp [args]  -- Copy an existing password with label [args]')
    print('del [args] -- Delete an existing password with label [args] (WARNING: irreversible)')
    print('list       -- List all existing password labels.')
    print('help       -- Display this help page.')
    print('quit       -- Exit program.\n')

if __name__ == "__main__":
    while True:
        inp = input(': ')
        command = inp.split(' ')[0]

        if (command == 'cn'):
            createNewPass(inp.split(' ')[1])
        elif (command == 'cp'):
            copyPass(inp.split(' ')[1], 1)
        elif (command == 'del'):
            deletePass(inp.split(' ')[1])
        elif (command == 'list'):
            listPass()
        elif (command == 'help'):
            help()
        elif (command == 'quit'):
            break
        else:
            print('Unknown command')