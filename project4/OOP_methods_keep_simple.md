```python
class Artpiece:
    def __init__( self, ingredients): 
        self.ingredients = ingredients 
    def __repr__( self):
        return f'Artpiece({ self.ingredients!r})'
Artpiece([' shapes', 'point'])
```

# Artpiece Factories (Hi, Andy!) With @classmethod
Artpiece([' trinagle', 'point']) 
Artpiece([' trinagle', 'point', 'point', 'point']) 
Artpiece([' point'] * 4)


# Different types of Artpiece can have some style: 
Pointilisme, Cubism, Low_poly, Lineart and so on 

Here I use class methods as factory functions for different styles of Artpieces.



