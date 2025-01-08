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
            raise ValueError("Invalid markdown, unclosed delimiter found")

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
        if not extract_markdown_images(node.text):
            new_nodes.append(node)
        else:
            param =  extract_markdown_images(node.text)
            for i in param:
                new_node = TextNode(i[0], TextType.IMAGE, i[1])
                new_nodes.append(new_node)
    return new_nodes
    


def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if not extract_markdown_links(node.text):
            new_nodes.append(node)
        else:
            param =  extract_markdown_links(node.text)
            for i in param:
                new_node = TextNode(i[0], TextType.LINK, i[1])
                new_nodes.append(new_node)
    return new_nodes
