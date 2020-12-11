# Types of methods

There are instance methods, class methods and static methods.

**Instance methods** are commonly used. They take at least the parameter *self* as an input.
This parameter points towards an instance of the class when the method is called. An instance method can modify both *object state* and *class state* (the latter can be modified through ```self.__class__```).

in my base class CanvasComponent there is an **instance method**:

```python 
def action(self, arguments):
        return f"{arguments} It creates {self._name} of type {self.sort_of} on {self.layer} layer of canvas. Here is additional info: {self.metadata_1}"
```

# Static method

Static methods take neither a self nor cls parameter as an input. Therefore, they cannot modify neither object state nor class state. 
Although they are related to the class, they are independent of the other class or instance methods and can only access the data they are provided with.

Let's add a static method to our class.


```python

class CanvasComponent:
    def __init__(vertices):
        pass
    def area(self):
        return self.component_area(self.vertices)

@staticmethod 
def extraordinary_thing(r): 
    return CanvasComponent('Spontan line', x1,y1,x2,y2)

```
We added an area() instance method that calculates and returns the components area.


We can also add a static method to our Shape class. It will tell us whether a shape is a subject for computation of area.

```
class Shape(CanvasComponent):
    """
    Given a shape, determine if it is appropriate to compute area.
    """
    shapes = {
            'Polygon': True,
            'Polyline': False,
            'Point': False,
            'Pointcloud': False,
            'Text': False,
            'Pixel': False
            'Pixel': False
            }

    return shape.get(shape, False)

```
# Class methods


Class methods take at least the parameter cls as an input. cls points towards the class - not a particular object instance - when the method is called. Therefore, a class method can only modify class state but not object state. Still, changing the class state will still affect all instances of the class.

@classmethod decorator to flag it as a class method.

Use of all of method described here make it possible to "write object-oriented Python that communicates its intent more clearly". <Bader, Dan. Python Tricks: A Buffet of Awesome Python Features (p. 145). Dan Bader (dbader.org). Kindle Edition.>

In Python a class can only have one constructor (the self.__init__() method)
@classmethod is a caveat to create factory functions. - allow us to create class objects that are configured exactly the way we want them: like additional constructors


For example, we probably want to create the main characters of our Canvas Components. Typing all the names and other attributes is time comsuming: a few class methods speed up the process. 
We can create a Polygon constructor as follows:

```
@classmethod
def polygon(cls):
    return cls('Triangle2', 'Simple Shapes', '''trinagle https://en.wikipedia.org/wiki/Triangle''', 'give me an array','give me an array', 'not Equilateral triangle')

@classmethod
def point(cls):
    return cls('PointXY', 'Simple Shapes', '''https://en.wikipedia.org/wiki/Point_(geometry)''', 'give me an array', 'give me an array', 'A unique location in space')
```

# Summary code

```
class CanvasComponent:
    """
    create Canvas component 
    """
    def __init__(self, name, layer, metadata_1):
        self._name = name
        self.sort_of = sort_of
        self.layer = layer
        self.metadata_1 = metadata_1
        
    def action(self, arguments):
        # some method
        return f"{arguments} It creates {self._name} of type {self.sort_of} on {self.layer} layer of canvas. Here is additional info: {self.metadata_1}"
    
    @staticmethod 
    def extraordinary_thing(): 
        return CanvasComponent('Spontan line', x1,y1,x2,y2)
    
triangle = CanvasComponent('Triangle', 'default', 'Simple Shapes', 'May be imported from external library')

print(triangle.action("Initiated! "))




class Shape(CanvasComponent):
    """
    Create a Shape on CanvasComponent
    """
    
    def __init__(self, name, layer, metadata_1, vertices, edges, type, blob = None):
        super().__init__(name, layer, metadata_1):
        self.vertices = vertices
        self.edges = edges
        self.type = type
        if blob:
            self.blob = blob
        
        self._characteristics = {
        'symmetric': False,
        'vertex_count': False,
        'circularity': False
        }
        
        
    @classmethod
    def polygon(cls):
        return cls('Triangle2', 'Simple Shapes', '''trinagle https://en.wikipedia.org/wiki/Triangle''', 'give me an array','give me an array', 'not Equilateral triangle')

    @classmethod
    def point(cls):
        return cls('PointXY', 'Simple Shapes', '''https://en.wikipedia.org/wiki/Point_(geometry)''', 'give me an array', 'give me an array', 'A unique location in space')



triangle1 = Shape(name='Triangle1',
              layer=Simple Shapes,
              metadata_1='''trinagle https://en.wikipedia.org/wiki/Triangle''',
              vertices='give me array',
              edges = 'give me an array',
              type = 'Equilateral triangle'
              # Blob None

Class PatternRaport(CanvasComponent):
    """
    Creates a canvas component pattern
    """
    def __init__(self, name, layer, metadata_1, x_start, y_start, x_step, y_step, type, blob = None):
        super().__init__(name, layer, metadata_1)
        self.x_start = x_start
        self.y_start = y_start
        self.x_step = x_step
        self.y_step = y_step
        self.type = type
        
        if blob is not None:
            self.blob = blob
    
    @classmethod
    def pattern1(cls):
        return cls('Pattern1', 'Simple Pattern', '''https://en.wikipedia.org/wiki/Pattern''', 0, 0, 2, 2, 'Predictable repetition of elements type1')
    
    @classmethod
    def pattern1(cls):
        return cls('Pattern2', 'Simple Pattern', '''https://en.wikipedia.org/wiki/Pattern''', 0, 0, 50, 50, 'Predictable repetition of elements type2')
        
Class TextWriter():
    # Creates a canvas component writer
    def __init__(self, name, layer, metadata_1, x_start, y_start, size_pts, type, blob = None):
        super().__init__(name, layer, metadata_1)
        self.x_start = x_start
        self.y_start = y_start

if __name__ == "__main__":

    triangle = CanvasComponent('Triangle', 'default', 'Simple Shapes', 'May be imported from external library')
    Triangle2 = Shape('Triangle1', 'Simple Shapes', '''trinagle https://en.wikipedia.org/wiki/Triangle''', 'give me an array','give me an array', 'Equilateral triangle')
    
    triangle1 = Shape(name='Triangle1',
              layer=Simple Shapes,
              metadata_1='''trinagle https://en.wikipedia.org/wiki/Triangle''',
              vertices='give me array',
              edges = 'give me an array',
              type = 'Equilateral triangle',
              # Blob None
    
```