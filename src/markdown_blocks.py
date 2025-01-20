import re
from htmlnode import ParentNode
from inline_markdown import text_to_textnodes
from textnode import text_node_to_html_node

block_heading = "heading"
block_code = "code"
block_quote = "quote"
block_ul = "unordered_list"
block_ol = "ordered_list"
block_paragraph = "paragraph"


def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    filtered_blocks = []
    for block in blocks:
        if block == "":
            continue
        # Preserve formatting for code blocks
        if block.startswith("```") and block.endswith("```"):
            filtered_blocks.append(block)
        else:
            filtered_blocks.append(block.strip())
    return filtered_blocks


def block_to_block_type(block):
    lines = block.split("\n")

    if re.match(r"^#{1,6} ", block):
        return block_heading
    if block.strip().startswith("```") and block.strip().endswith("```"):
        return block_code
    if block[0] == ">":
        return block_quote
    if re.match(r"^[\*\-] ", block):
        for line in lines:
            if not re.match(r"^[\*\-] ", line):
                return block_paragraph
        return block_ul
    if re.match(r"^\d+\. ", block):
        # subject to change
        if lines[0][0] != "1":
            return block_paragraph
        for i, v in enumerate(lines):
            if v[:3] != f"{i + 1}. ":
                return block_paragraph
        return block_ol
    return block_paragraph


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        html_node = block_to_htmlnode(block)
        children.append(html_node)
    return ParentNode("div", children, None)


def block_to_htmlnode(block):
    block_type = block_to_block_type(block)
    if block_type == block_heading:
        return heading_to_htmlnode(block)
    elif block_type == block_code:
        return code_to_htmlnode(block)
    elif block_type == block_quote:
        return quote_to_htmlnode(block)
    elif block_type == block_ol:
        return olist_to_htmlnode(block)
    elif block_type == block_ul:
        return ulist_to_htmlnode(block)
    elif block_type == block_paragraph:
        return paragraph_to_htmlnode(block)
    raise ValueError("Invalid block type")


def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    return [text_node_to_html_node(text_node) for text_node in text_nodes]


def heading_to_htmlnode(block):
    level = block.count("#")
    if level + 1 >= len(block):
        raise ValueError(f"Invalid heading level: {level}")
    heading_content = block[level + 1 :]
    heading_tag = f"h{level}"
    children = text_to_children(heading_content)
    return ParentNode(heading_tag, children)


def code_to_htmlnode(block):
    if not block.startswith("```") or not block.endswith("```"):
        raise ValueError("Invalid code block")
    text = block[4:-3]
    children = text_to_children(text)
    code = ParentNode("code", children)
    return ParentNode("pre", code)


def quote_to_htmlnode(block):
    lines = block.split("\n")
    new_lines = []
    for line in lines:
        if not line.startswith(">"):
            raise ValueError("Invalid quote block")
        new_lines.append(line[1:].strip())
    text = " ".join(new_lines)
    children = text_to_children(text)
    return ParentNode("blockquote", children)


def olist_to_htmlnode(block):
    items = block.split("\n")
    html_items = []
    for item in items:
        children = text_to_children(item[3:])
        html_items.append(ParentNode("li", children))
    return ParentNode("ol", html_items)


def ulist_to_htmlnode(block):
    items = block.split("\n")
    html_items = []
    for item in items:
        children = text_to_children(item[2:])
        html_items.append(ParentNode("li", children))
    return ParentNode("ul", html_items)


def paragraph_to_htmlnode(block):
    paragraph = " ".join(block.split("\n"))
    children = text_to_children(paragraph)
    return ParentNode("p", children)
