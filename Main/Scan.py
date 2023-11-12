import os
from datetime import datetime 




# extract the info of the files in the path given recursivly
# (in  -> content(string), path(string))   (out  -> file_info(list))
def extract_info(content,path):

    # a dictionary contain a key wich is the file (string), and a value wich is all the informatio in a readable way (list) 
    entries_info = {}
    try:
        for entry in content:

            entry_path = os.path.join(path ,entry)

            if os.path.isfile(entry_path):
                # a list containes all the information about the file
                array_of_information=[]    

                
                file_info = os.stat(entry_path) 

                # size information
                file_size = file_info.st_size
                # size in a human_readable way
                size =  str(file_size / 1024 )+ ' KB'
                # adding it up in the list
                array_of_information.append(size)

                # time information
                file_creation_time = file_info.st_ctime
                file_modefication_time = file_info.st_mtime
                # time in a human-readable way
                creation_time = datetime.fromtimestamp(file_creation_time).strftime('%Y-%m-%d %H:%M:%S')
                # adding it up in the list
                array_of_information.append(creation_time)
                modefication_time = datetime.fromtimestamp(file_modefication_time).strftime('%Y-%m-%d %H:%M:%S')
                # adding it up in the list
                array_of_information.append(modefication_time)

                # admenestrative information
                file_owner = file_info.st_uid
                # adding it up in the list
                array_of_information.append(file_owner)
                file_permission = file_info.st_mode
                # adding it up in the list
                array_of_information.append(file_permission)

                # assign the file with the array of information
                entries_info[entry] = array_of_information

                del(array_of_information)
                    
            else :
                file_info = scan(entry_path)
                
    except PermissionError as e:
        print("permission erorr : '{e}")                

    for x in entries_info:
        print(x)

# a function to scan a given path recursively 
# TAKES A PATH AND RETURN INFORMATION
# [ input is path and it is -> string ]   [ out  ??] 
def scan(path):
    
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
    
 
    content = os.listdir(path)


    try :
    # getting a list of all the directories
        content = os.listdir(path)
    except FileNotFoundError as e :
        print("eror : '{e}")
    except PermissionError as e :
        print("erorr : '{e}")
    

    extract_info(content,path)


scan(r"G:\\")
   
        



     



    
    
