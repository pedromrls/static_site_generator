import os, shutil
from .copy_static import recursive_copy
from .gen_content import generate_pages_recursive

static_dir = "./static"
public_dir = "./public"
content_dir = "./content"
template = "./template.html"


def main():
    print("Deleting public directory...")
    if os.path.exists(public_dir):
        shutil.rmtree(public_dir)
    print("Copying static files to public directory...")
    recursive_copy(static_dir, public_dir)
    print("Generating page...")
    generate_pages_recursive(content_dir, template, public_dir)


if __name__ == "__main__":
    main()
