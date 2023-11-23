from Scan import Scan




# take file size
# return average file size of the whole directory
def AverageFileSize (entries_info):
    # code
    pass

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

    entries_info = Scan(path)

    AverageSize = AverageFileSize(entries_info)
    SDistribution = SizeDistribution(entries_info)
    TDistribution = TypeDistribution(entries_info)
    DirectoriesList = LargestDirectories(entries_info)
    trends = temp_trends(entries_info)

    
    
     