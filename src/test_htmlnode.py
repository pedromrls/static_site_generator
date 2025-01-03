import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):

    prop_example = {
        "href": "https://www.google.com",
        "target": "_blank",
    }
    prop_example2 = {
        "href": "https://www.google.com",
    }

    def test_to_html_not_implemented(self):
        with self.assertRaises(NotImplementedError):
            node = HTMLNode()
            node.to_html()

    def test_props_to_html(self):
        node = HTMLNode(
            props={
                "href": "https://www.google.com",
                "target": "_blank",
            }
        )
        self.assertEqual(
            ' href="https://www.google.com" target="_blank"', node.props_to_html()
        )

    def test_props_to_html_none(self):
        node = HTMLNode()
        self.assertEqual("", node.props_to_html())

    def test_props_to_html_emty_dict(self):
        node = HTMLNode(props={})
        self.assertEqual("", node.props_to_html())

    def test_repr(self):
        node = HTMLNode(
            "a",
            "This is a string representing the value of the HTML tag",
            [],
            self.prop_example2,
        )
        self.assertEqual(
            "HTMLNode(a, This is a string representing the value of the HTML tag,[], {'href': 'https://www.google.com'})",
            repr(node),
        )


if __name__ == "__main__":
    unittest.main()
