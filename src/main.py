from textnode import TextNode, TextType, text_node_to_html_node
from htmlnode import HTMLNode, LeafNode

prop_example2 = {
    "href": "https://www.google.com",
}


def main():
    cato = TextNode("This is a text node", TextType.IMAGE, "https://www.boot.dev")
    node = HTMLNode(
        "a",
        "This is a string representing the value of the HTML tag",
        [],
        prop_example2,
    )
    lfnode = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
    print(text_node_to_html_node(cato).to_html())


if __name__ == "__main__":
    main()
