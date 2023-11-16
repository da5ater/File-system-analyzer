import os
from datetime import datetime 

# git a list of all the directories in the guven path
# parameters  ->( Path - string - )
# output      ->( a List in a vraiable named content )
def git_content_from_path(path):
      
      try :
        # getting a list of all the directories
        content =  os.listdir(path)
        return content
      except FileNotFoundError as e :
        raise FileNotFoundError(f"'{e}'")
        
      except PermissionError as e :
        return []
        raise PermissionError(f"'{e}'")

      





# extract the info of the files from the get content function.
# scan  the path given recursivly
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
        raise PermissionError(f"permission erorr : '{e}'")
                        

    return entries_info

# take the path as a parameter and handels all the expected erorrs
def handel_erorr(path):
        # CHECK if path is empty or not a string
    if not path or not isinstance(path,str):
        raise ValueError(f"please Provide a valid Path")

    try :
    # validate pass existance
        if not os.path.exists(path):
            raise FileNotFoundError(f"path dose not exist")
    except PermissionError as e:
        raise PermissionError(f"Permission eror accessing '{path}' : '{e}' ")
    
    try :
    # CHECK IF PATH IS NOT A DIRECTORY
        if not os.path.isdir(path):
            raise NotADirectoryError(f"THE PROVIDED PATH '{path}'IS NOT A DIRECTORY")    
    except PermissionError as e:
        raise PermissionError(f"PROVIDED PATH  '{path}' IS NOT A DIRECTORY : '{e}' ")




# a function to scan a given path recursively 
# TAKES A PATH AND RETURN INFORMATION
# [ input is path and it is -> string ]   [ out  ??] 
def scan(path):
    # FIRST we handel all the edge cases
    handel_erorr(path)    
    # then we extract the list fo content
    content = git_content_from_path(path)

    if content:
        # THIRD we retrive all the needed information about that list
        entries_info = extract_info(content, path)
        for x in entries_info:
            print(x)


scan(r"G:\\")
   
        



     



    
    
