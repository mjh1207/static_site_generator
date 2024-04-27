from htmlnode import HtmlNode

class LeafNode(HtmlNode):
    def __init__(self, tag, value=None, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("All leaf nodes require a value.")
        if self.tag is None:
            return self.value
        else:
            return f'<{self.tag}{super().props_to_html()}>{self.value}</{self.tag}>'