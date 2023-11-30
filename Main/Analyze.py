from Scan import scan

# take file size
# return average file size of the whole directory
def AverageFileSize(entries_info):
    total_size = 0
    total_files = 0

    for info in entries_info.values():
        size_str = info[1]
        size = float(size_str.replace(" KB", ""))
        total_size += size
        total_files += 1

    average_size = total_size / total_files if total_files > 0 else 0
    print("Average File Size:", average_size, "KB")


# take file size and type
# return the distribution of the size in the whole directory
def SizeDistribution(entries_info):
    # Dictionary to store size distribution
    size_distribution = {}

    for info in entries_info.values():
        size_str = info[1]
        size = float(size_str.replace(" KB", ""))

        # Categorize sizes into ranges, you can customize the ranges based on your needs
        if size < 100:
            category = "Small"
        elif 100 <= size < 1000:
            category = "Medium"
        else:
            category = "Large"

        # Update size distribution dictionary
        size_distribution[category] = size_distribution.get(category, 0) + 1

    print("Size Distribution:")
    for category, count in size_distribution.items():
        print(f"{category}: {count}")


# take file type
# return the distribution of the type in the whole directory
def TypeDistribution(entries_info):
    # Dictionary to store type distribution
    type_distribution = {}

    for info in entries_info.values():
        file_type = info[0]  # Assuming file type is the first element in the info list

        # Update type distribution dictionary
        type_distribution[file_type] = type_distribution.get(file_type, 0) + 1

    print("Type Distribution:")
    for file_type, count in type_distribution.items():
        print(f"{file_type}: {count}")


# take directory sizes
# return largest directories
def LargestDirectories(entries_info):
    # Dictionary to store directory sizes
    directory_sizes = {}

    for entry, info in entries_info.items():
        size_str = info[1]
        size = float(size_str.replace(" KB", ""))
        directory_sizes[entry] = size

    # Sort directories by size in descending order
    sorted_directories = sorted(directory_sizes.items(), key=lambda x: x[1], reverse=True)

    print("Largest Directories:")
    for directory, size in sorted_directories[:5]:  # Print the top 5 largest directories
        print(f"{directory}: {size} KB")


# RETURN TEMPORAL TRENDS BASED ON CREATION TIME
def temp_trends(entries_info):
    # Dictionary to store temporal trends
    temporal_trends = {}

    for entry, info in entries_info.items():
        creation_time_str = info[2]  # Assuming creation time is the third element in the info list

        # Extract year from creation time (you can adjust the granularity as needed)
        year = creation_time_str.split('-')[0]

        # Update temporal trends dictionary
        temporal_trends[year] = temporal_trends.get(year, 0) + 1

    print("Temporal Trends:")
    for year, count in temporal_trends.items():
        print(f"{year}: {count}")


def Analyze(path):
    entries_info = scan(path)

    AverageFileSize(entries_info)
    SizeDistribution(entries_info)
    TypeDistribution(entries_info)
    LargestDirectories(entries_info)
    temp_trends(entries_info)


Analyze(r"G:\Mohamed\كلية")

    