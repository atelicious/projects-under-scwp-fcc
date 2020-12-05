#This is my solution to the Polygon Area Calculator Problem in FCC's Scientific Computing with Python.
#You can view the original question and my repl solution @ https://repl.it/@atelicious/FCC-polygon-area-calculator


class Rectangle:
  # Initilizes the rectangle class with that accepts width and height as arguments
  def __init__(self, width, height):
      self.width = width
      self.height = height

  def set_width(self, set_width):
      # Sets the width of the rectangle
      self.width = set_width

  def set_height(self, set_height):
        # Sets the height of the rectangle
      self.height = set_height

  def get_area(self):
      # Returns the area of the rectangle
      area = self.width * self.height
      return area
    
  def get_perimeter(self):
      # Returns the perimeter of the rectangle
      perimeter = (2 * self.width) + (2 * self.height)
      return perimeter

  def get_diagonal(self):
        # Returns the diagonal of the rectangle
      diagonal = ((self.width ** 2 + self.height ** 2) ** .5)
      return diagonal

  def get_picture(self):
        # Creates a picture of the rectangle using "*" 
      picture_width = ''
      picture = ''
      if self.width > 50 or self.height > 50:
          return 'Too big for picture.'
      else:
          for i in range(0, self.width):
              picture_width += '*'

          for i in range(0, self.height):
              picture += picture_width
              picture += '\n'
          return picture
    
  def get_amount_inside(self, other_shape):
      # Returns the amount of other shape that can fit into the parent shape
      num_of_times = self.get_area() // other_shape.get_area()
      return num_of_times

  def __repr__(self):
  # Representative text when the object using the class is printed
      return (f'Rectangle(width={self.width}, height={self.height})')



class Square(Rectangle):
  def __init__(self, width, height=None):
  # Initilizes the rectangle class with that accepts width and height as arguments
      super().__init__(width, height)
  # Inherits width and height of rectangle class
      self.width = width
      self.height = width
    
  def set_side(self, set_side):
      self.width = set_side
      self.height = set_side
    
  def __repr__(self):
  # Representative text when the object using the class is printed
      return (f'Square(side={self.width})')