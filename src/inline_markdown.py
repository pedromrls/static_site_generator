import re
from textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        if delimiter not in node.text:
            new_nodes.append(node)
            continue

        if node.text.count(delimiter) % 2:
            raise ValueError(
                f"Unclosed formatting detected for '{delimiter}' starting at position {node.text.index(delimiter)}"
            )

        parts = node.text.split(delimiter)

        new_nodes.extend(
            TextNode(p, text_type if i % 2 else TextType.TEXT)
            for i, p in enumerate(parts)
            if p != ""
        )
    return new_nodes


def extract_markdown_images(text):
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)


def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)


def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:

        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        images = extract_markdown_images(node.text)
        current_text = node.text
        for alt, link in images:
            before, *remainder = current_text.split(f"![{alt}]({link})", 1)
            if before:
                new_nodes.append(TextNode(before, node.text_type))
            new_nodes.append(TextNode(alt, TextType.IMAGE, link))
            current_text = remainder[0] if remainder else ""
        if current_text:
            new_nodes.append(TextNode(current_text, node.text_type))

    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        links = extract_markdown_links(node.text)
        current_text = node.text
        for alt, link in links:
            before, *remainder = current_text.split(f"[{alt}]({link})", 1)
            if before:
                new_nodes.append(TextNode(before, node.text_type))
            new_nodes.append(TextNode(alt, TextType.LINK, link))
            current_text = remainder[0] if remainder else ""
        if current_text:
            new_nodes.append(TextNode(current_text, node.text_type))

    return new_nodes


def text_to_textnodes(text):
    node = TextNode(text, TextType.TEXT)
    bold = split_nodes_delimiter([node], "**", TextType.BOLD)
    italic = split_nodes_delimiter(bold, "*", TextType.ITALIC)
    code = split_nodes_delimiter(italic, "`", TextType.CODE)
    link = split_nodes_link(code)
    image = split_nodes_image(link)

    return image
