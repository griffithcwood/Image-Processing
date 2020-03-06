from Pillow import Image
import imageOpen
import fileSave
__name__ = "Griff Wood"
__version__ = "2.5"
"""The functions section of the image recognition projects"""
def mod(mod,imageName, threshold="100",):
    img      = getImage()
    arrayImg = getArray(img)
    new_img  = modImage(arrayImg,mod=mod,threshold=threshold)
    new_img.show()
    dir = fileSave.get_dir()
    dir = str(dir) + "/" + imageName + ".png"
    new_img.save(dir)

def getImage():
    '''Asks the user for the image
    :return the image:
    '''
    img_string = imageOpen.prompt_and_get_file_name()
    img = Image.open(img_string)
    return img

def getArray(img):
    '''turns an image into a 2-d array with touples for pixel colors
    :param img:
    :return the array:
    '''
    w = img.size[0]
    h = img.size[1]

    Array = [[1 for _  in range (h)]for _ in range (w)]

    for i in range(w):                              #Searches each pixel and puts into 2d array
        for j in range(h):
            pixel = img.getpixel((i, j))
            red = pixel[0]
            green = pixel[1]
            blue = pixel[2]
            RGB = (red,green,blue)
            Array[i][j] = (RGB)
    return Array

def modImage(array, mod="",threshold=100):
    '''takes an array of an image and modifies the image based on parameters
    :param An array of integers coresponding to an image:
    :param A modifier for what operation will be performed on the pixels:
    :param A threshold for some operations:
    :returns An image made from the modified array'''
    w = len(array)
    h = len(array[0])
    new_img = Image.new("RGBA", (w, h), "blue")     #makes a new blank blue image
    for i in range(w):                              #Iterates through each pixel's colors and modifies accordingly
        for j in range(h):
            red   = array[i][j][0]
            green = array[i][j][1]
            blue  = array[i][j][2]
                                                    #Chooses formula based on given parameter
            if mod == "sepia":
                '''Uses Formula for Sepia'''
                new_red   = int((red * 0.393) + (green * 0.796) + (blue * 0.189))
                new_green = int((red * 0.349) + (green * 0.686) + (blue * 0.161))
                new_blue  = int((red * 0.272) + (green * 0.534) + (blue * 0.131))
            elif mod == "greyscale":
                '''Uses Luminosity Formula for Greyscale'''
                new_red   = int((red * 0.21) + (green * 0.72) + (blue * 0.07))
                new_green = int((red * 0.21) + (green * 0.72) + (blue * 0.07))
                new_blue  = int((red * 0.21) + (green * 0.72) + (blue * 0.07))
            elif mod == "dog":
                new_rgb = dogVision(red, green, blue)
                new_red   = new_rgb[0]
                new_green = new_rgb[1]
                new_blue  = new_rgb[2]
            elif mod == "dalton":
                new_rgb = daltonize(red,green,blue)
                new_red   = new_rgb[0]
                new_green = new_rgb[1]
                new_blue  = new_rgb[2]
            elif mod == "lighten":
                new_red   = int(red + threshold)
                new_green = int(green + threshold)
                new_blue  = int(blue + threshold)
            elif mod == "darken":
                '''Decreases each color by given threshold'''
                new_red   = int(red - threshold)
                new_green = int(green - threshold)
                new_blue  = int(blue - threshold)
            else:
                new_red   = red
                new_green = green
                new_blue  = blue

            new_img.putpixel((i, j), (new_red, new_green, new_blue))
    return new_img

def reflect(array,axis="x"):
    ''' reflects the image over the selected axis
    :param The image array:
    :param The axis to reflect the image upon:
    :return The new Image:
    '''
    w = len(array)
    h = len(array[0])
    new_img = Image.new("RGBA", (w, h), "blue")
    for i in range(w):
        for j in range(h):
            '''swaps the pixels around in desired way'''
            red   = array[i][j][0]
            green = array[i][j][1]
            blue  = array[i][j][2]
            if axis == "x":
                new_img.putpixel((-i,j)(red,green,blue))
            elif axis == "y":
                new_img.putpixel((i,-j)(red,green,blue))
            else:
                new_img.putpixel((j,i),(red,green,blue))
    return new_img

def scanline(array):
    '''creates a scanline effect akin to those on old arcade machines and/or old screens
    :param The image as an array:
    :return The image:
    '''
    w = len(array)
    h = len(array[0])
    new_img = Image.new("RGBA", (w, h), "black")     #makes a new blank blue image
    big_pixels = [[1 for _  in range (int(h / 2))]for _ in range (int(w / 2))]
    for i in range(0,w,2):                              #Iterates through each pixel's colors and modifies accordingly
        for j in range(0,h,2):
            if(i != w - 1 and j != h -1):
                pixel0 = array[i]  [j]
                pixel1 = array[i+1][j]
                pixel2 = array[i]  [j+1]
                pixel3 = array[i+1][j+1]
                big_pixel_array = [pixel0,pixel1,pixel2,pixel3]
                red   = 0
                green = 0
                blue  = 0
                for pixel in big_pixel_array:
                    red = red + pixel[0]
                    green = green + pixel[1]
                    blue = blue + pixel[2]
                red   = int(red / 4)
                green = int(green / 4)
                blue  = int(blue / 4)
                big_pixel = (red, green, blue)
                new_img.putpixel((i,j),big_pixel)
    return new_img

def dogVision(red,green,blue):
    '''converts color into protanopia (dog vision) by going through LMS then a protanopia formula then back to RGB
    Scientific Data and Matricies come from here: http://biecoll.ub.uni-bielefeld.de/volltexte/2007/52/pdf/ICVS2007-6.pdf
    :param The amount red:
    :param The amount green:
    :param The amoun blue:
    :return a new array of the Image:
    '''
    '''transforms into RGB into LMS (a color space representing the three cones of the human eye)'''
    val1 = [[17.8824,43.5161,4.1193],[3.4557,27.1554,3.8671],[0.02996,0.18431,1.4670]]
    l = (val1[0][0] * red) + (val1[0][1] * green) + (val1[0][2] * blue)
    m = (val1[1][0] * red) + (val1[1][1] * green) + (val1[1][2] * blue)
    s = (val1[2][0] * red) + (val1[2][1] * green) + (val1[2][2] * blue)
    '''transforms into LMS into corresponding protanopia LMS (dog vision)'''
    val2 = [[0,2.0234,-2.52581],[0,1,0],[0,0,1]]
    lpro = (val2[0][0] * l) + (val2[0][1] * m) + (val2[0][2] * s)
    mpro = (val2[1][0] * l) + (val2[1][1] * m) + (val2[1][2] * s)
    spro = (val2[2][0] * l) + (val2[2][1] * m) + (val2[2][2] * s)
    '''Transforms LMS protanopia back into RGB (an inverse of the original matrix)'''
    val3 = [[0.0809,-0.1305,0.1167],[-0.0102,0.0540,-0.1136],[-0.0003, -0.0041,0.6935]]
    rpro = (val3[0][0] * lpro) + (val3[0][1] * mpro) + (val3[0][2] * spro)
    gpro = (val3[1][0] * lpro) + (val3[1][1] * mpro) + (val3[1][2] * spro)
    bpro = (val3[2][0] * lpro) + (val3[2][1] * mpro) + (val3[2][2] * spro)
    new_rgb = (int(rpro), int(gpro), int(bpro))
    return new_rgb
def daltonize(r,g,b):
    '''Takes an image and Daltonizes it. Daltonization is a process that makes an image more easily understood for someone who is
    red-green color blind.
    :param The red color val:
    :param The green color val:
    :param The blue color val:
    :return a touple of the daltonized color vals:
    '''
    '''takes the Protanopia value'''
    pro_rgb = dogVision(r,g,b)
    rpro = pro_rgb[0]
    gpro = pro_rgb[1]
    bpro = pro_rgb[2]
    '''subtracts normal color vals from color blind values'''
    r1   = r - rpro
    g1   = g - gpro
    b1   = b - bpro
    '''puts the values through an error matrix'''
    error_matrix = [[0,0,0],[0.7,1,0],[0.7,0,1]]
    r2 = (error_matrix[0][0] * r1) + (error_matrix[0][1] * g1) + (error_matrix[0][2] * b1)
    g2 = (error_matrix[1][0] * r1) + (error_matrix[1][1] * g1) + (error_matrix[1][2] * b1)
    b2 = (error_matrix[2][0] * r1) + (error_matrix[2][1] * g1) + (error_matrix[2][2] * b1)
    '''and then adds them back to the original colors'''
    r3 = int(r + r2)
    g3 = int(g + g2)
    b3 = int(b + b2)
    return (r3,g3,b3)

