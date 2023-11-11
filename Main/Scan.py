import os
import datetime
import humanize
from pathlib import Path as p


# extract the info of the files in the path given recursivly
# (in  -> content(string), path(string))   (out  -> file_info(list))
def extract_info(content,path):
    for entry in content:
        entry_path = os.path.join(path ,entry)
        if os.path.isfile(entry_path):
            print(entry_path)
            file_info = os.stat(entry_path)            
            return file_info.st_size    
        else :
            file_info = scan(entry_path)



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
    

    print(extract_info(content,path))


scan(r'G:\softwares')
   
        



     



    
    
