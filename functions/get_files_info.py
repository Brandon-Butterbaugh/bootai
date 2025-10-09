import os

def get_files_info(working_directory, directory="."):
    dir_path = os.path.join(working_directory, directory)
    if not os.path.abspath(dir_path).startswith(os.path.abspath(working_directory)):
        print(f'Error: Cannot list "{directory}" as it is outside the permitted working directory')
        return
    if not os.path.isdir(dir_path):
        print(f'Error: "{directory}" is not a directory')
        return
    for item in os.listdir(dir_path):
        inner_path = os.path.join(dir_path, item)
        if os.path.isfile(inner_path):
            print(f" - {item}: file_size={os.path.getsize(inner_path)}, is_dir=False")
        if os.path.isdir(inner_path):
            print(f" - {item}: file_size={os.path.getsize(inner_path)}, is_dir=True")