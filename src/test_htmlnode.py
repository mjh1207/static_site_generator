import unittest

from htmlnode import HtmlNode

class TestHtmlNode(unittest.TestCase):
    def test_repr(self):
        node1 = HtmlNode("h1", "My heading", None, {"href": "https://www.google.com", "target": "_blank"})
        node2 = HtmlNode(tag="p")
        node3 = HtmlNode(tag="div", props={"class": "wrapper-div"}, children=[node1, node2])
        self.assertEqual(node1.__repr__(), "HtmlNode(h1, My heading, children: None, {'href': 'https://www.google.com', 'target': '_blank'})")
        self.assertEqual(node2.__repr__(), "HtmlNode(p, None, children: None, None)")
        self.assertEqual(node3.__repr__(), "HtmlNode(div, None, children: [HtmlNode(h1, My heading, children: None, {'href': 'https://www.google.com', 'target': '_blank'}), HtmlNode(p, None, children: None, None)], {'class': 'wrapper-div'})")

    def test_props_to_html(self):
        node1 = HtmlNode(props={"class": "my_class"})
        self.assertEqual(node1.props_to_html(), ' class="my_class"')
        node2 = HtmlNode("h2")
        self.assertEqual(node2.props_to_html(), '')

if __name__ == "__main__":
    unittest.main()
