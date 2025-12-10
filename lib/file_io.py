def write_file(file_name, file_content):
    """Write `file_content` to `file_name`.txt.

    `file_name` may be a string or a Path-like object. The function
    ensures the file is opened with a `.txt` extension.
    """
    path = str(file_name) + ".txt"
    with open(path, 'w') as text_file:
        text_file.write(file_content)

def append_file(file_name, append_content):
    """Append `append_content` to `file_name`.txt.

    `file_name` may be a string or a Path-like object.
    """
    path = str(file_name) + ".txt"
    with open(path, 'a') as text_file:
        text_file.write(append_content)

def read_file(file_name):
    """Read and return the contents of `file_name`.txt.

    `file_name` may be a string or a Path-like object.
    """
    path = str(file_name) + ".txt"
    with open(path, 'r') as text_file:
        return text_file.read()
