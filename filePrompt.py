from PIL import Image # needed image processing
import imageOpen      # needed for dialog to open file
import tkinter as tk  # needed for window

def main():
    current_image_path = imageOpen.prompt_and_set_file()
    print(current_image_path)
if __name__ == '__main__':
    root = tk.Tk()
    root.wm_geometry("1x1")  #a trick to make it seem like the little annoying window
                                # never appeared
    main()  
    root.destroy()          #make the annoying little window begone!'''
