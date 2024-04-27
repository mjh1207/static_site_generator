from textnode import TextNode
from htmlnode import HtmlNode
from leafnode import LeafNode
from parentnode import ParentNode

def main():
    node = TextNode("This is a text node", "bold")
    print(node.__repr__())
    parent_node = ParentNode("div", [
        ParentNode("section", [LeafNode("p", "some paragraph")], {"width": "100%"}),
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
    ], {"class": "my_class"})

    print(parent_node.__repr__())

main()