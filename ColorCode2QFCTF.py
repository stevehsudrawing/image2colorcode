# Convert Color Code File to QFCTF Text
# Author: Steve Hsu

if __name__ == "__main__":
    import os
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    print('Tool: Convert Color Code File to QFCTF Text')

    print()
    try:
        file = open('./result_color_code.txt', 'r')
        print('"result_color_code.txt" is found.')
    except:
        print('You should prepare a "result_color_code.txt" in this folder first.')
        print('Cannot continue. Press any key to exit.')
        os.system('pause')
        exit()

    file_content = file.read()

    image_width = len(file_content[0 : file_content.find('\n')])
    image_height = file_content.count('\n')
    if (image_width > 128 or image_height > 64):
        print()
        print('Warning: This image has a resolution of ' + str(image_width) + '*' + str(image_height) + ', which is too large for Sticky Note. If you use the QFCTF text generated at this time, it will cause a great performance burden on your device.')
        process_continue = input('Are you sure to continue? (Y/N): ')
        if (process_continue != 'y' and process_continue != 'Y' and process_continue != 'n' and process_continue != 'N'):
            process_continue = 'N'
            print('Illegal value, corrected to "N".')
        if (process_continue == 'n' or process_continue == 'N'):
            print()
            print('Operation canceled. Press any key to exit.')
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

    print()
    print('Please select a font size:')
    print('-3 - 6pt')
    print('-2 - 7pt')
    print('-1 - 8pt')
    print(' 0 - 9pt')
    print(' 1 - 11pt')
    print(' 2 - 13pt')
    print(' 3 - 15pt')
    font_size = eval(input('Your choice: '))
    if (font_size != -3 and font_size != -2 and font_size != -1 and font_size != 0 and font_size != 1 and font_size != 2 and font_size != 3):
        font_size = 0
        print('Illegal value, corrected to 0.')

    # Generate the QFCTF text
    image_qfctf = '``'
    if (font_size < 0):
        image_qfctf += '+' + str(font_size)
    elif (font_size > 0):
        image_qfctf += '++' + str(font_size)
    for char in file_content:
        if (char == '\n'):
            image_qfctf += '\n'
        elif (char in '0123456789ABCDEF'):
            image_qfctf += '@^' + char + '█'*pixel_width + '@^' + char
        else:
            image_qfctf += ' '*pixel_width
    image_qfctf += '``'
    # Simplify the QFCTF text
    for keyword in [('@^'+chr(char_index))*2 for char_index in range(48, 58)] + [('@^'+chr(char_index))*2 for char_index in range(65, 71)]:
        image_qfctf = image_qfctf.replace(keyword, '')

    # If using an older build of QF, replace the keywords
    if (older_build == 1):
        image_qfctf = image_qfctf.replace('2', 'G').replace('3', 'H').replace('4', 'I').replace('5', 'J').replace('6', 'K').replace('A', 'L').replace('B', 'M').replace('C', 'N').replace('D', 'O').replace('E', 'P')
        image_qfctf = image_qfctf.replace('G', '3').replace('H', '2').replace('I', '5').replace('J', '6').replace('K', '4').replace('L', 'B').replace('M', 'A').replace('N', 'D').replace('O', 'E').replace('P', 'C')
    if (font_size < 0):
        image_qfctf += '+' + str(font_size)
    elif (font_size > 0):
        image_qfctf += '++' + str(font_size)

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