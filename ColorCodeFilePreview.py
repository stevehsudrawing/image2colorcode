# Color Code File Preview
# Author: Steve Hsu

import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

print('Tool: Color Code File Preview')
print('Author: Steve Hsu')

print()
try:
    from colorama import init, Back, deinit
    print('Successfully imported module "colorama".')
    init(autoreset=True)
    print('Current color palette:')
    print(Back.BLACK + '  ', end='')
    print(Back.RED + '  ', end='')
    print(Back.GREEN + '  ', end='')
    print(Back.YELLOW + '  ', end='')
    print(Back.BLUE + '  ', end='')
    print(Back.MAGENTA + '  ', end='')
    print(Back.CYAN + '  ', end='')
    print(Back.WHITE + '  ', end='')
    print()
    print(Back.LIGHTBLACK_EX + '  ', end='')
    print(Back.LIGHTRED_EX + '  ', end='')
    print(Back.LIGHTGREEN_EX + '  ', end='')
    print(Back.LIGHTYELLOW_EX + '  ', end='')
    print(Back.LIGHTBLUE_EX + '  ', end='')
    print(Back.LIGHTMAGENTA_EX + '  ', end='')
    print(Back.LIGHTCYAN_EX + '  ', end='')
    print(Back.LIGHTWHITE_EX + '  ', end='')
    deinit()
    print()
except:
    print('Cannot import module "colorama", maybe "colorama" is not installed.')
    print('Please open another CMD window or Terminal and execute the command below:')
    print('    python -m pip install --upgrade colorama')
    print('If necessary, you can also upgrade your "pip" first:')
    print('    python -m pip install --upgrade pip')
    print()
    print('Cannot continue. Press any key to exit.')
    os.system('pause')
    exit()

print()
try:
    file = open('./result_color_code.txt', 'r')
    print('"result_color_code.txt" is found.')
except:
    print('You should prepare a "result_color_code.txt" in this folder first.')
    print('Cannot continue. Press any key to exit.')
    os.system('pause')
    exit()

print()
print('Please specify the width of pixels:')
print('1 - Half-width')
print('2 - Square')
pixel_width = eval(input('Your choice (input the number, then press Enter): '))
if (pixel_width != 1 and pixel_width != 2):
    pixel_width = 1
    print('Illegal value, corrected to 1.')

print()
for char in file.read():
    if (char == '\n'):
        deinit()
        print(Back.RESET + '\n', end='')
    elif (char == '0'):
        print(Back.BLACK + ' ' * pixel_width, end='')
    elif (char == '1'):
        print(Back.RED + ' ' * pixel_width, end='')
    elif (char == '2'):
        print(Back.GREEN + ' ' * pixel_width, end='')
    elif (char == '3'):
        print(Back.YELLOW + ' ' * pixel_width, end='')
    elif (char == '4'):
        print(Back.BLUE + ' ' * pixel_width, end='')
    elif (char == '5'):
        print(Back.MAGENTA + ' ' * pixel_width, end='')
    elif (char == '6'):
        print(Back.CYAN + ' ' * pixel_width, end='')
    elif (char == '7'):
        print(Back.WHITE + ' ' * pixel_width, end='')
    elif (char == '8'):
        print(Back.LIGHTBLACK_EX + ' ' * pixel_width, end='')
    elif (char == '9'):
        print(Back.LIGHTRED_EX + ' ' * pixel_width, end='')
    elif (char == 'A'):
        print(Back.LIGHTGREEN_EX + ' ' * pixel_width, end='')
    elif (char == 'B'):
        print(Back.LIGHTYELLOW_EX + ' ' * pixel_width, end='')
    elif (char == 'C'):
        print(Back.LIGHTBLUE_EX + ' ' * pixel_width, end='')
    elif (char == 'D'):
        print(Back.LIGHTMAGENTA_EX + ' ' * pixel_width, end='')
    elif (char == 'E'):
        print(Back.LIGHTCYAN_EX + ' ' * pixel_width, end='')
    elif (char == 'F'):
        print(Back.LIGHTWHITE_EX + ' ' * pixel_width, end='')

deinit()
print()
print('Completed. Press any key to exit.')
os.system('pause')