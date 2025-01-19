import os, shutil
from copy_static import recursive_copy

static_dir = "./static"
public_dir = "./public"


def main():
    if os.path.exists(public_dir):
        shutil.rmtree(public_dir)
    recursive_copy(static_dir, public_dir)


if __name__ == "__main__":
    main()
