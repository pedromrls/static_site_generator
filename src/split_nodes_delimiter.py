from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        
        if delimiter not in node.text:
            new_nodes.append(node)
            continue
            
        if node.text.count(delimiter) % 2:
            raise Exception("Unclosed delimiter found")
            
        parts = node.text.split(delimiter)
        new_nodes.extend(
            TextNode(p, text_type if i % 2 else TextType.TEXT)
            for i, p in enumerate(parts)
        )
    return new_nodes
node = TextNode("This is text with a `code block` word", TextType.TEXT)

# Test Case 1: Basic case
node1 = TextNode("Here is `some code` and `normal text", TextType.TEXT)

# Test Case 2: Multiple delimiters
node2 = TextNode("Text `code` more `code again` end", TextType.TEXT)

# Test Case 3: No delimiters
node3 = TextNode("Just normal text", TextType.TEXT)

# Test Case 4: Invalid/unclosed delimiter
node4 = TextNode("Text with `unclosed code", TextType.TEXT)

new_nodes = split_nodes_delimiter([node1], "`", TextType.CODE)
print(new_nodes)