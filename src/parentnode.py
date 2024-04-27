from htmlnode import HtmlNode

class ParentNode(HtmlNode):
    def __init__(self, tag=None, children=None, props=None):
        super().__init__(tag, None, children, props)
        self.props = props
    
    def to_html(self,):
        if self.tag is None:
            raise ValueError("A tag is required for all parent elements")
        if self.children is None:
            raise ValueError("A parent element must have children elements")
        html_string = ""
        for child in self.children:
            html_string += child.to_html()
        return f"<{self.tag}{self.props_to_html()}>{html_string}</{self.tag}>"

    def __repr__(self) -> str:
        return f"ParentNode(Tag: {self.tag} Children: {self.children} Props: {self.props})"
