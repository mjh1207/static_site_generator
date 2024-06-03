from generate_page import generate_pages_recursive

from copy_directory import (
    delete_directory_contents,
    initialize_public_directory
)


def main():
    delete_directory_contents('./public')
    initialize_public_directory()
    generate_pages_recursive("./content", "./template.html", "./public")
    

main()