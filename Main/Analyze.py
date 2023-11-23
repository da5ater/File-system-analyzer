from Scan import scan




# take file size
# return average file size of the whole directory
def AverageFileSize (entries_info):
    total_size = 0
    total_files = 0
    
    for  info in entries_info.values():
        size_str = info[1]
        # print(size_str)
        size = float(size_str.replace(" KB",""))

        total_size += size
        total_files +=1

    AverageSize = total_size / total_files if total_files > 0 else 0
    print (AverageSize)
        

    

    

# take file size and type
# return the distribution of the size in the whole directory
def SizeDistribution(entries_info):
    # code
    pass


# take file type
# return the distribution of the type in the whole directory
def TypeDistribution(entries_info):
    #code
    pass

# take directory sizes 
# return largest directories
def LargestDirectories(directory_structures):
    # code
    pass

# RETURN TRMPORAL TRENDS BASED ON CRETION TIIME
def temp_trends(entries_info):
    #code
     pass     

def Analyze(path):

    entries_info = scan(path)

    # AverageSize = AverageFileSize(entries_info)
    # SDistribution = SizeDistribution(entries_info)
    # TDistribution = TypeDistribution(entries_info)
    # DirectoriesList = LargestDirectories(entries_info)
    # trends = temp_trends(entries_info)

    AverageFileSize(entries_info)

Analyze(r"G:\Mohamed\كلية")
    