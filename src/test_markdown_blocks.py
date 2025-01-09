import unittest
from markdown_blocks import markdown_to_blocks


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


if __name__ == "__main__":
    unittest.main()
