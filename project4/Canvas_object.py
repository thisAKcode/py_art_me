# C:\py_art_me\project4

class CanvasComponent:
    """
    create something on Canvas 
    """
    def __init__(self, name, sort_of, layer, metadata_1):
        self._name = name
        self.sort_of = sort_of
        self.layer = layer
        self.metadata_1 = metadata_1
    def action(self, arguments):
        # some method
        return f"{arguments} It creates {self._name} of type {self.sort_of} on {self.layer} layer of canvas. Here is additional info: {self.metadata_1}"
triangle = CanvasComponent('Triangle', 'default', 'Simple Shapes', 'May be imported from external library')

print(triangle.action("Initiated! "))