# My exhibition 2021:

The artist that is oscillating around two styles: Karma Farmer and mr Censor Procfrastinator. Varied style mainly web published .jpeg things using advanced features. As a great artist he steel styles and methods from other artists.  

Artist competing with mr Censor Procfrastinator a person trying to make simple dummy patterns and abstractions. 


Feauters used by artist are:

1. Text Writer Layers of Text
2. Simple Shapes is the parts of the Layers of Outline.
3. Spray Gradient, the part of the Layers of Transparency is a fancy tool. This layer combines hardly with some other Layers kind of standalone.
4. Pattern Report, Layers of grids, splitting whole image into subimage. 

Colorit Rule, part of the Whole Image Guise matching colors of everything. 

Composition Layout part of the Whole Image structure.

# Section 1 

# Object Oriented Programming 

I create objects that interact with each other.
Object contain 1) attributes, 2) behaviour (method). 

Python Classes as blueprint:

```
class CanvasComponent:
    pass
```
Having blueprint you can create an actual object. 

`component = CanvasComponent()`
We add attributes first. Then we add a method:


```
class CanvasComponent:
    """
    create something on Canvas 
    """
    def __init__(self, name, layer, metadata_1):
        self._name = name
        self.sort_of = sort_of
        self.layer = layer
        self.metadata_1 = metadata_1
    def action(self, arguments):
        # some method
        return f"{arguments} It creates {self._name} of type {self.sort_of} on {self.layer} layer of canvas. Here is additional info: {self.metadata_1}"
triangle = CanvasComponent('Triangle', 'default', 'Simple Shapes', 'May be imported from external library')

print(triangle.action("Initiated! "))
```

# Section 2.
## Inheritance

CanvasComponent is not enough for make the exhibition 2021.Something that I am missing at this point is:
1. shapes 
2. text
3. Spray Gradient effect
4. pattern Report. 
5. layers
6. trancparency 
all those are instances of CanvasComponent
```
class Shape(CanvasComponent):
    """
    Create a Shape on CanvasComponent
    """
    
    def __init__(self, name, layer, metadata_1, vertices, edges, type, blob = None):
        pass 
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
        
triangle1 = Shape(name='Triangle1',
              layer=Simple Shapes,
              metadata_1='''trinagle https://en.wikipedia.org/wiki/Triangle''',
              vertices='give me array',
              edges = 'give me an array',
              type = 'Equilateral triangle'
              # Blob None
```
In Shape class we use the method super to call the init method of the parent class. Then, we add new attributes to the class. These attributes will be specific to object instances of the Shape class. A shape has more attributes than a simple CanvasComponent member. For example, a shape belongs to one of the CanvasComponent instance and she/he started school in a specific year. Also, a pupil might own a pet.

Notice _characteristic was added for attributes a shape might have: for example a shape instance can belong to one of the layers  (e.g. Simple Shapes) and has some more _characteristics. 


When creating a new, none of characteristic is specified yet. But this might change!


# Section 3.
## Instance and class attributes
A Python object have 2 types of attributes: 
a. instance attributes
b. Class attributes


all the attributes above are instance attributes that has following features:
    describe particular object instance,
    the content of an instance variable (e.g. the actual name of a CanvasComponent) are stored on the instance itself, not on the class. For example, the content of the name attribute of the instance triangle is <em>Triangle</em>. Other instances of the CanvasComponent class will have different name.
    
    
A <em>Class attribute</em> is created on definition of class before constructor. 
```class CanvasComponent:
    """
    Creates a component to put on Canvas
    """
    
    # class attribute
    canvas_type = 'cardboard' # color code #ad8762 
    canvas_texture = 'smooth' 
    canvas_scale = hard_coded # alternatively scalable
    
    def __init__(self, name, layer, metadata_1):
        pass
```
Class attribute exists without any particular instance of the class
All instances of the class share properties written as set of class variables.
change on class variable affect all the instances of the class 
```
triangle = CanvasComponent('Triangle', 'default', 'Simple Shapes', 'May be imported from external library')
print(triangle.canvas_type, triangle.canvas_texture, triangle.canvas_scale)
```


# Summary code

```
class CanvasComponent:
    """
    create something on Canvas 
    """
    def __init__(self, name, layer, metadata_1):
        self._name = name
        self.sort_of = sort_of
        self.layer = layer
        self.metadata_1 = metadata_1
    def action(self, arguments):
        # some method
        return f"{arguments} It creates {self._name} of type {self.sort_of} on {self.layer} layer of canvas. Here is additional info: {self.metadata_1}"
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

Class TextWriter():
    # Creates a canvas component writer
    def __init__(self, name, layer, metadata_1, x_start, y_start, size_pts, type, blob = None):
        super().__init__(name, layer, metadata_1)
        self.x_start = x_start
        self.y_start = y_start

if __name__ == "__main__":
    triangle = CanvasComponent('Triangle', 'default', 'Simple Shapes', 'May be imported from external library')
    print(triangle.action("Initiated! "))
    
    triangle1 = Shape(name='Triangle1',
              layer=Simple Shapes,
              metadata_1='''trinagle https://en.wikipedia.org/wiki/Triangle''',
              vertices='give me array',
              edges = 'give me an array',
              type = 'Equilateral triangle',
              # Blob None
    
```