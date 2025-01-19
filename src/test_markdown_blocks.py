import unittest
from markdown_blocks import (
    markdown_to_html_node,
    markdown_to_blocks,
    block_to_block_type,
    block_paragraph,
    block_heading,
    block_code,
    block_ol,
    block_ul,
    block_quote,
)


class TestMarkdownBlocks(unittest.TestCase):
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

    def test_block_to_block_type_heading_1(self):
        text = "# This is a heading."
        self.assertEqual("heading", block_to_block_type(text))

    def test_block_to_block_type_heading_2(self):
        text = "## This is a heading."
        self.assertEqual("heading", block_to_block_type(text))

    def test_block_to_block_type_heading_3(self):
        text = "###### This is a heading."
        self.assertEqual("heading", block_to_block_type(text))

    def test_block_to_block_type_invalid_heading_1(self):
        text = "#This is an invalid heading."
        self.assertEqual("paragraph", block_to_block_type(text))

    def test_block_to_block_type_invalid_heading_2(self):
        text = "####### This is another invalid heading."
        self.assertEqual("paragraph", block_to_block_type(text))

    def test_block_to_block_type_code(self):
        text = '```print("this is a code block")```'
        self.assertEqual("code", block_to_block_type(text))

    def test_block_to_block_type_invalid_code(self):
        text = '```print("this is an invalid code block")'
        self.assertEqual("paragraph", block_to_block_type(text))

    def test_block_to_block_type_unordered_list_1(self):
        text = """* This is an unordered list.
* This is the second element.
* And this is the third one."""
        self.assertEqual("unordered_list", block_to_block_type(text))

    def test_block_to_block_type_unordered_list_2(self):
        text = """- This is another unordered list.
- This is the second element.
- And this is the third one."""
        self.assertEqual("unordered_list", block_to_block_type(text))

    def test_block_to_block_type_invalid_unordered_list_1(self):
        text = """-This is an invalid unordered list.
-This is the second element.
-And this is the third one."""
        self.assertEqual("paragraph", block_to_block_type(text))

    def test_block_to_block_type_ordered_list_1(self):
        text = """1. This is an ordered list.
2. This is the second element.
3. And this is the third one."""
        self.assertEqual("ordered_list", block_to_block_type(text))

    def test_block_to_block_type_invalid_ordered_list_1(self):
        text = """1.This is an ordered list.
2.This is the second element.
3.And this is the third one."""
        self.assertEqual("paragraph", block_to_block_type(text))

    def test_block_to_block_type_invalid_ordered_list_2(self):
        text = """1. This is an ordered list.
5. This is the second element.
25. And this is the third one."""
        self.assertEqual("paragraph", block_to_block_type(text))

    def test_block_to_block_type_invalid_ordered_list_3(self):
        # subject to change
        text = """1. This is an ordered list.
2.This is the second element.
3. And this is the third one."""
        self.assertEqual("paragraph", block_to_block_type(text))

    # markdown_to_htmlnode

    def test_paragraph(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p></div>",
        )

    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with *italic* text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_lists(self):
        md = """
- This is a list
- with items
- and *more* items

1. This is an `ordered` list
2. with items
3. and more items

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>This is a list</li><li>with items</li><li>and <i>more</i> items</li></ul><ol><li>This is an <code>ordered</code> list</li><li>with items</li><li>and more items</li></ol></div>",
        )

    def test_headings(self):
        md = """
# this is an h1

this is paragraph text

## this is an h2
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>this is an h1</h1><p>this is paragraph text</p><h2>this is an h2</h2></div>",
        )

    def test_blockquote(self):
        md = """
> This is a
> blockquote block

this is paragraph text

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a blockquote block</blockquote><p>this is paragraph text</p></div>",
        )


#     def test_codeblock(self):
#         md = """
# ```
# This is a code block
# ```

# this is paragraph text

# """

#         node = markdown_to_html_node(md)
#         html = node.to_html()
#         self.assertEqual(
#             html,
#             "<div><pre><code>This is a code block\n</code></pre><p>this is paragraph text</p></div>",
#         )


if __name__ == "__main__":
    unittest.main()
