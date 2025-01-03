from textnode import TextNode, TextType
from htmlnode import HTMLNode
from leafnode import LeafNode

prop_example2 = {
    "href": "https://www.google.com",
}


def main():
    cato = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
    node = HTMLNode(
        "a",
        "This is a string representing the value of the HTML tag",
        [],
        prop_example2,
    )
    lfnode = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
    print(repr(cato))
    print(repr(node))
    print(lfnode.to_html())


if __name__ == "__main__":
    main()
