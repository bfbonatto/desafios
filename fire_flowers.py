from sys import stdin
from math import sqrt

class Point:
	def __init__(self, x: float, y: float):
		self.x = x
		self.y = y

	def distance(self, other: "Point"):
		p = (self.x - other.x)**2
		q = (self.y - other.y)**2
		return sqrt(p+q)

	def __repr__(self):
		return f"(x= {self.x}, y= {self.y})"
	def __str__(self):
		return f"(x= {self.x}, y= {self.y})"

class Vector:
	def __init__(self, x: float, y: float):
		self.x = x
		self.y = y

	def __str__(self):
		return f"(x= {self.x}, y= {self.y})"
	def __repr__(self):
		return f"(x= {self.x}, y= {self.y})"

	@staticmethod
	def from_points(a: Point, b: Point) -> "Vector":
		return Vector(b.x - a.x, b.y - a.y)

	def add_point(self, p: Point) -> Point:
		return Point(p.x + self.x, p.y + self.y)

	@staticmethod
	def add_vectors(u: "Vector", v: "Vector") -> "Vector":
		return Vector(u.x + v.x, u.y + v.y)

	def scale(self, r: float) -> "Vector":
		return Vector(self.x * r, self.y * r)

	def norm(self) -> float:
		return sqrt(self.x**2 + self.y**2)

	def normalized(self) -> "Vector":
		return self.scale(1/self.norm())

class Circle:
	def __init__(self, c: Point, r: float):
		self.center = c
		self.r = r

	def is_inside(self, p: Point) -> bool:
		return self.center.distance(p) <= self.r

	def __str__(self):
		return f"(c= {self.center}, r= {self.r})"
	def __repr__(self):
		return f"(c= {self.center}, r= {self.r})"

def is_dead(hunter: Circle, flower: Circle) -> bool:
	v: Vector = Vector.from_points(hunter.center, flower.center)
	if v.norm() == 0:
		return hunter.r < flower.r
	v = v.normalized().scale(flower.r)
	most_distant: Point = v.add_point(flower.center)
	return not hunter.is_inside(most_distant)

def parse(line):
	case = line.replace("\n","").split()
	h_r, h_x, h_y, f_r, f_x, f_y = [float(p) for p in case]
	hunter = Circle(Point(h_x, h_y), h_r)
	flower = Circle(Point(f_x, f_y), f_r)
	return (hunter, flower)


for line in stdin.readlines():
	hunter, flower = parse(line)
	if is_dead(hunter, flower):
		print("MORTO")
	else:
		print("RICO")

