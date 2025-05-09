from manim import *
class DefaultTemplate(Scene):
    def construct(self):
        title = MathTex(r"\text{Kolmnurk}")

        self.play(Write(title))

        self.wait(1)

        self.play(FadeOut(title))

        self.wait(1)

        # Create initial triangle with side labels
        triangle = Polygon(
            [-2, -1, 0],   # Point A (left)
            [3, -1, 0],    # Point C (right)
            [-1, 1.5, 0],   # Point B (top)
            color=BLUE
        )

        # Calculate midpoints of sides
        midpointC = (triangle.get_vertices()[0] + triangle.get_vertices()[1]) / 2  # bottom side
        midpointA = (triangle.get_vertices()[1] + triangle.get_vertices()[2]) / 2  # right side
        midpointB = (triangle.get_vertices()[0] + triangle.get_vertices()[2]) / 2  # left side

        triangleSideLabels = VGroup(
            MathTex(r"b ", font_size=36).move_to(midpointC + DOWN * 0.5),
            MathTex(r"a", font_size=36).move_to(midpointA + UP * 0.5),
            MathTex(r"c", font_size=36).move_to(midpointB + LEFT * 0.4 + UP * 0.2)
        )

        trianglePointLabels = VGroup(
            MathTex(r"A", font_size=36).move_to(triangle.get_vertices()[0] + LEFT * 0.5),
            MathTex(r"C", font_size=36).move_to(triangle.get_vertices()[1] + RIGHT * 0.5),
            MathTex(r"B", font_size=36).move_to(triangle.get_vertices()[2] + UP * 0.5)
        )
        
        self.play(
            Create(triangle), 
            Write(VGroup(triangleSideLabels, trianglePointLabels)))

        self.wait(1)

        # Create triangle height
        heightLine = Line(start=triangle.get_vertices()[2], end=[triangle.get_vertices()[2][0], triangle.get_vertices()[0][1], 0], color=RED)
        heightLabel = MathTex(r"h", font_size=36, color=RED).move_to(heightLine.get_center() + RIGHT * 0.4)
        heightArrow = Arrow(end=heightLabel.get_center(), start=heightLabel.get_center() + RIGHT + UP * 2, color=RED)
        heightText = MathTex(r"\text{kõrgus}", font_size=36, color=RED).move_to(heightArrow.get_start() + UP * 0.5)
        baseLine = Line(start=triangle.get_vertices()[0], end=triangle.get_vertices()[1], color=RED)
        heightAngle = Angle(baseLine, heightLine, radius = 0.6, dot=True, quadrant=(1, -1), color=RED)

        triangleWithLabels = VGroup(triangle, triangleSideLabels, trianglePointLabels, heightLine, heightLabel, heightAngle)

        self.play(
            Create(VGroup(heightLine, heightArrow, baseLine, heightAngle)),
            Write(VGroup(heightLabel, heightText)),
            Transform(triangleSideLabels[0], MathTex(r"\text{alus}", font_size=36, color=RED).move_to(midpointC + DOWN * 0.5))
        )


        # Create an obtuse triangle to highlight that height can be drawn outside of the triangle
        obtuseTriangle = Polygon(
            [-2, -1, 0],   # Point A (left)
            [2, -1, 0],    # Point B (right)
            [3.5, 1, 0],     # Point C (top, obtuse angle)
            color=BLUE
        ).move_to(LEFT * 3.5)

        bottomLineExtension = DashedLine(start=obtuseTriangle.get_vertices()[1], end=obtuseTriangle.get_vertices()[1] + RIGHT * 1.5, color=RED)
        obtuseTriangleHeightLine = Line(start=obtuseTriangle.get_vertices()[2], end=bottomLineExtension.get_end(), color=RED)
        obtuseTriangleHeightLabel = MathTex(r"h", font_size=36, color=RED).move_to(obtuseTriangleHeightLine.get_center() + RIGHT * 0.4)
        obtuseTriangleHeightAngle = Angle(obtuseTriangleHeightLine, bottomLineExtension, radius = 0.6, dot=True, quadrant=(-1, -1), color=RED)
        secondHeightArrow = Arrow(end=obtuseTriangleHeightLabel.get_center(), start=heightArrow.get_start() + RIGHT * 3.1, color=RED)
        newHeightText = MathTex(r"\text{kõrgused}", font_size=36, color=RED).move_to(heightText.get_center() + RIGHT * 3.1)

        obtusePointLabels = VGroup(
            MathTex(r"A", font_size=36).next_to(obtuseTriangle.get_points()[0], LEFT * 0.75),
            MathTex(r"C", font_size=36).move_to(obtuseTriangle.get_points()[1] + DOWN * 0.5 + RIGHT * 2.6),
            MathTex(r"B", font_size=36).move_to(obtuseTriangle.get_points()[2] + UP * 2.5 + RIGHT * 2.8)
        )

        obtuseMidpoints = [
            [(obtuseTriangle.get_vertices()[0][0] + obtuseTriangle.get_vertices()[1][0]) / 2, obtuseTriangle.get_vertices()[0][1], 0],
            [(obtuseTriangle.get_vertices()[1][0] + obtuseTriangle.get_vertices()[2][0]) / 2, obtuseTriangle.get_vertices()[1][1], 0],
            [(obtuseTriangle.get_vertices()[2][0] + obtuseTriangle.get_vertices()[0][0]) / 2, obtuseTriangle.get_vertices()[2][1], 0]
        ]

        obtuseSideLabels = VGroup(
            MathTex(r"b", font_size=36).move_to(obtuseMidpoints[0] + DOWN * 0.5),
            MathTex(r"a", font_size=36).move_to(obtuseMidpoints[1] + UP * 0.75 + LEFT * 0.75),
            MathTex(r"c", font_size=36).move_to(obtuseMidpoints[2] + DOWN * 0.5)
        )

        self.play(
            triangleWithLabels.animate.shift(RIGHT * 3.1),
            VGroup(
                baseLine,
                heightArrow,
                heightText,
            ).animate.shift(RIGHT * 3.1),
        )

        heightText.save_state()

        self.play(
            Create(
                VGroup(
                    obtuseTriangle,
                    bottomLineExtension,
                    obtuseTriangleHeightLine,
                    obtuseTriangleHeightAngle,
                    secondHeightArrow
                )
            ),
            Transform(heightText, newHeightText),
            Write(
                VGroup(
                    obtusePointLabels,
                    obtuseSideLabels,
                    obtuseTriangleHeightLabel
                )
            )
        )

        self.wait(2)

        self.play(
            FadeOut(
                obtuseTriangle,
                bottomLineExtension,
                obtuseTriangleHeightLine,
                obtuseTriangleHeightAngle,
                obtusePointLabels,
                obtuseSideLabels,
                obtuseTriangleHeightLabel,
                secondHeightArrow
            ),
            Restore(heightText),
            triangleWithLabels.animate.shift(LEFT * 3.1),
            VGroup(
                baseLine,
                heightArrow,
                heightText,
            ).animate.shift(LEFT * 3.1)
        )

        self.play(
            Transform(triangleSideLabels[0], MathTex(r"b", font_size=36, color=WHITE).move_to(midpointC + DOWN * 0.5)),
            FadeOut(heightArrow, heightText, baseLine),
            baseLine.animate.set_color(BLUE),
            heightLine.animate.set_color(BLUE),
            heightLabel.animate.set_color(WHITE),
            heightAngle.animate.set_color(BLUE)
        )

        self.wait(2)

        # Side definitions

        pointA = triangle.get_vertices()[0]
        pointB = triangle.get_vertices()[2]
        pointC = triangle.get_vertices()[1]

        lineAB = Line(start=pointA, end=pointB)
        lineAC = Line(start=pointA, end=pointC)

        lineBA = Line(start=pointB, end=pointA)
        lineBC = Line(start=pointB, end=pointC)

        lineCA = Line(start=pointC, end=pointA)
        lineCB = Line(start=pointC, end=pointB)

        self.play(
            lineAB.animate.set_color(RED),
            lineAC.animate.set_color(RED),
            trianglePointLabels[0].animate.set_color(RED),
            Transform(triangleSideLabels[0], MathTex(r"\text{lähiskülg}", font_size=36, color=RED).move_to(triangleSideLabels[0].get_center())),
            Transform(triangleSideLabels[2], MathTex(r"\text{lähiskülg}", font_size=36, color=RED).move_to(triangleSideLabels[2].get_center()).rotate(1.15)),
        )

        self.wait(4)

        self.play(
            lineBC.animate.set_color(GREEN),
            Transform(triangleSideLabels[1], MathTex(r"\text{vastaskülg}", font_size=36, color=GREEN).move_to(triangleSideLabels[1].get_center()).rotate(-0.55)),
        )

        self.wait(4)

        # reset

        midpointC = (triangle.get_vertices()[0] + triangle.get_vertices()[1]) / 2  # bottom side
        midpointA = (triangle.get_vertices()[1] + triangle.get_vertices()[2]) / 2  # right side
        midpointB = (triangle.get_vertices()[0] + triangle.get_vertices()[2]) / 2  # left side

        self.play(
            FadeOut(
                VGroup(
                    lineAB,
                    lineAC,
                    lineBC,
                    lineCA,
                    lineCB,
                    lineBA)),
            trianglePointLabels[0].animate.set_color(WHITE),
            Transform(triangleSideLabels[0], MathTex(r"b", font_size=36).move_to(midpointC + DOWN * 0.5)),
            Transform(triangleSideLabels[2], MathTex(r"a", font_size=36).move_to(midpointA + UP * 0.5)),
            Transform(triangleSideLabels[1], MathTex(r"c", font_size=36).move_to(midpointB + LEFT * 0.4 + UP * 0.2)),
        )

        self.wait(1)
        
        # Angle definitions

        angleA = Angle(lineAC, lineAB, radius=0.9, color=RED)
        angleB = Angle(lineBA, lineBC, radius=0.9, color=RED)
        angleC = Angle(lineCB, lineCA, radius=1.5, color=RED)

        angleAText = MathTex(r"\alpha", font_size=36, color=RED).move_to(angleA.get_center() + DOWN * 0.1 + LEFT * 0.15)
        angleBText = MathTex(r"\beta", font_size=36, color=RED).move_to(angleB.get_center() + UP * 0.15 + LEFT * 0.05)
        angleCText = MathTex(r"\gamma", font_size=36, color=RED).move_to(angleC.get_center() + RIGHT * 0.35 + DOWN * 0.075)

        self.play(
            Create(angleA),
            Create(angleB),
            Create(angleC),
            Write(angleAText),
            Write(angleBText),
            Write(angleCText),
            FadeOut(heightLine, heightLabel, heightAngle)
        )

        self.wait(4)

        angleARepresentation = MathTex(r"\alpha = \angle BAC", font_size=55, color=GREEN).move_to(DOWN * 2.5 + LEFT * 3)
        angleBRepresentation = MathTex(r"\beta = \angle ABC", font_size=55, color=RED).next_to(angleARepresentation, RIGHT * 1.5)
        angleCRepresentation = MathTex(r"\gamma = \angle BCA", font_size=55, color=BLUE_E).next_to(angleBRepresentation, RIGHT * 1.5)

        self.play(
            Write(VGroup(angleARepresentation, angleBRepresentation, angleCRepresentation)),
            VGroup(
                angleA,
                angleAText,
            ).animate.set_color(GREEN),
            VGroup(
                angleB,
                angleBText,
            ).animate.set_color(RED),
            VGroup(
                angleC,
                angleCText,
            ).animate.set_color(BLUE_E),
        )
        
        self.wait(4)

        self.play(
            Transform(angleARepresentation, MathTex(r"\alpha = \angle A", font_size=55, color=GREEN).move_to(DOWN * 2.5 + LEFT * 3)),
            Transform(angleBRepresentation, MathTex(r"\beta = \angle B", font_size=55, color=RED).next_to(angleARepresentation, RIGHT * 1.5)),
            Transform(angleCRepresentation, MathTex(r"\gamma = \angle C", font_size=55, color=BLUE_E).next_to(angleBRepresentation, RIGHT * 0.25)),
        )

        self.wait(4)
        
        self.play(
            FadeOut(
                angleARepresentation,
                angleBRepresentation,
                angleCRepresentation,
                angleB, angleBText, angleA,
                angleAText, angleC,
                angleCText),
            FadeIn(heightLabel, heightLine, heightAngle)
        )

        self.wait(2)

        self.play(
            triangleWithLabels.animate.shift(LEFT * 2.5)
        )

        self.wait(2)

        # Show calculation of perimeter

        perimeterFormula = MathTex(r"P = a + b + c", font_size=64, color=RED).move_to(RIGHT * 4)
        
        self.play(
            Write(perimeterFormula),
            triangle.animate.set_color(RED)
        )

        self.wait(2)

        arbitraryValues = MathTex(r"a = 4\text{ cm},\text{ }b = 5\text{ cm},\text{ }c = 3\text{ cm}", font_size=55, color=RED).next_to(perimeterFormula, UP * 2).shift(LEFT)

        self.play(
            Write(arbitraryValues)
        )

        self.wait(2)

        self.play(
            Transform(perimeterFormula, MathTex(r"P = 4 + 5 + 3\text{ cm}", font_size=64, color=RED).move_to(perimeterFormula.get_center())),
        )

        self.wait(2)

        self.play(
            Transform(perimeterFormula, MathTex(r"P = 12\text{ cm}", font_size=64, color=RED).move_to(perimeterFormula.get_center())),
        )

        self.wait(4)

        self.play(
            Transform(perimeterFormula, MathTex(r"P = a + b + c", font_size=64, color=WHITE).move_to(perimeterFormula.get_center())),
            triangle.animate.set_color(BLUE),
            FadeOut(arbitraryValues),
        )

        self.wait(4)

        self.play(
            perimeterFormula.animate.shift(UP)
        )

        # Show calculation of area

        areaFormula = MathTex(r"S = \frac{a \cdot h}{2}", font_size=64, color=RED).next_to(perimeterFormula, DOWN * 2)

        self.play(
            Write(areaFormula),
            triangle.animate.set_fill(RED, opacity=0.5)
        )

        self.wait(4)

        arbitraryValues = MathTex(r"b = 5\text{ cm},\text{ }h = 2\text{ cm}", font_size=55, color=RED).next_to(areaFormula, DOWN * 2)

        self.play(
            Write(arbitraryValues)
        )

        self.wait(2)

        self.play(
            Transform(areaFormula, MathTex(r"S = \frac{b \cdot h}{2}", font_size=64, color=RED).move_to(areaFormula.get_center())),
        )

        self.wait(2)

        self.play(
            Transform(areaFormula, MathTex(r"S = \frac{5 \cdot 2}{2}\text{ cm}^2", font_size=64, color=RED).move_to(areaFormula.get_center())),
        )
        
        self.wait(2)

        self.play(
            Transform(areaFormula, MathTex(r"S = \frac{10}{2}\text{ cm}^2", font_size=64, color=RED).move_to(areaFormula.get_center())),
        )
        
        self.wait(2)

        self.play(
            Transform(areaFormula, MathTex(r"S = 5\text{ cm}^2", font_size=64, color=RED).move_to(areaFormula.get_center())),
        )
        
        self.wait(4)

        self.play(
            triangle.animate.set_fill(WHITE, opacity=0),
            Transform(areaFormula, MathTex(r"S = \frac{a \cdot h}{2}", font_size=64, color=WHITE).move_to(areaFormula.get_center())),
            FadeOut(arbitraryValues),
        )

        self.wait(2)

        angleSum = MathTex(r"\alpha + \beta + \gamma = 180^{\circ}", font_size=55, color=RED).next_to(areaFormula, DOWN * 2)

        alphaPart = MathTex(r"\mathbf{\alpha}", font_size=80, color=GREEN)
        restPart = MathTex(r"+ \beta + \gamma = 180^{\circ}", font_size=55, color=RED)
        
        restPart.next_to(alphaPart, RIGHT, buff=0.2)
        
        angleSumAlpha = VGroup(alphaPart, restPart).move_to(angleSum.get_center())
        
        firstPart = MathTex(r"\alpha + ", font_size=55, color=RED)
        betaPart = MathTex(r"\mathbf{\beta}", font_size=80, color=GREEN)
        lastPart = MathTex(r"+ \gamma = 180^{\circ}", font_size=55, color=RED)

        firstPart.next_to(angleSum, LEFT, buff=0.2)
        betaPart.next_to(firstPart, RIGHT, buff=0.2)
        lastPart.next_to(betaPart, RIGHT, buff=0.2)

        angleSumBeta = VGroup(firstPart, betaPart, lastPart).move_to(angleSum.get_center())

        firstPartGamma = MathTex(r"\alpha + \beta + ", font_size=55, color=RED)
        gammaPart = MathTex(r"\mathbf{\gamma}", font_size=80, color=GREEN)
        lastPartGamma = MathTex(r"= 180^{\circ}", font_size=55, color=RED)

        firstPartGamma.next_to(angleSum, LEFT, buff=0.2)
        gammaPart.next_to(firstPartGamma, RIGHT, buff=0.2)
        lastPartGamma.next_to(gammaPart, RIGHT, buff=0.2)

        angleSumGamma = VGroup(firstPartGamma, gammaPart, lastPartGamma).move_to(angleSum.get_center())

        # Redefine points and lines to show that angle sum is 180 degrees
        pointA = triangle.get_vertices()[0]
        pointB = triangle.get_vertices()[2]
        pointC = triangle.get_vertices()[1]

        lineAB = Line(start=pointA, end=pointB)
        lineAC = Line(start=pointA, end=pointC)

        lineBA = Line(start=pointB, end=pointA)
        lineBC = Line(start=pointB, end=pointC)

        lineCA = Line(start=pointC, end=pointA)
        lineCB = Line(start=pointC, end=pointB)

        angleA = Angle(lineAC, lineAB, radius=0.9, color=RED)
        angleB = Angle(lineBA, lineBC, radius=0.9, color=RED)
        angleC = Angle(lineCB, lineCA, radius=1.5, color=RED)

        angleAText = MathTex(r"\alpha", font_size=36, color=RED).move_to(angleA.get_center() + DOWN * 0.1 + LEFT * 0.15)
        angleBText = MathTex(r"\beta", font_size=36, color=RED).move_to(angleB.get_center() + UP * 0.15 + LEFT * 0.05)
        angleCText = MathTex(r"\gamma", font_size=36, color=RED).move_to(angleC.get_center() + RIGHT * 0.35 + DOWN * 0.075)

        angles = VGroup(angleA, angleB, angleC,
                       angleAText, angleBText, angleCText)
        
        self.play(
            Write(angleSum),
            FadeOut(heightLine, heightLabel, heightAngle),
            Create(angles),
        )
        
        self.wait(2)

        self.play(
            angleA.animate.set_color(GREEN),
            angleAText.animate.set_color(GREEN),
            Transform(angleSum, angleSumAlpha)
        )
        self.wait(2)

        self.play(
            angleA.animate.set_color(RED),
            angleAText.animate.set_color(RED),
            angleB.animate.set_color(GREEN),
            angleBText.animate.set_color(GREEN),
            Transform(angleSum, angleSumBeta)
        )

        self.wait(2)

        self.play(
            angleB.animate.set_color(RED),
            angleBText.animate.set_color(RED),
            angleC.animate.set_color(GREEN),
            angleCText.animate.set_color(GREEN),
            Transform(angleSum, angleSumGamma)
        )

        self.wait(2)

        self.play(
            angleC.animate.set_color(RED),
            angleCText.animate.set_color(RED),
            Transform(angleSum, MathTex(r"\alpha + \beta + \gamma = 180^{\circ}", font_size=55, color=WHITE).move_to(angleSum.get_center()))
        )

        self.wait(2)

        self.play(
            angles.animate.set_color(BLUE),
            Create(VGroup(heightLine, heightLabel, heightAngle))
        )
        
        self.wait(5)

        self.play(
            *[FadeOut(mobject) for mobject in self.mobjects]
        )
