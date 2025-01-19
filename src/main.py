from textnode import TextNode, TextType, text_node_to_html_node
from htmlnode import HTMLNode, LeafNode
import os
import shutil

static_dir = "static"
public_dir = "public"


def copy_static(src_dir, dst_dir):
    if not os.path.exists(src_dir):
        raise Exception(f"Source directory '{src_dir}' does not exist")

    if not os.path.exists(dst_dir):
        os.mkdir(dst_dir)

    for item in os.listdir(src_dir):
        src_path = os.path.join(src_dir, item)
        dst_path = os.path.join(dst_dir, item)
        if os.path.isfile(src_path):
            shutil.copy(src_path, dst_path)
        else:
            os.mkdir(dst_path)
            copy_static(src_path, dst_path)


def main():
    if os.path.exists(public_dir):
        shutil.rmtree(public_dir)
    copy_static(static_dir, public_dir)


if __name__ == "__main__":
    main()
