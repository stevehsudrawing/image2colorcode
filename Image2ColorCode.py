# Convert PNG Image to Indexed Image and Color Code File
# Author: Steve Hsu

import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

print('Tool: Convert PNG Image to Indexed Image and Color Code File')
print('Author: Steve Hsu')

print()
try:
    from PIL import Image
    print('Successfully imported module "PIL".')
except:
    print('Cannot import module "PIL", maybe "Pillow" is not installed.')
    print('Please open another CMD window or Terminal and execute the command below:')
    print('    python -m pip install --upgrade Pillow')
    print('If necessary, you can also upgrade your "pip" first:')
    print('    python -m pip install --upgrade pip')
    print()
    print('Cannot continue. Press any key to exit.')
    os.system('pause')
    exit()

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
    image = Image.open('./source_image.png').convert('RGB')
    print('"source_image.png" is found.')
except:
    print('You should prepare a "source_image.png" in this folder first.')
    print('Cannot continue. Press any key to exit.')
    os.system('pause')
    exit()

print()
print('Image resolution: '+str(image.size[0])+'*'+str(image.size[1]))
print('Please select a resolution and pixel ratio:')
print('0 - 64*32, half-width pixel')
print('1 - 32*32, square pixel')
print('2 - 40*25, square pixel')
print('3 - 80*25, half-width pixel')
print('4 - 80*43, square pixel')
print('5 - 80*50, square pixel')
print('6 - Other (A resolution that\'s too large will result in abnormal displaying of this image in the command line interface or text mode!)')
print('The image will be resized to the specified resolution while keeping its ratio.')
resolution_section = eval(input('Your choice (input the number, then press Enter): '))
if (resolution_section != 0 and resolution_section != 1 and resolution_section != 2 and resolution_section != 3 and resolution_section != 4 and resolution_section != 5 and resolution_section != 6):
    resolution_section = 0
    print('Illegal value, corrected to 0.')

def clamp(n, min_value, max_value):
    if (min_value > max_value):
        raise ValueError('max_value must be greater than min_value')
    return min(max(n, min_value), max_value)

if (resolution_section == 0):
    resize_width = 32
    resize_height = 32
    pixel_width = 0.5
elif (resolution_section == 1):
    resize_width = 32
    resize_height = 32
    pixel_width = 1
elif (resolution_section == 2):
    resize_width = 40
    resize_height = 25
    pixel_width = 1
elif (resolution_section == 3):
    resize_width = 40
    resize_height = 25
    pixel_width = 0.5
elif (resolution_section == 4):
    resize_width = 80
    resize_height = 43
    pixel_width = 1
elif (resolution_section == 5):
    resize_width = 80
    resize_height = 50
    pixel_width = 1
else:
    resize_width = clamp(round(eval(input('Width (16 - 256): '))), 16, 256)
    resize_height = clamp(round(eval(input('Height (16 - 256): '))), 16, 256)
    pixel_width = eval(input('Pixel width (0.5 or 1): '))
    if (pixel_width != 0.5 and pixel_width != 1):
        pixel_width = 1
        print('Illegal value, corrected to 1.')

try:
    image_ratio = image.width / image.height
    image_resize_width = resize_width
    image_resize_height = round(resize_width / image_ratio)
    if (image_resize_height > resize_height):
        image_resize_width = round(resize_height * image_ratio)
        image_resize_height = resize_height
    image_resize_width /= pixel_width
    image_resize_width = int(image_resize_width)
    image_resize_height = int(image_resize_height)
    image = image.resize((image_resize_width, image_resize_height))
    print('Resized the image to '+str(image_resize_width)+'*'+str(image_resize_height)+'.')
except:
    print()
    print('Error occurred while resizing the image.')
    print('You may need to debug this script to troubleshoot.')
    print('Cannot continue. Press any key to exit.')
    os.system('pause')
    exit()

print()
print('Please choose a color palette:')
print('0 - CGA')
print('1 - Vintage')
print('2 - Campbell')
print('3 - Dark+')
print('4 - Ubuntu')
palette_type = eval(input('Your choice: '))
if (palette_type != 0 and palette_type != 1 and palette_type != 2 and palette_type != 3 and palette_type != 4):
    palette_type = 0
    print('Illegal value, corrected to 0.')

palette = {
    0: [
        0, 0, 0,        # 0
        170, 0, 0,      # 1
        0, 170, 0,      # 2
        170, 85, 0,     # 3
        0, 0, 170,      # 4
        170, 0, 170,    # 5
        0, 170, 170,    # 6
        170, 170, 170,  # 7
        85, 85, 85,     # 8
        255, 85, 85,    # 9
        85, 255, 85,    # A
        255, 255, 85,   # B
        85, 85, 255,    # C
        255, 85, 255,   # D
        85, 255, 255,   # E
        255, 255, 255   # F
    ],
    1: [
        0, 0, 0, 
        128, 0, 0, 
        0, 128, 0, 
        128, 128, 0, 
        0, 0, 128, 
        128, 0, 128, 
        0, 128, 128, 
        192, 192, 192, 
        128, 128, 128, 
        255, 0, 0, 
        0, 255, 0, 
        255, 255, 0, 
        0, 0, 255, 
        255, 0, 255, 
        0, 255, 255, 
        255, 255, 255
    ],
    2: [
        12, 12, 12, 
        197, 15, 31, 
        19, 161, 14, 
        193, 156, 0, 
        0, 55, 218, 
        136, 23, 152, 
        58, 150, 221, 
        204, 204, 204, 
        118, 118, 118, 
        231, 72, 86, 
        22, 198, 12, 
        249, 241, 165, 
        59, 120, 255, 
        180, 0, 158, 
        97, 214, 214, 
        242, 242, 242
    ], 
    3: [
        0, 0, 0, 
        205, 49, 49, 
        13, 188, 121, 
        229, 229, 16, 
        36, 114, 200, 
        188, 63, 188, 
        17, 168, 205, 
        229, 229, 229, 
        102, 102, 102, 
        241, 76, 76, 
        35, 209, 139, 
        245, 245, 67, 
        59, 142, 234, 
        214, 112, 214, 
        41, 184, 219, 
        229, 229, 229
    ], 
    4: [
        1, 1, 1, 
        222, 56, 43, 
        57, 181, 74, 
        255, 199, 6, 
        0, 111, 184, 
        118, 38, 113, 
        44, 181, 233, 
        204, 204, 204, 
        128, 128, 128, 
        255, 0, 0, 
        0, 255, 0, 
        255, 255, 0, 
        0, 0, 255, 
        255, 0, 255, 
        0, 255, 255, 
        255, 255, 255
    ]
}
for type in palette:
    palette[type] += [0] * (256*3 - len(palette[type]))

try:
    # Convert the source image using the specified palette
    palette_image = Image.new('P', (1, 1))
    palette_image.putpalette(palette[palette_type])
    indexed_image = image.quantize(palette=palette_image)
except:
    print()
    print('Error occurred while converting the source image using the specified palette.')
    print('You may need to debug this script to troubleshoot.')
    print('Cannot continue. Press any key to exit.')
    os.system('pause')
    exit()

print()
# Save the indexed image
try:
    indexed_image.save('./result_image.png')
    print('The indexed image is saved in "./result_image.png".')
except:
    print('Cannot save the indexed image.')

# Generate the color code
try:
    image_code = ''
    i = 0
    for pixel in indexed_image.tobytes():
        if (pixel >= 0 and pixel <=9):
            image_code += (chr(pixel+48))
        else:
            image_code += (chr(pixel+55))
        i += 1
        if (i == indexed_image.size[0]):
            image_code += '\n'
            i = 0
except:
    print()
    print('Error occurred while generating the color code.')
    print('You may need to debug this script to troubleshoot.')
    print('Cannot continue. Press any key to exit.')
    os.system('pause')
    exit()

# Save the color code file
print()
try:
    file = open('./result_color_code.txt', 'w', encoding='utf8')
    file.write(image_code)
    print('The color code file is saved in "./result_color_code.txt".')
    print('Run "ColorCodeFilePreview.py" to preview this file.')
    file.close()
except:
    print('Cannot save the color code file.')

print()
print('Completed. Press any key to exit.')
os.system('pause')