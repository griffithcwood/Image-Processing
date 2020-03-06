import functions as f
import sys
__name__ = "Griff Wood"
__version__ = "2.5"
"""The GUI section of the Image Recognition Project. It's fairly rudimentary but it works """
def showMenu():
    '''shows the main menu in terminal and functions as a GUI'''
    while(True):
        print("0: Explanation  \n " +
          "1: Sepiatone  \n"        +
          "2: Greyscale  \n"        +
          "3: Dog-Vision  \n"       +
          "4: Lighten  \n"          +
          "5: Darken  \n"           +
          "6: Scanline  \n"         +
          "7: Reflect  \n"          +
          "8: Reflect  \n"          +
          "9: Quit \n"
          )
        option = input("Hello, and welcome What would you like to do?: ")
        try:
            option = int(option)
        except ValueError:
            print("Please enter a valid number")
        if   option == 0:
            print("This is an image recognition project. Enter an option to transform a selected Image.  Image Version 2.5 By")
        elif option == 1:
            name = input("Please enter a name for your image: ")
            f.mod("sepia",name)
        elif option == 2:
            name = input("Please enter a name for your image: ")
            f.mod("greyscale",name)
        elif option == 3:
            name = input("Please enter a name for your image: ")
            f.mod("dog",name)
        elif option == 4:
            name = input("Please enter a name for your image: ")
            f.mod("lighten",name)
        elif option == 5:
            name = input("Please enter a name for your image: ")
            f.mod("darken",name)
        elif option == 6:
            name = input("Please enter a name for your image: ")
            img      = f.getImage()
            arrayImg = f.getArray(img)
            new_img  = f.scanline(arrayImg)
            new_img.show()
            dir = f.fileSave.get_dir()
            dir = str(dir) + "/" + name + ".png"
            new_img.save(dir)
        elif option == 7:
            name = input("Please enter a name for your image: ")
            img      = f.getImage()
            arrayImg = f.getArray(img)
            new_img  = f.reflect(arrayImg)
            new_img.show()
            dir = f.fileSave.get_dir()
            dir = str(dir) + "/" + name + ".png"
            new_img.save(dir)
        elif option == 8:
            name = input("Please enter a name for your image: ")
            f.mod("dalton",name)
        elif option == 9:
            sys.exit(0)
        else:
            print("Please enter a valid number")


showMenu()