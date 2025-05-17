# Convert Color Code File to QFCTF Text
# Author: Steve Hsu

import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

print('Tool: Convert Color Code File to QFCTF Text')
print('Author: Steve Hsu')

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
print('Are you using Quanto Flx 2.00 Delta (Build 1101) or older?')
print('0 - No')
print('1 - Yes')
older_build = eval(input('Your choice: '))
if (older_build != 0 and older_build != 1):
    older_build = 0
    print('Illegal value, corrected to 0.')

# Generate the QFCTF text
image_qfctf = '``'
for char in file.read():
    if char == '\n':
        image_qfctf += '\n'
    else:
        image_qfctf += '@^' + char + '█'*pixel_width + '@^' + char
image_qfctf += '``'
# Simplify the QFCTF text
for keyword in [('@^'+chr(char_index))*2 for char_index in range(48, 58)] + [('@^'+chr(char_index))*2 for char_index in range(65, 71)]:
    image_qfctf = image_qfctf.replace(keyword, '')
# If using an older build of QF, replace the keywords
if (older_build == 1):
    image_qfctf = image_qfctf.replace('2', 'G')
    image_qfctf = image_qfctf.replace('3', 'H')
    image_qfctf = image_qfctf.replace('4', 'I')
    image_qfctf = image_qfctf.replace('5', 'J')
    image_qfctf = image_qfctf.replace('6', 'K')
    image_qfctf = image_qfctf.replace('A', 'L')
    image_qfctf = image_qfctf.replace('B', 'M')
    image_qfctf = image_qfctf.replace('C', 'N')
    image_qfctf = image_qfctf.replace('D', 'O')
    image_qfctf = image_qfctf.replace('E', 'P')
    image_qfctf = image_qfctf.replace('G', '3')
    image_qfctf = image_qfctf.replace('H', '2')
    image_qfctf = image_qfctf.replace('I', '5')
    image_qfctf = image_qfctf.replace('J', '6')
    image_qfctf = image_qfctf.replace('K', '4')
    image_qfctf = image_qfctf.replace('L', 'B')
    image_qfctf = image_qfctf.replace('M', 'A')
    image_qfctf = image_qfctf.replace('N', 'D')
    image_qfctf = image_qfctf.replace('O', 'E')
    image_qfctf = image_qfctf.replace('P', 'C')

print()
try:
    file = open('./result_qfctf_text.txt', 'w', encoding='utf8')
    file.write(image_qfctf)
    print('The QFCTF text is saved in "./result_qfctf_text.txt".')
    print('Copy the content of "result_qfctf_text.txt" into your Sticky Note and enjoy!')
    file.close()
except:
    print('Cannot save the QFCTF text.')

print()
print('Completed. Press any key to exit.')
os.system('pause')