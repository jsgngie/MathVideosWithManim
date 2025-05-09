from manim import *

class DefaultTemplate(Scene):
    def construct(self):

        title = MathTex(r"\text{Ristkülik}", font_size=100)

        self.play(Write(title))

        self.wait(1)

        self.play(FadeOut(title))

        self.wait(1)

        # Create the rectangle

        rectangle = Rectangle(BLUE, width=4, height=2)
        
        self.play(Create(rectangle))

        # Create the side labels

        sideLabels = VGroup(
            MathTex(r"a").next_to(rectangle, UP),
            MathTex(r"b").next_to(rectangle, RIGHT),
            MathTex(r"a").next_to(rectangle, DOWN),
            MathTex(r"b").next_to(rectangle, LEFT),
        )

        sideLabels.save_state()

        rectangle.save_state()

        self.play(Write(sideLabels))

        self.wait(1)

        # Create the right angle representations

        rightAngleRepresentations = VGroup(
            VGroup(
                Arc(radius=0.6, start_angle=PI/2, angle=PI/2).move_to(rectangle.get_vertices()[3] + UP * 0.3 + LEFT * 0.3),
                Dot(point=rectangle.get_vertices()[3] + UP * 0.25 + LEFT * 0.25, radius=0.05),
            ),
            VGroup(
                Arc(radius=0.6, start_angle=0, angle=PI/2).move_to(rectangle.get_vertices()[2] + UP * 0.3 + RIGHT * 0.3),
                Dot(point=rectangle.get_vertices()[2] + UP * 0.25 + RIGHT * 0.25, radius=0.05),
            ),
            VGroup(
                Arc(radius=0.6, start_angle=-PI/2, angle=PI/2).move_to(rectangle.get_vertices()[1] + DOWN * 0.3 + RIGHT * 0.3),
                Dot(point=rectangle.get_vertices()[1] + DOWN * 0.25 + RIGHT * 0.25, radius=0.05),
            ),
            VGroup(
                Arc(radius=0.6, start_angle=PI, angle=PI/2).move_to(rectangle.get_vertices()[0] + DOWN * 0.3 + LEFT * 0.3),
                Dot(point=rectangle.get_vertices()[0] + DOWN * 0.25 + LEFT * 0.25, radius=0.05),
            ),
        )

        rightAngleRepresentations.save_state()

        self.play(Write(rightAngleRepresentations))

        self.wait(1)

        # Create the grabber to signify that the rectangle retains its shape when stretched

        grabber = ImageMobject("grabber.png").scale(0.15).move_to(rectangle.get_vertices()[0]).rotate(PI/1.5)
        grabber.save_state()

        self.play(FadeIn(grabber))

        self.wait(1)

        self.play(
            rectangle.animate.stretch(0.5, 0, about_edge=LEFT),
            sideLabels[0].animate.shift(LEFT),
            sideLabels[1].animate.shift(LEFT*2),
            sideLabels[2].animate.shift(LEFT),
            grabber.animate.shift(LEFT*2),
            rightAngleRepresentations[0].animate.shift(LEFT*2),
            rightAngleRepresentations[3].animate.shift(LEFT*2),
            )
        
        self.wait(1)

        self.play(
            rectangle.animate.scale(2),
            sideLabels[0].animate.shift(RIGHT * 0.25 + UP),
            sideLabels[1].animate.shift(RIGHT),
            sideLabels[2].animate.shift(RIGHT * 0.25 + DOWN),
            sideLabels[3].animate.shift(LEFT),
            grabber.animate.shift(RIGHT + UP),
            rightAngleRepresentations[0].animate.shift(RIGHT + DOWN),
            rightAngleRepresentations[1].animate.shift(LEFT + DOWN),
            rightAngleRepresentations[3].animate.shift(RIGHT + UP),
            rightAngleRepresentations[2].animate.shift(LEFT + UP),
        )

        self.wait(1)

        self.play(
            rectangle.animate.restore(),
            rightAngleRepresentations.animate.restore(),
            sideLabels.animate.restore(),
            grabber.animate.restore(),
        )

        self.wait(1)

        self.play(
            FadeOut(grabber, rightAngleRepresentations)
        )

        self.play(
            VGroup(
                rectangle,
                sideLabels
            ).animate.shift(LEFT * 3)
        )

        # Create the side length labels

        sideLengthLabels = MathTex(r"a = 4\ \text{cm},\ b = 2\ \text{cm}", font_size=64).move_to(UP + RIGHT*3.5)
            
        self.play(Write(sideLengthLabels))

        self.wait(1)

        sideLabelsCm = VGroup(
            MathTex(r"4\ \text{cm}").next_to(rectangle, UP),
            MathTex(r"2\ \text{cm}").next_to(rectangle, RIGHT),
            MathTex(r"4\ \text{cm}").next_to(rectangle, DOWN),
            MathTex(r"2\ \text{cm}").next_to(rectangle, LEFT),
        )

        self.play(Transform(sideLabels, sideLabelsCm))

        self.wait(1)

        originalSideLabels = VGroup(
            MathTex(r"a").next_to(rectangle, UP),
            MathTex(r"b").next_to(rectangle, RIGHT),
            MathTex(r"a").next_to(rectangle, DOWN),
            MathTex(r"b").next_to(rectangle, LEFT),
        )

        self.play(Transform(sideLabels, originalSideLabels))

        self.wait(1)

        # Create the diagonal line and label

        diagonalLine = Line(start=rectangle.get_vertices()[1], end=rectangle.get_vertices()[3], stroke_color=RED)
        diagonalLabel = MathTex(r"d").next_to(diagonalLine.get_center() + UP * 0.2)
        diagonalArrow = Arrow(start=diagonalLabel.get_center() + UP * 2 + RIGHT, end=diagonalLabel.get_center() + UP * 0.2, color=RED)
        diagonalText = MathTex(r"d^2 = a^2 + b^2", font_size=64).move_to(sideLengthLabels.get_center() + DOWN)
        diagonalArrowText = MathTex(r"\text{Diagonaal}").next_to(diagonalArrow.get_points()[0], UP)

        self.play(
            Create(VGroup(diagonalLine, diagonalArrow)),
            Write(VGroup(diagonalLabel, diagonalText, diagonalArrowText)))

        self.wait(1)

        # Show the diagonal calculation

        self.play(
            Transform(diagonalText, MathTex(r"d = \sqrt{a^2 + b^2}", font_size=64).move_to(diagonalText.get_center()))
        )

        self.wait(1)

        self.play(
            Transform(diagonalText, MathTex(r"d = \sqrt{4^2 + 2^2}", font_size=64).move_to(diagonalText.get_center()))
        )

        self.wait(1)

        self.play(
            Transform(diagonalText, MathTex(r"d = \sqrt{16 + 4}", font_size=64).move_to(diagonalText.get_center()))
        )

        self.wait(1)

        self.play(
            Transform(diagonalText, MathTex(r"d = \sqrt{20} \approx 4,47\ \text{cm}", font_size=64).move_to(diagonalText.get_center()))
        )
        
        self.wait(1)

        self.play(
            FadeOut(diagonalArrowText, diagonalArrow),
            diagonalLine.animate.set_stroke(color=BLUE)
        )

        self.wait(1)

        rectangleLineOne = Line(start=rectangle.get_vertices()[0], end=rectangle.get_vertices()[1], stroke_color=RED)
        rectangleLineTwo = Line(start=rectangle.get_vertices()[1], end=rectangle.get_vertices()[2], stroke_color=GREEN)
        rectangleLineThree = Line(start=rectangle.get_vertices()[2], end=rectangle.get_vertices()[3], stroke_color=YELLOW)
        rectangleLineFour = Line(start=rectangle.get_vertices()[3], end=rectangle.get_vertices()[0], stroke_color=PURPLE)

        perimeterPartOne = rectangleLineOne.copy()
        perimeterPartTwo = rectangleLineTwo.copy()
        perimeterPartThree = rectangleLineThree.copy()
        perimeterPartFour = rectangleLineFour.copy()

        # Perimeter

        perimeterLabel = MathTex(r"P = 2a + 2b").next_to(diagonalText, DOWN * 4)

        self.play(
            Write(perimeterLabel),
            Create(
                VGroup(
                    rectangleLineOne, 
                    rectangleLineTwo,
                    rectangleLineThree,
                    rectangleLineFour
                ),
            ),
            Create(
                VGroup(
                    perimeterPartOne,
                    perimeterPartTwo,
                    perimeterPartThree,
                    perimeterPartFour
                )
            )
        )
        self.wait(1)

        self.play(
            perimeterPartOne.animate.move_to(DOWN * 3 + LEFT * 4),
            perimeterPartTwo.animate.move_to(DOWN * 3 + LEFT).rotate(PI/2),
            perimeterPartThree.animate.move_to(DOWN * 3 + RIGHT * 2),
            perimeterPartFour.animate.move_to(DOWN * 3 + RIGHT * 5).rotate(PI/2)
        )

        labels = VGroup(
            MathTex(r"a").next_to(perimeterPartOne, UP),
            MathTex(r"b").next_to(perimeterPartTwo, UP),
            MathTex(r"a").next_to(perimeterPartThree, UP),
            MathTex(r"b").next_to(perimeterPartFour, UP)
        )

        self.play(Write(labels))

        self.wait(1)

        perimeterLabelCalcOne = MathTex(r"P = 2 \cdot 4 + 2 \cdot 2\ \text{cm}").move_to(perimeterLabel.get_center())

        self.play(
            Transform(perimeterLabel, perimeterLabelCalcOne)
        )

        self.wait(1)

        perimeterLabelCalcTwo = MathTex(r"P = 8 + 4\ \text{cm}").move_to(perimeterLabel.get_center())
        
        self.play(
            Transform(perimeterLabel, perimeterLabelCalcTwo)
        )

        self.wait(1)

        perimeterLabelCalcThree = MathTex(r"P = 12\ \text{cm}").move_to(perimeterLabel.get_center())

        self.play(
            Transform(perimeterLabel, perimeterLabelCalcThree)
        )

        self.wait(0.5)

        self.play(
            FadeOut(
                VGroup(
                    rectangleLineOne,
                    rectangleLineTwo,
                    rectangleLineThree,
                    rectangleLineFour,
                    perimeterPartOne,
                    perimeterPartTwo,
                    perimeterPartThree,
                    perimeterPartFour,
                    labels
                )
            )
        )

        # Area

        self.wait(0.5)

        areaHighlight = Rectangle(width=4, height=2, fill_color=RED, fill_opacity=0.8).move_to(rectangle)

        areaLabel = MathTex(r"S = a \cdot b").next_to(perimeterLabel, DOWN * 1.5)

        self.play(
            Write(areaLabel),
            FadeIn(areaHighlight)
        )

        self.wait(1)

        areaLabelCalcOne = MathTex(r"S = 4 \cdot 2\ \text{cm}^2").move_to(areaLabel.get_center())

        self.play(
            Transform(areaLabel, areaLabelCalcOne)
        )

        self.wait(1)

        areaLabelCalcTwo = MathTex(r"S = 8\ \text{cm}^2").move_to(areaLabel.get_center())

        self.play(
            Transform(areaLabel, areaLabelCalcTwo)
        )

        self.wait(1)

        oldLabels = VGroup(
            sideLengthLabels,
            perimeterLabel,
            areaLabel,
            diagonalText
        )

        self.play(
            oldLabels.animate.move_to(oldLabels.get_center() + UP * 1.7),
            FadeOut(areaHighlight)
        )

        self.wait(1)

        perimeterFormula = MathTex(r"P = 2a + 2b").next_to(oldLabels, DOWN * 4)
        areaFormula = MathTex(r"S = a \cdot b").next_to(perimeterFormula, DOWN * 1.5)
        diagonalFormula = MathTex(r"d = \sqrt{a^2 + b^2}", font_size=64).next_to(rectangle.get_center(), DOWN * 10)

        self.play(
            Write(VGroup(perimeterFormula, areaFormula, diagonalFormula))
        )

        self.wait(2)

        self.play(
            *[FadeOut(mobject) for mobject in self.mobjects]
        )