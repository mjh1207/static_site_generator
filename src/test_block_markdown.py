import unittest
from block_markdown import (
    markdown_to_blocks,
    block_to_block_type,
    block_type_paragraph,
    block_type_heading,
    block_type_code,
    block_type_quote,
    block_type_unordered_list,
    block_type_ordered_list
)

class BlockMarkdown(unittest.TestCase):
    def test_markdown_to_blocks(self):
        markdown = """This is **bolded** paragraph

This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line




* This is a list
* with items



"""
        markdown_blocks = markdown_to_blocks(markdown)
        self.assertListEqual(markdown_blocks, ['This is **bolded** paragraph', 'This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line', '* This is a list\n* with items'])

    def test_block_to_block_type(self):
        block = "# My Heading"
        self.assertEqual(block_to_block_type(block), block_type_heading)
        block = "```\nconsole.log('hello world')\n```"
        self.assertEqual(block_to_block_type(block), block_type_code)
        block = ">some quote\n>in a block"
        self.assertEqual(block_to_block_type(block), block_type_quote)
        block = "* unordered list item 1\n* unordered list item 2"
        self.assertEqual(block_to_block_type(block), block_type_unordered_list)
        block = "1. ordered list item 1\n2. ordered list item 2"
        self.assertEqual(block_to_block_type(block), block_type_ordered_list)
        block = "Some paragraph"
        self.assertEqual(block_to_block_type(block), block_type_paragraph)