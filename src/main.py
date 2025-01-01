from textnode import TextNode, TextType


def main():
    cato = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
    gato = TextNode("This is a text node", TextType.BOLD, None)
    print(repr(cato))
    print(repr(gato))


if __name__ == "__main__":
    main()
