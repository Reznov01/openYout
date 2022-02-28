import os,keyboard as kb

def run():
    os.system("start www.youtube.com")

kb.add_hotkey('ctrl + shift + y', run, args =("")) 
kb.wait("f4")