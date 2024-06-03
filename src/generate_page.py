import os
from block_markdown import (
    markdown_to_blocks,
    markdown_to_html_node,
    block_to_block_type,
    block_type_heading
)

def extract_title(markdown):
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        if block_to_block_type(block) == block_type_heading and block.startswith("# "):
            return block[2:]
    raise Exception("All pages need a single h1 header")

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path.replace(".md", ".html")} using {template_path}")

    # Get page contents
    from_contents = ""
    with open(from_path, 'r') as from_file:
        from_contents = from_file.read()
    
    # Get template contents
    template_contents = ""
    with open(template_path, "r") as template_file:
        template_contents = template_file.read()

    # Convert content to html and get title
    html_content = markdown_to_html_node(from_contents)
    html_content = html_content.to_html()
    title = extract_title(from_contents)
    
    # Replace title and content in template
    template_contents = template_contents.replace("{{ Title }}", title)
    template_contents = template_contents.replace("{{ Content }}", html_content)

    # Write contents to new html file in dest_path
    dest_dir = os.path.dirname(dest_path)
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
    with open(dest_path.replace(".md", ".html"), "w") as new_file:
        new_file.write(template_contents)
    
def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    dir_items = os.listdir(dir_path_content)
    for item in dir_items:
        source_path = f"{dir_path_content}/{item}"
        dest_path = f"{dest_dir_path}/{item}"
        if os.path.isdir(f"{dir_path_content}/{item}"):
            generate_pages_recursive(source_path, template_path, dest_path)
        else:
            generate_page(source_path, template_path, dest_path)