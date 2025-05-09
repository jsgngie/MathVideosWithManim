from manim import *
import math

class CircleScene(Scene):
    def construct(self):
        wojak = ImageMobject("surprised.png")
        circle = Circle(radius=2, color=RED, z_index=-1, fill_color=RED, fill_opacity=0.5).move_to(UP * 0.5)
        self.add(wojak, circle)

class SquareScene(Scene):
    def construct(self):
        wojak = ImageMobject("surprised.png")
        square = Square(side_length=4, color=BLUE, z_index=-1, fill_color=BLUE, fill_opacity=0.5).move_to(UP * 0.5)
        self.add(wojak, square)

class RectangleScene(Scene):
    def construct(self):
        wojak = ImageMobject("surprised.png")
        rectangle = Rectangle(width=6, height=3, color=GREEN, z_index=-1, fill_color=GREEN, fill_opacity=0.5).move_to(UP * 0.5)
        self.add(wojak, rectangle)

class TriangleScene(Scene):
    def construct(self):
        wojak = ImageMobject("surprised.png")
        triangle = Triangle(color=YELLOW, z_index=-1, fill_color=YELLOW, fill_opacity=0.5).scale(2).move_to(UP * 0.5)
        self.add(wojak, triangle)