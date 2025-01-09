import re


def markdown_to_blocks(markdown):
    return [block.strip() for block in re.split(r"\n\s*\n", markdown) if block.strip()]
