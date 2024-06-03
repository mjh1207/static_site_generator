from generate_page import generate_page

from copy_directory import (
    delete_directory_contents,
    initialize_public_directory
)


def main():
    delete_directory_contents('./public')
    initialize_public_directory()
    generate_page("./content/index.md", "./template.html", "./public/index.html")
    

main()