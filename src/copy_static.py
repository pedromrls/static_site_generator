import os
import shutil


def recursive_copy(src_dir, dst_dir):
    if not os.path.exists(src_dir):
        raise Exception(f"Source directory '{src_dir}' does not exist")

    if not os.path.exists(dst_dir):
        os.mkdir(dst_dir)

    for item in os.listdir(src_dir):
        src_path = os.path.join(src_dir, item)
        dst_path = os.path.join(dst_dir, item)
        if os.path.isfile(src_path):
            shutil.copy(src_path, dst_path)
        else:
            os.mkdir(dst_path)
            recursive_copy(src_path, dst_path)
