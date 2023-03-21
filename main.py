import re
import os
import threading
from PIL import Image
from concurrent.futures import ThreadPoolExecutor


def read_html_file(file_path):
    formatted_html_content = ""
    with open(file_path, "r") as file:
        lines = file.readlines()
    file.close()
    for line in lines:
        formatted_html_content += line.strip()
    return formatted_html_content


def find_html_tags(html):
    link_tag_regex = r'<link[^>]*>'
    script_tag_regex = r'<script[^>]*>'
    img_tag_regex = r'<img[^>]*>'
    found_links = re.findall(link_tag_regex, html)
    found_scripts = re.findall(script_tag_regex, html)
    found_imgs = re.findall(img_tag_regex, html)
    return [found_links, found_scripts, found_imgs]


def grab_attributes_links(found_links, found_scripts, found_imgs):
    regex = r'(?:href|src)=["\']?([^"\'>]+)["\']?'
    attributes_links = []

    for link_tags in found_links:
      for links in re.findall(regex, link_tags):
         attributes_links.append(links)

    for script_tags in found_scripts:
      for links in re.findall(regex, script_tags):
         attributes_links.append(links)

    for img_tags in found_imgs:
      for links in re.findall(regex, img_tags):
         attributes_links.append(links)

    return attributes_links


def grab_extensions(attributes_links):
    img_regex = r'.+\.(?:jpe?g|png|gif|bmp)'
    script_regex = r'.+\.(?:xml|py|js|c|css|php)'
    png_list = []
    script_list = []
    for file in attributes_links:
        if re.match(img_regex, file):
            png_list.append(file)
        elif re.match(script_regex, file):
            script_list.append(file)
    return png_list, script_list


def open_png(png_list):
    for img in png_list:
        if os.path.exists(img):
            size = os.path.getsize(os.path.abspath(img))
            print("==============================")
            print(f"[!] Thread: {threading.current_thread().name}")
            print(f"[+] Tamanho de {img} em bytes:", size)
            print("==============================\n\n\n")
        else:
            print(f"[!] Arquivo {img} não encontrado no diretório")
        image = Image.open(img)
        image.show()


def get_script_size(script_list):
    for script in script_list:
        if os.path.exists(script):
            size = os.path.getsize(script)
            print("==============================")
            print(f"[!] Thread: {threading.current_thread().name}")
            print(f"[+] Tamanho de {script} em bytes:", size)
            print(f"[*] Prévia do arquivo {script}:")
            show_file_preview(script)
            print("==============================\n\n\n")
        else:
            print(f"[!] Arquivo {script} não encontrado no diretório")


def show_file_preview(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        print("".join(lines[:5]))
        if len(lines) > 5:
            print(f"...mais {len(lines) - 5} linhas")


def main():
    dir = input(
        "[+] Entre com o caminho do arquivo html, contendo a extensão: ")
    html_file_content = read_html_file(dir)
    [found_links, found_scripts, found_imgs] = find_html_tags(
        html_file_content)
    attributes_links = grab_attributes_links(
        found_links, found_scripts, found_imgs)
    png_list, script_list = grab_extensions(attributes_links)
    print("==============================")
    print("[!] Lista de Imagens: ", png_list)
    print("[!] Lista de Scripts: ", script_list)
    print("==============================\n")

    with ThreadPoolExecutor(max_workers=3) as executor:
        t1 = executor.submit(get_script_size, script_list)
        t2 = executor.submit(open_png, png_list)


if __name__ == "__main__":
    main()
