def read_notes():
    file_path = r"E:\notes.json" #TODO: make usable on any system!!
    try:
        with open(file_path, 'r') as file:
            data = file.read()
        return data
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return f"An error occurred: {e}"

def write_to_notes(text):
    file_path = r"E:\notes.json" #TODO: make usable on any system!!
    try:
        with open(file_path, 'a') as file:
            file.write(text)
            file.write("\n")
        return "Notes written successfully."
    except Exception as e:
        return f"An error occurred: {e}"