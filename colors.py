#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from termcolor import colored
from pyfiglet import  figlet_format


def text_art(word=input("Message  to print:")):
    result = figlet_format(word)
    color = input("What color:")
    valid_colors= ("blue", "cyan", "green", "grey", "magenta")
    
    if color not in valid_colors:
        return colored(result, color= "magenta")
    else:

        return colored(result, color)

print(text_art())
