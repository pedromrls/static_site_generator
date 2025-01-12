import re
from htmlnode import HTMLNode, LeafNode, ParentNode
from inline_markdown import *

block_heading = "heading"
block_code = "code"
block_quote = "quote"
block_ul = "unordered_list"
block_ol = "ordered_list"
block_paragraph = "paragraph"
heading_dict = {
    "#": "h1",
    "##": "h2",
    "###": "h3",
    "####": "h4",
    "#####": "h5",
    "######": "h6",
}


def markdown_to_blocks(markdown):
    return [block.strip() for block in re.split(r"\n\s*\n", markdown) if block.strip()]


def block_to_block_type(block):
    if re.match(r"^#{1,6} ", block):
        return block_heading
    elif re.match(r"^```(.*?)```$", block):
        return block_code
    elif block[0] == ">":
        return block_quote
    elif re.match(r"^[\*\-] ", block):
        lines = block.split("\n")
        for line in lines:
            if not re.match(r"^[\*\-] ", line):
                return block_paragraph
        return block_ul
    elif re.match(r"^\d+\. ", block):
        # subject to change

        lines = block.split("\n")
        if lines[0][0] != "1":
            return block_paragraph
        for i, v in enumerate(lines):
            if v[:3] != f"{i + 1}. ":
                return block_paragraph
        return block_ol
    else:
        return block_paragraph


def markdown_to_html_node(markdown):
    # 1. split the markdown
    blocks = markdown_to_blocks(markdown)
    # 2. Process for each block
    for block in blocks:
        # 2.1. identify the kind of block

        block_type = block_to_block_type(block)
        # 2.2. Create a corresponding HTMLNode for that block type
        if block_type == block_heading:

            count = block.count("#")
            heading_tag = heading_dict("#" * count)
            heading_content = block[count:].strip()
            parent = ParentNode(heading_tag, text_to_textnodes(heading_content))

        elif block_type == block_code:
            pass
        elif block_type == block_quote:
            pass
        elif block_type == block_ol:
            pass
        elif block_type == block_ul:
            pass
        elif block_type == block_paragraph:
            pass


def text_to_children(text):
    pass
