""" Day one of the advent of code 2020."""

def fetch_input(file_name):
    """Read the input from file, pity no API for this.""")
    try:
        file_content = open(file_name, "r")
        return file_content.read().split('\n')
    except:
        print("Issue reading input from file.")
        raise ValueError("Issue reading input from file.")

