from manim import *
class DefaultTemplate(Scene):
    def construct(self):

        circle = Circle().move_to(LEFT * 4)
        circle.set_fill(PINK, opacity=0.5)

        circleText = Text('See on ring', font_size=36).next_to(circle, DOWN)

        triangle = Triangle()
        triangle.set_fill(GREEN, opacity=0.5)

        triangleText = Text('See on kolmnurk', font_size=36).next_to(triangle, DOWN)

        square = Square().move_to(RIGHT * 4)
        square.set_fill(BLUE, opacity=0.5)

        squareText = Text('See on ruut', font_size=36).next_to(square, DOWN)
        
        objects = VGroup(circle, square, triangle)
        texts = VGroup(circleText, squareText, triangleText)
        
        self.play(Create(objects), Write(texts))

        self.wait(2)

        self.play(FadeOut(objects), FadeOut(texts))
