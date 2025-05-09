from manim import *

class DefaultTemplate(Scene):
    def construct(self):

        title = MathTex(r"\text{Ruut}", font_size=100)
        self.play(Write(title))

        self.wait(1)

        self.play(Uncreate(title))

        #Create the square

        sideLength = 2
        squareOne = Square(sideLength)
        squareOne.flip(RIGHT)

        self.play(Create(squareOne))

        self.play(squareOne.animate.shift(LEFT * 2))

        grabber = ImageMobject("grabber.png").scale(0.15).move_to(squareOne.get_vertices()[3]).rotate(PI/1.5)

        topLabel = MathTex(r"a").next_to(squareOne.get_top(), UP)
        bottomLabel = MathTex(r"a").next_to(squareOne.get_bottom(), DOWN)
        leftLabel = MathTex(r"a").next_to(squareOne.get_left(), LEFT)
        rightLabel = MathTex(r"a").next_to(squareOne.get_right(), RIGHT)

        labels = VGroup(topLabel, bottomLabel, leftLabel, rightLabel)
        self.play(Create(labels))

        # Create right angle representations at each corner
        rightAngleRepresentations = VGroup(
            VGroup(
                Arc(radius=0.6, start_angle=PI/2, angle=PI/2).move_to(squareOne.get_vertices()[0] + UP * 0.3 + LEFT * 0.3),
                Dot(point=squareOne.get_vertices()[0] + UP * 0.25 + LEFT * 0.25, radius=0.05),
            ),
            VGroup(
                Arc(radius=0.6, start_angle=0, angle=PI/2).move_to(squareOne.get_vertices()[1] + UP * 0.3 + RIGHT * 0.3),
                Dot(point=squareOne.get_vertices()[1] + UP * 0.25 + RIGHT * 0.25, radius=0.05),
            ),
            VGroup(
                Arc(radius=0.6, start_angle=-PI/2, angle=PI/2).move_to(squareOne.get_vertices()[2] + DOWN * 0.3 + RIGHT * 0.3),
                Dot(point=squareOne.get_vertices()[2] + DOWN * 0.25 + RIGHT * 0.25, radius=0.05),
            ),
            VGroup(
                Arc(radius=0.6, start_angle=PI, angle=PI/2).move_to(squareOne.get_vertices()[3] + DOWN * 0.3 + LEFT * 0.3),
                Dot(point=squareOne.get_vertices()[3] + DOWN * 0.25 + LEFT * 0.25, radius=0.05),
            ),
        )

        self.play(Create(rightAngleRepresentations))
        
        self.wait(1)

        # Create the side label

        sideLabel = MathTex(r"a = 3\,\text{ cm}").move_to(RIGHT * 4)
        self.play(
            Create(sideLabel),
            FadeIn(grabber)
            )

        self.wait(1)

        scaleFactor = 1.5

        sideLabel.save_state()

        squareGroup = VGroup(squareOne, rightAngleRepresentations)

        # Apply transformations
        self.play(
            squareGroup.animate.scale(scaleFactor),
            Transform(sideLabel, MathTex(r"a = 4\,\text{ cm}").move_to(sideLabel.get_center())),
            grabber.animate.shift(UP * 0.5 + RIGHT * 0.5),
            Transform(topLabel, MathTex(r"a").next_to(squareOne.get_top() + UP * 0.5, UP)),
            Transform(bottomLabel, MathTex(r"a").next_to(squareOne.get_bottom() + DOWN * 0.5, DOWN)),
            Transform(leftLabel, MathTex(r"a").next_to(squareOne.get_left() + LEFT * 0.5, LEFT)),
            Transform(rightLabel, MathTex(r"a").next_to(squareOne.get_right() + RIGHT * 0.5, RIGHT)),
        )

        self.wait(1)

        self.play(
            squareGroup.animate.scale(2/3),
            sideLabel.animate.restore(),
            grabber.animate.shift(DOWN * 0.5 + LEFT * 0.5),
            Transform(topLabel, MathTex(r"a").next_to(squareOne.get_top() + DOWN * 0.5, UP)),
            Transform(bottomLabel, MathTex(r"a").next_to(squareOne.get_bottom() + UP * 0.5, DOWN)),
            Transform(leftLabel, MathTex(r"a").next_to(squareOne.get_left() + RIGHT * 0.5, LEFT)),
            Transform(rightLabel, MathTex(r"a").next_to(squareOne.get_right() + LEFT * 0.5, RIGHT)),
        )

        self.wait(1)

        # Perimeter

        perimeterLabel = MathTex(r"P = 4a\,\text{ cm}").next_to(sideLabel, DOWN, buff=0.2)
        self.play(Create(perimeterLabel), FadeOut(grabber))

        self.wait(1)

        self.play(FadeOut(rightAngleRepresentations))

        squareLineOne = Line(start=squareOne.get_vertices()[0], end=squareOne.get_vertices()[1], stroke_color=RED)
        squareLineTwo = Line(start=squareOne.get_vertices()[1], end=squareOne.get_vertices()[2], stroke_color=GREEN)
        squareLineThree = Line(start=squareOne.get_vertices()[2], end=squareOne.get_vertices()[3], stroke_color=YELLOW)
        squareLineFour = Line(start=squareOne.get_vertices()[3], end=squareOne.get_vertices()[0], stroke_color=PURPLE)

        perimeterPartOne = squareLineOne.copy()
        perimeterPartTwo = squareLineTwo.copy()
        perimeterPartThree = squareLineThree.copy()
        perimeterPartFour = squareLineFour.copy()
        
        self.play(
            Create(
                VGroup(
                    squareLineOne, 
                    squareLineTwo, 
                    squareLineThree, 
                    squareLineFour, 
                    perimeterPartOne, 
                    perimeterPartTwo, 
                    perimeterPartThree,
                    perimeterPartFour)
            ),
        )

        self.wait(1)

        self.play(
            perimeterPartOne.animate.move_to(DOWN * 3 + LEFT * 3),
            perimeterPartTwo.animate.move_to(DOWN * 3 + LEFT).rotate(PI/2),
            perimeterPartThree.animate.move_to(DOWN * 3 + RIGHT),
            perimeterPartFour.animate.move_to(DOWN * 3 + RIGHT * 3).rotate(PI/2)
        )

        perimeterLabels = VGroup(
            MathTex(r"a").next_to(perimeterPartOne.get_center(), UP),
            MathTex(r"a").next_to(perimeterPartTwo.get_center(), UP),
            MathTex(r"a").next_to(perimeterPartThree.get_center(), UP),
            MathTex(r"a").next_to(perimeterPartFour.get_center(), UP)
        )

        self.play(Create(perimeterLabels))

        self.play(Transform(perimeterLabel, MathTex(r"P = a + a + a + a\,\text{ cm}").next_to(sideLabel, DOWN, buff=0.2)))
        
        self.wait(1)

        self.play(Transform(perimeterLabel, MathTex(r"P = 4 \cdot 3\,\text{ cm}").next_to(sideLabel, DOWN, buff=0.2)))

        self.wait(1)

        self.play(Transform(perimeterLabel, MathTex(r"P = 12\,\text{ cm}").next_to(sideLabel, DOWN, buff=0.2)))

        self.wait(1)

        # Area

        areaHighlight = Square(sideLength, fill_color=RED, fill_opacity=0.8).move_to(squareOne)
        areaLabel = MathTex(r"S = a \cdot a\,\text{ cm}^2").next_to(sideLabel, UP, buff=0.2)
        self.play(
            FadeOut(
                perimeterLabels,
                VGroup(
                    perimeterPartOne,
                    perimeterPartTwo,
                    perimeterPartThree,
                    perimeterPartFour
                ),
                VGroup(
                    squareLineOne,
                    squareLineTwo,
                    squareLineThree,
                    squareLineFour
                )
            ),
            Create(areaLabel),
            FadeIn(areaHighlight)
        )

        self.wait(1)

        self.play(Transform(areaLabel, MathTex(r"S = a^2 \text{ cm}^2").next_to(sideLabel, UP, buff=0.2)))

        self.wait(1)

        self.play(FadeOut(areaHighlight))

        self.wait(1)

        self.play(
            squareOne.animate.scale(3),
            topLabel.animate.shift(UP * 2),
            bottomLabel.animate.shift(DOWN * 2),
            leftLabel.animate.shift(LEFT * 2),
            rightLabel.animate.shift(RIGHT * 2)
        )

        self.wait(1)

        # Rubics cube area calculation
        squareCenter = squareOne.get_center()

        squareOne1 = Square(side_length=2, fill_color=YELLOW, fill_opacity=1).move_to(squareCenter + UP * 2)
        squareTwo = Square(side_length=2, fill_color=GREEN, fill_opacity=1).move_to(squareCenter + UP * 2 + LEFT * 2)
        squareThree = Square(side_length=2, fill_color=RED, fill_opacity=1).move_to(squareCenter + UP * 2 + RIGHT * 2)
        squareFour = Square(side_length=2, fill_color=PURPLE, fill_opacity=1).move_to(squareCenter + DOWN * 2)
        squareFive = Square(side_length=2, fill_color=ORANGE, fill_opacity=1).move_to(squareCenter + DOWN * 2 + LEFT * 2)
        squareSix = Square(side_length=2, fill_color=PINK, fill_opacity=1).move_to(squareCenter + DOWN * 2 + RIGHT * 2)
        squareSeven = Square(side_length=2, fill_color=BLUE_E, fill_opacity=1).move_to(squareCenter + LEFT * 2)
        squareEight = Square(side_length=2, fill_color=RED_A, fill_opacity=1).move_to(squareCenter)
        squareNine = Square(side_length=2, fill_color=TEAL, fill_opacity=1).move_to(squareCenter + RIGHT * 2)
        
        rubicsSquare = VGroup(
                    squareOne1,
                    squareTwo,
                    squareThree,
                    squareFour,
                    squareFive,
                    squareSix,
                    squareSeven,
                    squareEight,
                    squareNine
        )

        self.play(
            FadeIn(rubicsSquare)
        )

        self.wait(1)

        self.play(
            VGroup(
                squareFour,
                squareFive,
                squareSix
            ).animate.set_stroke(color=PURE_GREEN, width=10)
        )

        self.wait(1)

        self.play(
            VGroup(
                squareThree,
                squareNine
            ).animate.set_stroke(color=PURE_GREEN, width=10)
        )

        self.wait(1)
        
        # Update area label to reflect the actual area
        self.play(Transform(areaLabel, MathTex(r"S = 3 \cdot 3\,\text{ cm}^2").next_to(sideLabel, UP, buff=0.2)))

        self.wait(1)

        self.play(Transform(areaLabel, MathTex(r"S = 9\,\text{ cm}^2").next_to(sideLabel, UP, buff=0.2)))

        self.play(FadeOut(rubicsSquare))

        self.play(
                squareOne.animate.scale(1/3),
                topLabel.animate.shift(DOWN * 2),
                bottomLabel.animate.shift(UP * 2),
                leftLabel.animate.shift(RIGHT * 2),
                rightLabel.animate.shift(LEFT * 2)
            )

        self.wait(1)

        # Diagonal

        diagonalLine = Line(start=squareOne.get_vertices()[0], end=squareOne.get_vertices()[2], stroke_color=RED)
        diagonalLabel = MathTex(r"d", color=RED).next_to(diagonalLine.get_center(), UP * 0.5 + RIGHT * 0.5)
        diagonalArrow = Arrow(start=diagonalLabel.get_center() + UP * 2 + RIGHT, end=diagonalLabel.get_center() + UP * 0.2, color=RED)
        diagonalArrowText = MathTex(r"\text{diagonaal}").next_to(diagonalArrow.get_points()[0], UP * 0.5)
        diagonalFormula = MathTex(r"d = a\cdot  \sqrt{2}").next_to(perimeterLabel, DOWN)

        self.play(Create(diagonalLine), Create(diagonalLabel), Create(diagonalArrow), Create(diagonalArrowText))

        self.wait(1)

        self.play(Write(diagonalFormula))

        self.wait(1)

        diagonalFormulaFromPythagoras = MathTex(r"d = \sqrt{a^2 + a^2} = \sqrt{2a^2} = \sqrt{2 \cdot a^2} = \sqrt{2} \cdot \sqrt{a^2} = a \cdot \sqrt{2}", color=BLUE).move_to(DOWN * 3)

        self.play(Write(diagonalFormulaFromPythagoras))

        self.wait(1)

        self.play(Transform(diagonalFormula, MathTex(r"d = 3\cdot  \sqrt{2}").next_to(perimeterLabel, DOWN)))

        self.wait(1)
        
        self.play(Transform(diagonalFormula, MathTex(r"d = 3\cdot  \sqrt{2}").next_to(perimeterLabel, DOWN)))

        self.wait(1)

        self.play(Transform(diagonalFormula, MathTex(r"d \approx 4{,}24\,\text{ cm}").next_to(perimeterLabel, DOWN)))

        self.wait(1)

        self.play(
            diagonalLine.animate.set_stroke(color=WHITE),
            diagonalLabel.animate.set_fill(color=WHITE),
            FadeOut(
                VGroup(diagonalArrow, diagonalArrowText, diagonalFormulaFromPythagoras)
                )
            )
        
        # Final formula screen
    
        perimeterFormula = MathTex(r"P = 4a").next_to(perimeterLabel, DOWN * 0.7, buff=0.2)
        areaFormula = MathTex(r"S = a \cdot a = a^2").next_to(perimeterFormula, DOWN, buff=0.2)
        diagonalFormulaFinal = MathTex(r"d = a\cdot  \sqrt{2}").next_to(areaFormula, DOWN, buff=0.2)

        formulas = VGroup(
            areaFormula,
            perimeterFormula,
            diagonalFormulaFinal
        )

        self.play(areaLabel.animate.shift(UP * 2),
                  perimeterLabel.animate.shift(UP * 2),
                  sideLabel.animate.shift(UP * 2),
                  diagonalFormula.animate.shift(UP * 2)
        )

        self.play(Create(formulas))

        self.wait(2)

        self.play(
            *[FadeOut(mobject) for mobject in self.mobjects]
        )