class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        if not self.props:
            return ""
        return " " + " ".join(f'{key}="{value}"' for key, value in self.props.items())

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value},{self.children}, {self.props})"


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if not self.value:
            raise ValueError("Invalid HTML: no value")
        if not self.tag:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def _children_to_html(self):
        if not self.children:
            raise ValueError("Invalid HTML: no children")
        return "".join(child.to_html() for child in self.children)

    def to_html(self):
        if not self.tag:
            raise ValueError("Invalid HTML: no tag")
        return f"<{self.tag}>{self._children_to_html()}</{self.tag}>"


node = ParentNode(
    "p",
    [
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
        ParentNode(
            "p",
            [
                LeafNode("b", "Bold text2"),
                LeafNode(None, "Normal text2"),
                LeafNode("i", "italic text2"),
                LeafNode(None, "Normal text2"),
            ],
        ),
    ],
)

# print(node.to_html())
