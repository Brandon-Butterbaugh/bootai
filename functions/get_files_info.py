import os

def get_files_info(working_directory, directory="."):
    dir_path = os.path.abspath(os.path.join(working_directory, directory))
    if not os.path.abspath(dir_path).startswith(os.path.abspath(working_directory)):
        return(f'Error: Cannot list "{directory}" as it is outside the permitted working directory')
        
    if not os.path.isdir(dir_path):
        return(f'Error: "{directory}" is not a directory')
        
    try:
        files = []
        for item in os.listdir(dir_path):
            inner_path = os.path.join(dir_path, item)
            is_dir = os.path.isdir(inner_path)
            files.append(f" - {item}: file_size={os.path.getsize(inner_path)}, is_dir={is_dir}")
        return "\n".join(files)
    except Exception as e:
        return f"Error listing files: {e}"