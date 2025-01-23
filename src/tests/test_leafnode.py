import unittest

from src.htmlnode import LeafNode


class TestLeafNode(unittest.TestCase):

    prop_example = {
        "href": "https://www.google.com",
    }
    prop_example2 = {
        "href": "https://www.google.com",
        "target": "_blank",
    }
    paragraph = "This is a paragraph of text."

    text = "Click me!"

    def test_empty_value(self):

        node = LeafNode(None, "")
        self.assertEqual("", node.to_html())

    def test_empty_value_raises_error2(self):
        with self.assertRaises(ValueError):
            node = LeafNode(None, None)
            node.to_html()

    def test_to_html_none_tag(self):
        node = LeafNode(None, self.paragraph)
        self.assertEqual("This is a paragraph of text.", node.to_html())

    def test_to_html_single_prop(self):
        node = LeafNode("a", self.text, self.prop_example)
        self.assertEqual(
            '<a href="https://www.google.com">Click me!</a>', node.to_html()
        )

    def test_to_html_multiple_props(self):
        node = LeafNode("a", self.text, self.prop_example2)
        self.assertEqual(
            '<a href="https://www.google.com" target="_blank">Click me!</a>',
            node.to_html(),
        )

    def test_to_html_prop_no_tag(self):
        node = LeafNode(None, self.text)
        self.assertEqual("Click me!", node.to_html())


if __name__ == "__main__":
    unittest.main()
