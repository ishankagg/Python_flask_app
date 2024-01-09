import os

path_1 = "final_cleaned_files"
path_2 = "output"
path_3 = "static/files"

dir_list_1 = []

for file in os.listdir(path_1):
    if file == '.gitkeep':
        continue
    else:
        dir_list_1.append(file)


dir_list_2 = []

for file in os.listdir(path_2):
    if file == '.gitkeep':
        continue
    else:
        dir_list_2.append(file)


dir_list_3 = []

for file in os.listdir(path_3):
    if file == '.gitkeep':
        continue
    else:
        dir_list_3.append(file)


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