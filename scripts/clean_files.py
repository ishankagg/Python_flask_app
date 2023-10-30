import os

path_1 = "final_cleaned_files"
path_2 = "output"
path_3 = "static/files"

dir_list_1 = os.listdir(path_1)
dir_list_2 = os.listdir(path_2)
dir_list_3 = os.listdir(path_3)


def clean_files():
    for file in dir_list_1:
        if os.path.exists(path_1):
            os.remove(f'{path_1}/{file}')
    
    for file in dir_list_2:
        if os.path.exists(path_2):
            os.remove(f'{path_2}/{file}')
    
    for file in dir_list_3:
        if os.path.exists(path_3):
            os.remove(f'{path_3}/{file}')

    print("Files Cleaned")

if __name__ == "__main__":
    clean_files()