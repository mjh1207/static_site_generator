import os
import shutil


def delete_directory_contents(dir):
    if os.path.exists(dir):
        shutil.rmtree(dir)
    os.mkdir(dir)

def initialize_public_directory(current_path="", new_path=""):
    static_path = "./static"
    public_path = "./public"
    if not current_path:
        current_path = static_path
    if not new_path:
        new_path = public_path

    # List the contents of the static directory
    print(current_path)
    static_contents = os.listdir(current_path)
    for element in static_contents:
        static_item = os.path.join(current_path, element)
        public_item = os.path.join(new_path, element)
        if os.path.isdir(static_item):
            os.mkdir(public_item)
            initialize_public_directory(static_item, public_item)
        elif os.path.isfile(static_item):
            shutil.copy(static_item, public_item)