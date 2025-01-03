from enum import Enum


class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"


class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        if not isinstance(text_type, TextType):
            raise ValueError(
                f"text_type must be an instance of TextType, got {text_type}"
            )
        self.url = url

    def __eq__(self, obj):
        return (
            self.text == obj.text
            and self.text_type == obj.text_type
            and self.url == obj.url
        )

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
