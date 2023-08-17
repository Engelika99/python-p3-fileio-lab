def write_file(file_name, file_content):
    file_name_str = str(file_name) + '.txt'
    with open(file_name_str, 'w') as text_file:
        text_file.write(file_content)

def append_file(file_name, append_content):
    file_name_str = str(file_name) + '.txt'
    with open(file_name_str, 'a') as text_file:
        text_file.write(append_content)


def read_file(file_name):
    file_name_str = str(file_name) + '.txt'
    with open(file_name_str, 'r') as text_file:
        content = text_file.read()
    return content
