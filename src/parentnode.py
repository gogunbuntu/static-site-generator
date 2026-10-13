from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("Parent node must have tag.")
        if self.children is None:
            raise ValueError("Parent node must have at least one child node.")
        return f"<{self.tag}{self.props}>{"".join([x.to_html() for x in self.children])}</{self.tag}>"

