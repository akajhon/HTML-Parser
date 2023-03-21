# HTML-Parser

A Python program created for the Distributed Systems course that allows extracting links from an HTML file, as well as "href" and "src" attributes from "link", "script", and "img" tags. Additionally, the program can show information about the size of the found files and previews of code files.

## 🚀 Usage

Before using this script, make sure you have installed:

- Python 3+
- Python libraries: re, os, threading, PIL, and concurrent.futures

Just run the following command at the root of project:

```sh
python3 main.py
```

## 🤔 How to use

1. Provide the path to the HTML file you want to analyze and press Enter.

2. Then, separate lists of image links and script links found will be displayed.

3. For each image found, the program will display the file size in bytes and show the image in a new window.

4. For each script found, the program will display the file size in bytes and a preview of the first five lines of the file.

5. After all images and scripts are processed, the program will terminate.

## 🧑‍💻 Authors

**Hugo Linhares**

- Github: [@hugolinhareso](https://github.com/hugolinhareso)

**João Pedro**

- Github: [@akajhon](https://github.com/akajhon)
