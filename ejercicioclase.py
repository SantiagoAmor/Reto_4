# We start creating the class Point, which will heredar from the class Line,
# this class will have two attributes x and y, which will be the coordinates
# of the point.
class Point:
    #* Initializing the attributes x and y
    def __init__(self, x, y):
        self.x = x
        self.y = y
    #* Here we define a method to compute the distance between two points
    def compute_distance(self, other):
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5

# Now we create the class Line, which will have 
class Line:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.length = start.compute_distance(end)

class Figure:
    def __init__(self, vertices, edges, inner_angles):
        self.is_regular = True
        for i in range(1, len(edges)):
            if edges[i].length != edges[i-1].length:
                self.is_regular = False
                break
        self.vertices = vertices
        self.edges = edges
        self.inner_angles = inner_angles
        
    def compute_area(self):
        pass
    def compute_perimeter(self):
        pass
    def compute_inner_angles(self):
        pass



class Rectangle(Figure):
    def __init__(self, vertices, edges, inner_angles):
        super().__init__(vertices, edges, inner_angles)

    def compute_area(self):
        if len(self.vertices) == 4:
            length = self.edges[0].length
            width = self.edges[3].length
            return length * width
        return None
    def compute_perimeter(self):
        if len(self.vertices) == 4:
            return sum(edges.length for edges in self.edges)
        return None
    def compute_inner_angles(self):
        if len(self.vertices) == 4:
            return [90] * 4
    

class Square(Rectangle):
    def __init__(self, vertices, edges, inner_angles):
        super().__init__(vertices, edges, inner_angles)

class Triangle(Figure):
    def __init__(self, vertices, edges, inner_angles):
        super().__init__(vertices, edges, inner_angles)
    def compute_area(self):
        if len(self.vertices) == 3:
            a = self.edges[0].length
            b = self.edges[1].length
            c = self.edges[2].length
            s = (a + b + c) / 2
            return (s * (s - a) * (s - b) * (s - c)) ** 0.5
        return None
    def compute_perimeter(self):
        if len(self.vertices) == 3:
            return sum(edge.length for edge in self.edges)
        return None
    def compute_inner_angles(self):
        if len(self.vertices) == 3:
            if self.is_regular:
                return [60] * 3
            else:
                a = self.edges[0].length
                b = self.edges[1].length
                c = self.edges[2].length
                angle_A = (b**2 + c**2 - a**2) / (2 * b * c)
                angle_B = (a**2 + c**2 - b**2) / (2 * a * c)
                angle_C = (a**2 + b**2 - c**2) / (2 * a * b)
                return [angle_A, angle_B, angle_C]
                

class Isosceles(Triangle):
    def __init__(self, vertices, edges, inner_angles):
        super().__init__(vertices, edges, inner_angles)

class Equilateral(Triangle):
    def __init__(self, vertices, edges, inner_angles):
        super().__init__(vertices, edges, inner_angles)

class Scalene(Triangle):
    def __init__(self, vertices, edges, inner_angles):
        super().__init__(vertices, edges, inner_angles) 

class TriRectangle(Triangle):
    def __init__(self, vertices, edges, inner_angles):
        super().__init__(vertices, edges, inner_angles)


if __name__ == "__main__":
    # Example usage Rectangle
    p1 = Point(0, 0)
    p2 = Point(4, 0)
    p3 = Point(4, 3)
    p4 = Point(0, 3)

    edge1 = Line(p1, p2)
    edge2 = Line(p2, p3)
    edge3 = Line(p3, p4)
    edge4 = Line(p4, p1)

    rectangle = Rectangle([p1, p2, p3, p4], [edge1, edge2, edge3, edge4], [90, 90, 90, 90])
    
    print("Area of rectangle:", rectangle.compute_area())
    print("Perimeter of rectangle:", rectangle.compute_perimeter())
    print("Inner angles of rectangle:", rectangle.compute_inner_angles())
    print("Is rectangle regular?", rectangle.is_regular)
    
    # Example usage Triangle
    p5 = Point(0, 0)
    p6 = Point(1, 0)
    p7 = Point(0.5, (3**0.5)/2)

    edge5 = Line(p5, p6)
    edge6 = Line(p6, p7)
    edge7 = Line(p7, p5)

    triangle = Triangle([p5, p6, p7], [edge5, edge6, edge7], [])

    print("Area of triangle:", triangle.compute_area())
    print("Perimeter of triangle:", triangle.compute_perimeter())
    print("Inner angles of triangle:", triangle.compute_inner_angles())
    print("Is triangle regular?", triangle.is_regular)
