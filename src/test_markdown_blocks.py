import unittest
from markdown_blocks import markdown_to_blocks, block_to_block_type


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


if __name__ == "__main__":
    unittest.main()
