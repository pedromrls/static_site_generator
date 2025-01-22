import os, shutil
from copy_static import recursive_copy, generate_page

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
    generate_page(os.path.join(content_dir, "/index.md"), os.path.join(public_dir, "/index.html", template))


if __name__ == "__main__":
    main()
