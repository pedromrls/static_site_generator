from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)


    def to_html(self):
        if not self.value:
            raise ValueError("All leaf nodes must have a value.")
        if not self.tag:
            return str(self.value)
        if not self.props:
            return f"<{self.tag}>{self.value}</{self.tag}>"
        props = " ".join(f'{k}="{v}"' for k,v in self.props.items())
        
        return f'<{self.tag} {props}>{self.value}</{self.tag}>'
    