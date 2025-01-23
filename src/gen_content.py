from .markdown_blocks import markdown_to_html_node
import os


def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line.strip("# ").strip()
    raise Exception("Title not found")


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path, "r") as f:
        src_file = f.read()
    with open(template_path, "r") as f:
        tmp_file = f.read()
    file_content = markdown_to_html_node(src_file)
    title = extract_title(src_file)
    html_file = tmp_file.replace("{{ Title }}", title).replace(
        "{{ Content }}", file_content.to_html()
    )
    with open(dest_path, "w") as f:
        print(html_file, file=f)


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    for item in os.listdir(dir_path_content):
        src_content = os.path.join(dir_path_content, item)
        dst_content = os.path.join(dest_dir_path, item)
        if os.path.isfile(src_content):
            generate_page(src_content, template_path, dst_content.replace("md", "html"))
        else:
            os.mkdir(dst_content)
            generate_pages_recursive(src_content, template_path, dst_content)
