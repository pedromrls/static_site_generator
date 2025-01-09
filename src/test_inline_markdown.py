import unittest
from inline_markdown import (
    split_nodes_delimiter,
    extract_markdown_images,
    extract_markdown_links,
    split_nodes_link,
    split_nodes_image,
    text_to_textnodes,
    markdown_to_blocks,
)
from textnode import TextNode, TextType


class TestSplitDelimiter(unittest.TestCase):
    def test_delim_bold(self):
        node = TextNode("This is text with a **bolded** word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bolded", TextType.BOLD),
                TextNode(" word", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_delim_bold_double(self):
        node = TextNode(
            "This is text with a **bolded** word and **another**", TextType.TEXT
        )
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bolded", TextType.BOLD),
                TextNode(" word and ", TextType.TEXT),
                TextNode("another", TextType.BOLD),
            ],
            new_nodes,
        )

    def test_delim_bold_multiword(self):
        node = TextNode(
            "This is text with a **bolded word** and **another**", TextType.TEXT
        )
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bolded word", TextType.BOLD),
                TextNode(" and ", TextType.TEXT),
                TextNode("another", TextType.BOLD),
            ],
            new_nodes,
        )

    def test_delim_italic(self):
        node = TextNode("This is text with an *italic* word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "*", TextType.ITALIC)
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_delim_bold_and_italic(self):
        node = TextNode("**bold** and *italic*", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        new_nodes = split_nodes_delimiter(new_nodes, "*", TextType.ITALIC)
        self.assertListEqual(
            [
                TextNode("bold", TextType.BOLD),
                TextNode(" and ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
            ],
            new_nodes,
        )

    def test_delim_code(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" word", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_assert_unclosed_delimiter(self):
        with self.assertRaises(ValueError):
            node = TextNode("This is text with a `code block word", TextType.TEXT)
            new_node = split_nodes_delimiter([node], "`", TextType.CODE)

    def test_extract_markdown_links(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        self.assertEqual(
            [
                ("to boot dev", "https://www.boot.dev"),
                ("to youtube", "https://www.youtube.com/@bootdotdev"),
            ],
            extract_markdown_links(text),
        )

    def test_extract_markdown_images(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        self.assertEqual(
            [
                ("rick roll", "https://i.imgur.com/aKaOqIh.gif"),
                ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg"),
            ],
            extract_markdown_images(text),
        )

    # test_split_nodes_image

    def test_image_simple_case(self):
        node = TextNode("text ![image](test.png) text", TextType.TEXT)
        expected = [
            TextNode("text ", TextType.TEXT),
            TextNode("image", TextType.IMAGE, "test.png"),
            TextNode(" text", TextType.TEXT),
        ]
        self.assertEqual(expected, split_nodes_image([node]))

    def test_image_multiple(self):
        node = TextNode("![1](1.png) mid ![2](2.png)", TextType.TEXT)
        expected = [
            TextNode("1", TextType.IMAGE, "1.png"),
            TextNode(" mid ", TextType.TEXT),
            TextNode("2", TextType.IMAGE, "2.png"),
        ]
        self.assertEqual(expected, split_nodes_image([node]))

    def test_image_no_images(self):
        node = TextNode("just plain text", TextType.TEXT)
        expected = [node]
        self.assertEqual(expected, split_nodes_image([node]))

    def test_image_empty_sections(self):
        node = TextNode("![alt](test.png)", TextType.TEXT)
        expected = [TextNode("alt", TextType.IMAGE, "test.png")]
        self.assertEqual(expected, split_nodes_image([node]))

    # test_split_nodes_link

    def test_link_simple_case(self):
        node = TextNode("text [link](test.com) text", TextType.TEXT)
        expected = [
            TextNode("text ", TextType.TEXT),
            TextNode("link", TextType.LINK, "test.com"),
            TextNode(" text", TextType.TEXT),
        ]
        self.assertEqual(expected, split_nodes_link([node]))

    def test_link_multiple(self):
        node = TextNode("[1](1.com) mid [2](2.com)", TextType.TEXT)
        expected = [
            TextNode("1", TextType.LINK, "1.com"),
            TextNode(" mid ", TextType.TEXT),
            TextNode("2", TextType.LINK, "2.com"),
        ]
        self.assertEqual(expected, split_nodes_link([node]))

    def test_link_no_links(self):
        node = TextNode("just plain text", TextType.TEXT)
        expected = [node]
        self.assertEqual(expected, split_nodes_link([node]))

    def test_link_empty_sections(self):
        node = TextNode("[alt](test.png)", TextType.TEXT)
        expected = [TextNode("alt", TextType.LINK, "test.png")]
        self.assertEqual(expected, split_nodes_link([node]))

    # test texnodes
    def test_handles_simple_bold_and_italic(self):
        text = "This is **bold** and *italic*"
        node = text_to_textnodes(text)
        self.assertEqual(
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("bold", TextType.BOLD),
                TextNode(" and ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
            ],
            node,
        )

    def test_parses_multiple_formats(self):
        text = "**bold**, *italic*, `code block`, and ![alt text](image_url)"
        node = text_to_textnodes(text)
        self.assertEqual(
            [
                TextNode("bold", TextType.BOLD),
                TextNode(", ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(", ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(", and ", TextType.TEXT),
                TextNode("alt text", TextType.IMAGE, "image_url"),
            ],
            node,
        )

    def test_handles_plain_text_only(self):
        text = "Just plain text with no formatting."
        node = text_to_textnodes(text)
        self.assertEqual(
            [
                TextNode("Just plain text with no formatting.", TextType.TEXT),
            ],
            node,
        )

    def test_returns_empty_list_for_empty_input(self):
        text = ""
        node = text_to_textnodes(text)
        self.assertEqual(
            [],
            node,
        )

    def test_image_without_alt_text(self):
        text = "![](image_url)"
        node = text_to_textnodes(text)
        self.assertEqual(
            [
                TextNode("", TextType.IMAGE, "image_url"),
            ],
            node,
        )

    def test_incomplete_formatting(self):
        with self.assertRaises(ValueError) as context:
            text = "This is **bold and *italic but unclosed."
            node = text_to_textnodes(text)
        self.assertEqual(
            str(context.exception),
            "Unclosed formatting detected for '**' starting at position 8",
        )

    def test_text_with_extra_spaces(self):
        text = "  **bold**   "
        node = text_to_textnodes(text)
        self.assertEqual(
            [
                TextNode("  ", TextType.TEXT),
                TextNode("bold", TextType.BOLD),
                TextNode("   ", TextType.TEXT),
            ],
            node,
        )

    def test_multiple_images_in_text(self):
        text = "Here is one image: ![first image](url1) and another: ![second image](url2)."
        node = text_to_textnodes(text)
        self.assertEqual(
            [
                TextNode("Here is one image: ", TextType.TEXT),
                TextNode("first image", TextType.IMAGE, "url1"),
                TextNode(" and another: ", TextType.TEXT),
                TextNode("second image", TextType.IMAGE, "url2"),
                TextNode(".", TextType.TEXT),
            ],
            node,
        )

    def test_code_block_with_symbols(self):
        text = "Look at this `code_block_with_symbols!@#$%^&()` for fun."
        node = text_to_textnodes(text)
        self.assertEqual(
            [
                TextNode("Look at this ", TextType.TEXT),
                TextNode("code_block_with_symbols!@#$%^&()", TextType.CODE),
                TextNode(" for fun.", TextType.TEXT),
            ],
            node,
        )

    def test_mixed_format_with_no_spaces(self):
        text = "**bold***italic*`code_block`no_spaces!"
        node = text_to_textnodes(text)
        self.assertEqual(
            [
                TextNode("bold", TextType.BOLD),
                TextNode("italic", TextType.ITALIC),
                TextNode("code_block", TextType.CODE),
                TextNode("no_spaces!", TextType.TEXT),
            ],
            node,
        )

    def test_unusual_but_valid_markdown(self):
        text = "Text ![alt](url) **bold**![alt2](url2)."
        node = text_to_textnodes(text)
        self.assertEqual(
            [
                TextNode("Text ", TextType.TEXT),
                TextNode("alt", TextType.IMAGE, "url"),
                TextNode(" ", TextType.TEXT),
                TextNode("bold", TextType.BOLD),
                TextNode("alt2", TextType.IMAGE, "url2"),
                TextNode(".", TextType.TEXT),
            ],
            node,
        )

    def test_markdown_blocks_header_only(self):
        text = """# This is a heading"""
        self.assertEqual(["# This is a heading"], markdown_to_blocks(text))

    def test_markdown_blocks_header_only_with_whitespace(self):
        text = """ # This is a heading """
        self.assertEqual(["# This is a heading"], markdown_to_blocks(text))

    def test_markdown_blocks_header_only_with_empty_lines(self):
        text = """
        # This is a heading
        
        """
        self.assertEqual(["# This is a heading"], markdown_to_blocks(text))

    def test_markdown_blocks_header_and_paragraph(self):
        text = """
        # This is a heading.

        And this is a paragraph.
        """
        self.assertEqual(
            ["# This is a heading.", "And this is a paragraph."],
            markdown_to_blocks(text),
        )

    def test_markdown_blocks_all_blocks(self):
        text = """
        # This is a heading.

        And this is a paragraph.

        * This are bullet points.\n* The previous one was the first and this is the second.\n* Finally, this is the third.
        """
        self.assertEqual(
            [
                "# This is a heading.",
                "And this is a paragraph.",
                "* This are bullet points.\n* The previous one was the first and this is the second.\n* Finally, this is the third.",
            ],
            markdown_to_blocks(text),
        )

    def test_markdown_blocks_all_blocks_extra_empty_lines(self):
        text = """
        # This is a heading.\n

        And this is a paragraph.\n

        * This are bullet points.\n* The previous one was the first and this is the second.\n* Finally, this is the third.
        """
        self.assertEqual(
            [
                "# This is a heading.",
                "And this is a paragraph.",
                "* This are bullet points.\n* The previous one was the first and this is the second.\n* Finally, this is the third.",
            ],
            markdown_to_blocks(text),
        )


if __name__ == "__main__":
    unittest.main()
