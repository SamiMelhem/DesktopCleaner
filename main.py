from os import listdir, makedirs, path
from shutil import move
from logging import basicConfig, info, INFO

# logging configuration
basicConfig(level=INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Locate the download folder
download_folder = 'C:\\Users\\terry\\Downloads'
org_system_folder_names = { # folder_name_shortcut : file_location
    'acr': "C:\\Users\\terry\\OneDrive\\Desktop\\desktop_cleaner\\After College Resources",
    'band': "C:\\Users\\terry\\OneDrive\\Desktop\\desktop_cleaner\\Band",
    'books': "C:\\Users\\terry\\OneDrive\\Desktop\\desktop_cleaner\\Books",
    'business': "C:\\Users\\terry\\OneDrive\\Desktop\\desktop_cleaner\\Business",
    'codeproj': "C:\\Users\\terry\\OneDrive\\Desktop\\desktop_cleaner\\Coding Projects",
    'collegedoc': "C:\\Users\\terry\\OneDrive\\Desktop\\desktop_cleaner\\College Documents",
    'dsp': "C:\\Users\\terry\\OneDrive\\Desktop\\desktop_cleaner\\Data Science Projects",
    'ditl': "C:\\Users\\terry\\OneDrive\\Desktop\\desktop_cleaner\\Day In The Life",
    'diet': "C:\\Users\\terry\\OneDrive\\Desktop\\desktop_cleaner\\Diet",
    'edit': "C:\\Users\\terry\\OneDrive\\Desktop\\desktop_cleaner\\Editing",
    'finance': "C:\\Users\\terry\\OneDrive\\Desktop\\desktop_cleaner\\Finances",
    'fb': "C:\\Users\\terry\\OneDrive\\Desktop\\desktop_cleaner\\Friend Blackmail",
    'hsd': "C:\\Users\\terry\\OneDrive\\Desktop\\desktop_cleaner\\High School Documents",
    'hsc': "C:\\Users\\terry\\OneDrive\\Desktop\\desktop_cleaner\\High School to College",
    'intern': "C:\\Users\\terry\\OneDrive\\Desktop\\desktop_cleaner\\Internships",
    'mus': "C:\\Users\\terry\\OneDrive\\Desktop\\desktop_cleaner\\Music",
    'lf': "C:\\Users\\terry\\OneDrive\\Desktop\\desktop_cleaner\\Leftover Files",
    'mc': "C:\\Users\\terry\\OneDrive\\Desktop\\desktop_cleaner\\Music Composition",
    'pi': "C:\\Users\\terry\\OneDrive\\Desktop\\desktop_cleaner\\Personal Information",
    'pod': "C:\\Users\\terry\\OneDrive\\Desktop\\desktop_cleaner\\Podcast",
    'selfie': "C:\\Users\\terry\\OneDrive\\Desktop\\desktop_cleaner\\Selfies",
    'sid': "C:\\Users\\terry\\OneDrive\\Desktop\\desktop_cleaner\\Self-Improvement Diagrams",
    'trip': "C:\\Users\\terry\\OneDrive\\Desktop\\desktop_cleaner\\Trips",
    'vg': "C:\\Users\\terry\\OneDrive\\Desktop\\desktop_cleaner\\Video Games"
}

# Create an organization system for different files
def create_org_system():
    # Check if system exists before creating it
    for folder in org_system_folder_names.values():
        if not path.exists(folder):
            makedirs(folder)
            folder_name = folder.split("\\")[-1]
            info(f'Created folder: {folder_name}')

# Put each file into their respective folders
def insert_files():
    for filename in listdir(download_folder):
        # Removes the leading and trailing quotes from the download folder
        download_folder_clean = download_folder.strip('"')

        file_shortcut = filename.split(' ')[-1].lower().split('.')[0]
        if file_shortcut in org_system_folder_names.keys():
            folder_path = org_system_folder_names[file_shortcut]
        else: # Insert into lf
            folder_path = org_system_folder_names['lf']

        src_path = path.join(download_folder_clean, filename)
        dst_path = path.join(folder_path, filename)

        # check if the file already exists in the dst_folder
        counter = 1
        while path.exists(dst_path):
            file_name, file_ext = path.splitext(filename)
            new_file_name = f'{file_name}_({counter}){file_ext}'
            dst_path = path.join(folder_path, new_file_name)
            counter += 1

        move(src_path, dst_path)
        info(f'Moved {filename} to {dst_path}')

if __name__ == '__main__':
    create_org_system()
    insert_files()
