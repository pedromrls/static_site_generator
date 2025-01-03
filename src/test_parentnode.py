import unittest
from htmlnode import ParentNode, LeafNode


class TestParentNode(unittest.TestCase):
    simple = (
        "p",
        [LeafNode("b", "Bold text")],
    )
    multi_ch = (
        "p",
        [
            LeafNode("b", "Bold text"),
            LeafNode("b", "Bold text"),
            LeafNode("i", "italic text"),
            LeafNode("i", "Italic text"),
        ],
    )
    multi_ch_no_tag = (
        "p",
        [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
        ],
    )
    nested = (
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

    def test_basic_parentnode(self):
        node = ParentNode(*self.simple)
        self.assertEqual("<p><b>Bold text</b></p>", node.to_html())

    def test_parentnode_multi_children(self):
        node = ParentNode(*self.multi_ch)
        self.assertEqual(
            "<p><b>Bold text</b><b>Bold text</b><i>italic text</i><i>Italic text</i></p>",
            node.to_html(),
        )

    def test_parentnode_none_tag(self):
        with self.assertRaises(ValueError):
            node = ParentNode(None, self.multi_ch[1])
            node.to_html()

    def test_parentnode_no_children(self):
        with self.assertRaises(ValueError):
            node = ParentNode(self.multi_ch[0], None)
            node.to_html()

    def test_parentnode_nested_no_tag(self):
        node = ParentNode(*self.nested)
        self.assertEqual(
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text<p><b>Bold text2</b>Normal text2<i>italic text2</i>Normal text2</p></p>",
            node.to_html(),
        )

    def test_parentnode_empty_str_tag(self):
        with self.assertRaises(ValueError):
            node = ParentNode("", self.multi_ch[1])
            node.to_html()
