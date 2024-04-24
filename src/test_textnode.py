import unittest

from textnode import TextNode

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)
    
    def test_url_is_none(self):
        node = TextNode("This is a text node", "bold")
        self.assertIsNone(node.url)

    def test_repr(self):
        node = TextNode("This is a text node", "bold", "https://localhost:8888")
        self.assertEqual(node.__repr__(), f"TextNode({node.text}, {node.text_type}, {node.url})")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node2.__repr__(), f"TextNode({node2.text}, {node2.text_type}, {node2.url})")


if __name__ == "__main__":
    unittest.main()