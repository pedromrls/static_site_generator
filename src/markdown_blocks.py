import re


def markdown_to_blocks(markdown):
    return [block.strip() for block in re.split(r"\n\s*\n", markdown) if block.strip()]


def block_to_block_type(block):
    if re.match(r"^#{1,6} ", block):
        return "heading"
    elif re.match(r"^```(.*?)```$", block):
        return "code"
    elif block[0] == ">":
        return "quote"
    elif re.match(r"^[\*\-] ", block):
        lines = block.split("\n")
        for line in lines:
            if not re.match(r"^[\*\-] ", line):
                return "paragraph"
        return "unordered_list"
    elif re.match(r"^\d+\. ", block):
        # subject to change

        lines = block.split("\n")
        if lines[0][0] != "1":
            return "paragraph"
        for i, v in enumerate(lines):
            if v[:3] != f"{i + 1}. ":
                return "paragraph"
        return "ordered_list"
    else:
        return "paragraph"
