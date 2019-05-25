#!/usr/bin/python3
def text_indentation(text):
    delims = ('.', '?', ':')
    if not isinstance(text, str) or text is None:
        raise TypeError("text must be a string")
    for i in range(len(text)):
        if text[i] in delims:
            print("\n")
            i += 1
        else:
            if text[i - 1] in delims and text[i] == " ":
                continue
            print(text[i], end="")
