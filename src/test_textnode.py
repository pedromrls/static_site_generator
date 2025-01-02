import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_non_eq_text(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is not a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)
    
    def test_non_eq_text_type(self):
        node = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
        node2 = TextNode("This is a text node", TextType.ITALIC, "https://www.boot.dev")
        self.assertNotEqual(node, node2)

    def test_non_eq_url(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD,"https://www.boot.dev")
        self.assertNotEqual(node, node2)

    def test_invalid_text_type_raises_attribute_error(self):
        with self.assertRaises(AttributeError):
            node = TextNode("This is a text node", TextType.bold) 

    def test_none_url(self):
        node = TextNode("This is a text node", TextType.BOLD, None)
        self.assertIsNone(node.url)   
        
    def test_repr(self):
        node = TextNode("This is a text node", TextType.NORMAL, "https://www.boot.dev")
        self.assertEqual(
            "TextNode(This is a text node, normal, https://www.boot.dev)", repr(node)
        )

if __name__ == "__main__":
    unittest.main()
