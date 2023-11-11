import os
import datetime
import humanize
from pathlib import Path as p



# a function to scan a given path recursively 
# TAKES A PATH AND RETURN INFORMATION
# [ input is path and it is -> string ]   [ out  ??] 
def scan(path):
    # path = p(path)
    # CHECK if path is empty or not a string
    if not path or not isinstance(path,str):
        raise ValueError("please Provide a valid Path")

    try :
    # validate pass existance
        if not os.path.exists(path):
            raise FileNotFoundError("path dose not exist")
    except PermissionError as e:
        raise PermissionError("Permission eror accessing '{path}' : '{e}' ")
    
    try :
    # CHECK IF PATH IS NOT A DIRECTORY
        if not os.path.isdir(path):
            raise NotADirectoryError("THE PROVIDED PATH '{PATH}'IS NOT A DIRECTORY")    
    except PermissionError as e:
        raise PermissionError("PROVIDED PATH  '{path}' IS NOT A DIRECTORY : '{e}' ")
    
    try :
    # getting a list of all the directories
        content = os.listdir(path)
    except FileNotFoundError as e :
        print("eror : '{e}")
    except PermissionError as e :
        print("erorr : '{e}")


    print(content)

scan("G:\Mohamed\هجرة")

     



    
        
    
