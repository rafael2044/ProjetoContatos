from customtkinter import CTkFont
import pyglet
import platform
import os

def install_fonts():
    if platform.system() == 'Windows':
        pyglet.options['win32_gbi_font']=True
        dir_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'Roboto')

        fonts = ['Roboto-Regular.ttf', 'Roboto-Bold.ttf']

        for font in fonts:
            pyglet.font.add_file(os.path.join(dir_path, font))

