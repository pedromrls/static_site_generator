from markdown_blocks import markdown_to_html_node

def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line.strip('# ').strip()
    raise Exception("Title not found")

def generate_page(from_path, dest_path, template_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path, 'r') as f:
        src_file = f.read()
    with open(template_path, 'r') as f:
        tmp_file = f.read()
    file_content = markdown_to_html_node(src_file)
    title = extract_title(src_file)
    html_file = tmp_file.replace("{{ Title }}", title).replace("{{ Content }}", file_content.to_html())
    with open(dest_path, 'w') as f:
        print(html_file, file=f)