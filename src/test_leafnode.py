import unittest

from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_to_html(self):
        node1 = LeafNode(None)
        self.assertRaises(ValueError, node1.to_html)
        node2 = LeafNode("p", "This is a paragraph element")
        self.assertEqual(node2.to_html(), "<p>This is a paragraph element</p>")
        node3 = LeafNode("a", "Link to website", {"class": "primary_link", "href": "https://www.google.com"})
        self.assertEqual(node3.to_html(), '<a class="primary_link" href="https://www.google.com">Link to website</a>')
        node4 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node4.to_html(), '<a href="https://www.google.com">Click me!</a>')