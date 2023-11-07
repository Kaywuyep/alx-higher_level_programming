#!/usr/bin/python3
"""a simple module"""


def append_after(filename="", search_string="", new_string=""):
    """Inserts text after each line containing a given string in a file."""
    updated_text = []

    with open(filename, "r") as f:
        for line in f:
            updated_text.append(line)
            if search_string in line:
                updated_text.append(new_string)

    with open(filename, "w") as f:
        f.writelines(updated_text)
