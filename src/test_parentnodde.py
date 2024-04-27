import unittest

from parentnode import ParentNode
from htmlnode import HtmlNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    def test_to_html(self):
        node1 = LeafNode("a", "Link to google", {"href": "https://www.google.com", "target": "_blank"})
        node3 = ParentNode(tag="div", props={"class": "wrapper-div"}, children=[node1])
        parent_node = ParentNode(
            "div",
            [
                node3,
                LeafNode("b", "Bold text", {"class": "bold_class"}),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(parent_node.to_html(), '<div><div class="wrapper-div"><a href="https://www.google.com" target="_blank">Link to google</a></div><b class="bold_class">Bold text</b>Normal text</div>')

    def test_repr(self):
        parent_node = ParentNode(
            "div",
            [
                LeafNode("p", "paragraph")
            ],
            {"class": "my_class"}
        )
        self.assertEqual(parent_node.__repr__(), "ParentNode(Tag: div Children: [HtmlNode(p, paragraph, children: None, None)] Props: {'class': 'my_class'})")