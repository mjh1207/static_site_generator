import unittest
from inline_markdown import (
    split_nodes_delimiter,
    extract_markdown_images,
    extract_markdown_links    
)
from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_code,
    text_type_italic
)

class InlineMakrdown(unittest.TestCase):
    def test_bold(self):
        node1 = TextNode("This text has **bold** words", text_type_text)
        node2 = TextNode("This text has no bold words", text_type_text)
        new_nodes = split_nodes_delimiter([node1, node2], "**", text_type_bold)
        self.assertListEqual(
            [
            TextNode("This text has ", text_type_text),
            TextNode("bold", text_type_bold),
            TextNode(" words", text_type_text),
            TextNode("This text has no bold words", text_type_text),
            ],
            new_nodes
        )

    def test_bold_multiple(self):
        node1 = TextNode("This **text** has multiple **bold** words", text_type_text)
        new_nodes = split_nodes_delimiter([node1], "**", text_type_bold)
        self.assertListEqual([
            TextNode("This ", text_type_text),
            TextNode("text", text_type_bold),
            TextNode(" has multiple ", text_type_text),
            TextNode("bold", text_type_bold),
            TextNode(" words", text_type_text)
        ],
          new_nodes
        )
    def test_bold_several_words(self):
        node1 = TextNode("This text has **multiple bold** words", text_type_text)
        new_nodes = split_nodes_delimiter([node1], "**", text_type_bold)
        self.assertListEqual([
            TextNode("This text has ", text_type_text),
            TextNode("multiple bold", text_type_bold),
            TextNode(" words", text_type_text)
        ],
          new_nodes
        )

    def test_italic(self):
        node1 = TextNode("This text has *italic* words", text_type_text)
        new_nodes = split_nodes_delimiter([node1], "*", text_type_italic)
        self.assertListEqual(
            [
            TextNode("This text has ", text_type_text),
            TextNode("italic", text_type_italic),
            TextNode(" words", text_type_text),
            ],
            new_nodes
        )

    def test_code(self):
        node1 = TextNode("This text has `code` words", text_type_text)
        new_nodes = split_nodes_delimiter([node1], "`", text_type_code)
        self.assertListEqual(
            [
            TextNode("This text has ", text_type_text),
            TextNode("code", text_type_code),
            TextNode(" words", text_type_text),
            ],
            new_nodes
        )

    def test_invalid_text_node(self):
        node1 = TextNode("This text has **invalid markup syntax", text_type_text)
        self.assertRaises(Exception, lambda: split_nodes_delimiter([node1], "**", text_type_bold))
                          

    def test_extract_markdown_image(self):
        text = "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and ![another](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png)"
        extracted_images = extract_markdown_images(text)
        self.assertEqual(extracted_images, [
            ("image", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"),
            ("another", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png")
        ])
    
    def test_extract_markdown_link(self):
        text = "This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)"
        extracted_links = extract_markdown_links(text)
        self.assertEqual(extracted_links, [
            ("link", "https://www.example.com"),
            ("another", "https://www.example.com/another")
        ])