from textnode import TextNode, TextType, text_node_to_html_node
from htmlnode import HTMLNode, LeafNode
import os
import shutil

static_dir = "static"
public_dir = "public"

def list_files(static_dir):
    file_list = []
    if os.path.isfile(static_dir):
        file_list.append(static_dir)
    else: 
        for link in os.listdir(static_dir):
            new_filepath = os.path.join(static_dir, link)
            if os.path.isfile(link):
                file_list.append(new_filepath)
            else:
                file_list.extend(list_files(new_filepath))
    return file_list

def cleaner():
    
    if not os.path.exists(static_dir):
        raise Exception(f"No {static_dir}directory found")
    if os.path.exists(public_dir):
        shutil.rmtree(public_dir)
    file_list = list_files(static_dir)
    print(file_list)


def main():
    cleaner()
    pass
if __name__ == "__main__":
    main()
