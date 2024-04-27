class HtmlNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.props = props
        self.children = children

    def __repr__(self) -> str:
        return f"HtmlNode({self.tag}, {self.value}, children: {self.children}, {self.props})"

    def to_html(self):
        raise NotImplementedError()
    
    def props_to_html(self):
        if not self.props or type(self.props) != dict:
            return ''
        htmlString = ''
        for prop in self.props:
            htmlString += f' {prop}="{self.props[prop]}"'
        return htmlString