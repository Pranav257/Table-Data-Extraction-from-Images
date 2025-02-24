# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1qoe8_XWMt0HCPRLxmDeKs5w1HOroROZW
"""

output_str = processor.decode(predictions[0], skip_special_tokens=True)


lines = [line for line in output_str.replace("<0x0A>", "\n").split("\n") if line.strip()]


processed_lines = []
current_line = ""
for line in lines:
    if "|" in line:
        if current_line:
            processed_lines.append(current_line)
        current_line = line
    else:
        current_line += " " + line
processed_lines.append(current_line)

# Format and print the processed lines
for line in processed_lines:
    print(line)