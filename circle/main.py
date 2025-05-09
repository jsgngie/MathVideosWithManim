from manim import *
import math

class DefaultTemplate(Scene):

    def construct(self):

        title = Text("Ring", font_size=60)

        self.play(Write(title))

        self.wait(1)

        self.play(FadeOut(title))
        
        # Create the circle

        circle = Circle(2, color=BLUE)

        self.play(Create(circle))

        centerDot = Dot(circle.get_center(), color=RED)

        self.play(Create(centerDot))

        self.wait(0.5)

        # Highlight the center dot

        dotArrow = Arrow(circle.get_center() + UP * 2 + RIGHT * 3, circle.get_center(), color=RED, stroke_width=3)

        centerDotLabel = Text("Ringi keskpunkt", color=RED, font_size=36).move_to(dotArrow.get_start() + UP * 0.5)

        self.play(Create(dotArrow), Write(centerDotLabel))

        self.wait(1)

        self.play(
            FadeOut(dotArrow, centerDotLabel),
            centerDot.animate.set_fill(BLUE)
        )

        self.wait(1)

        self.play(circle.animate.move_to(LEFT * 3), centerDot.animate.move_to(LEFT * 3))

        # Create the radius line and label

        radiusLine = Line(circle.get_center(), circle.get_center() + LEFT * 2, color=BLUE)
        radiusLabel = MathTex(r"r", color=BLUE).next_to(radiusLine, UP)

        self.play(Create(radiusLine), Write(radiusLabel))

        self.wait(1)

        radiusText = MathTex(r"r = 3\text{ cm}").move_to(RIGHT * 3.5 + UP * 2)

        self.play(Write(radiusText))

        self.wait(1)

        # Highlight the full circle angle

        circleAngleText = MathTex(r"360^\circ = 2\pi \text{ rad}", color=RED).next_to(circle, UP)
        circleFullAngle = Circle(2, color=RED).move_to(circle.get_center()).rotate(PI, axis=[0, 0, 1]).rotate(PI, axis=[0, 1, 0])

        self.play(Create(circleFullAngle), Write(circleAngleText))

        self.wait(1)

        self.play(
            FadeOut(circleAngleText, circleFullAngle),
            radiusText.animate.set_fill(WHITE)
        )

        self.wait(1)

        # Highlight the diameter line and label

        secondRadiusLine = Line(circle.get_center(), circle.get_center() + RIGHT * 2, color=RED)
        diameterLabel = MathTex(r"d", color=RED).next_to(circle.get_center(), DOWN)
        secondRadiusLabel = MathTex(r"r", color=BLUE).next_to(secondRadiusLine.get_center(), UP)

        self.play(
            Create(VGroup(secondRadiusLine, diameterLabel, secondRadiusLabel)),
            radiusLine.animate.set_color(RED)
        )

        diameterText = MathTex(r"d = 6\text{ cm}", color=RED).next_to(radiusText, DOWN)

        self.play(Write(diameterText))

        self.wait(1)

        diameterText.set_fill(WHITE)

        self.wait(1)

        # Sectors

        sectorLineOne = Line(circle.get_center() + LEFT * 2, circle.get_center(), color=RED)
        sectorLineTwo = Line(circle.get_center(), circle.get_center() + UP * 2, color=RED).rotate(-PI / 1.5, about_point=circle.get_center())
        sectorAngle = Angle(sectorLineTwo, sectorLineOne, radius=0.75, color=RED, dot_color=RED, quadrant=(1, -1))
        sectorAngleTwo = Angle(sectorLineTwo, sectorLineOne, radius=0.75, color=RED, dot_color=RED, quadrant=(-1, 1))

        theta = MathTex(r"\theta", color=GREEN).move_to(sectorAngle.get_center() +UP * 0.25)
        thetaPrime = MathTex(r"\theta'", color=YELLOW).move_to(sectorAngleTwo.get_center() + DOWN * 0.25)

        invisSectorLine = Line(circle.get_center() + LEFT * 2, circle.get_center(), color=GREEN, stroke_opacity=0)
        invisSectorLineTwo = Line(circle.get_center(), circle.get_center() + UP * 2, color=GREEN, stroke_opacity=0).rotate(-PI / 6, about_point=circle.get_center())
        invisSectorAngle = Angle(invisSectorLineTwo, invisSectorLine, radius=0.75, color=RED, dot_color=GREEN, quadrant=(1, -1))

        # Define the angle in radians
        angle = PI / 2

        # Create the arcs
        arcOne = Arc(radius=2, start_angle=-PI, angle=-(7 * PI / 6), color=GREEN).move_to(circle.get_center() + UP * 0.5)
        arcTwo = Arc(radius=2, start_angle=-PI, angle=(5 * PI / 6), color=YELLOW).move_to(circle.get_center() + DOWN + LEFT * 0.13)

        arcText = Text("Kaared", color=RED, font_size=36).move_to(RIGHT * 0.5)
        arrowArcOne = CurvedArrow(arcText.get_center() + UP * 0.5, arcOne.get_center() + UP + RIGHT * 1.5, color=GREEN)
        arrowArcTwo = CurvedArrow(arcText.get_center() + DOWN * 0.5, arcTwo.get_center() + DOWN + RIGHT, color=YELLOW, angle=-TAU/4)

        self.play(
            Create(
                VGroup(
                    sectorLineOne,
                    sectorLineTwo,
                    sectorAngle,
                    sectorAngleTwo,
                    theta,
                    thetaPrime,
                    invisSectorLine,
                    invisSectorLineTwo,
                    arcOne,
                    arcTwo,
                    arcText,
                    arrowArcOne,
                    arrowArcTwo
                )),
            FadeOut(
                radiusLine,
                secondRadiusLine, 
                diameterLabel,
            ),
            secondRadiusLabel.animate.move_to(secondRadiusLine.get_center() + DOWN * 0.25 + RIGHT * 0.1),
            run_time=2
        )

        self.wait(1)

        arcThree = Arc(radius=2, start_angle=-PI, angle=-(PI / 2 + PI / 6), color=GREEN).move_to(circle.get_center() + UP + LEFT * 0.5)

        self.play(
            Rotate(sectorLineTwo, angle, about_point=circle.get_center()),
            FadeOut(sectorAngleTwo, thetaPrime, arcTwo, arcText, arrowArcTwo, arrowArcOne, arcOne),
            Transform(sectorAngle, invisSectorAngle),
            FadeIn(arcThree),
            theta.animate.shift(LEFT * 0.15 + DOWN * 0.05),
            secondRadiusLabel.animate.move_to(invisSectorLineTwo.get_center() + RIGHT * 0.25 + DOWN * 0.25)
        )

        self.wait(1)

        sectorArea = AnnularSector(
            inner_radius=0,
            outer_radius=2,
            start_angle=-PI,
            angle=-angle - PI / 6,
            color=RED_A
        ).move_to(circle.get_center() + UP + LEFT * 0.5)

        self.play(FadeIn(sectorArea.set_opacity(0.3)))

        self.wait(1)

        # Sector area formulas, conversions and calculations

        sectorAreaRadiansText = MathTex(r"S_{\text{sektor}} = \frac{r^2 \cdot \theta}{2} \text{ cm}^2", color=RED).move_to(RIGHT * 4.5 + UP * 0.25)
        areaRadiansText = MathTex(r"\text{Radiaanides: }", color=WHITE).next_to(sectorAreaRadiansText, LEFT * 1.1)

        sectorAreaDegreesText = MathTex(r"S_{\text{sektor}} = \frac{r^2 \cdot \frac{\theta \cdot \pi}{180}}{2} \text{ cm}^2", color=RED).next_to(sectorAreaRadiansText, DOWN * 1.5)
        areaDegreesText = MathTex(r"\text{Kraadides: }", color=WHITE).next_to(sectorAreaDegreesText, LEFT * 1.1)

        self.play(Write(VGroup(sectorAreaRadiansText, areaRadiansText, sectorAreaDegreesText, areaDegreesText)))

        self.wait(1)

        convertingRadiansToDegrees = MathTex(r"\theta \cdot \frac{\pi}{180}", color=BLUE).next_to(sectorAreaDegreesText, DOWN + LEFT * 1.5)
        arrow = CurvedArrow(convertingRadiansToDegrees.get_center() + RIGHT, sectorAreaDegreesText.get_center() + RIGHT * 0.5, color=BLUE)

        self.play(Write(convertingRadiansToDegrees), Create(arrow))

        self.wait(1)

        self.play(FadeOut(arrow, convertingRadiansToDegrees, sectorAreaDegreesText, areaDegreesText))
        
        self.play(
            sectorAreaRadiansText.animate.shift(DOWN + LEFT),
            FadeOut(areaRadiansText)
        )

        thetaText = MathTex(r"\theta = 2{,}09 \text{ rad}", color=WHITE).next_to(diameterText, DOWN)
        sectorAngleInRadians = MathTex(r"\text{2,09}", font_size=30, color=RED).move_to(theta.get_center() + LEFT * 0.05)

        self.play(Transform(theta, sectorAngleInRadians), Write(thetaText))

        self.wait(1)

        newRadiansSectorAreaTextFirst = MathTex(r"S_{\text{sektor}} = \frac{3^2 \cdot 2{,}09}{2} \text{ cm}^2", color=RED).move_to(sectorAreaRadiansText.get_center())

        self.play(Transform(sectorAreaRadiansText, newRadiansSectorAreaTextFirst))

        newRadiansSectorAreaTextSecond = MathTex(r"S_{\text{sektor}} = \frac{18{,}81}{2} \text{ cm}^2", color=RED).move_to(newRadiansSectorAreaTextFirst.get_center() + LEFT * 0.3)

        self.play(Transform(sectorAreaRadiansText, newRadiansSectorAreaTextSecond))

        newRadiansSectorAreaTextThird = MathTex(r"S_{\text{sektor}} = 9{,}405 \text{ cm}^2", color=RED).move_to(newRadiansSectorAreaTextSecond.get_center())

        self.play(Transform(sectorAreaRadiansText, newRadiansSectorAreaTextThird))

        self.wait(2)

        sectorAreaDegreesText.move_to(sectorAreaRadiansText.get_center())
        areaDegreesText.move_to(areaRadiansText.get_center())

        self.play(Transform(sectorAreaRadiansText, sectorAreaDegreesText))

        self.wait(1)

        sectorAngleInDegrees = MathTex(r"120^\circ", color=RED, font_size=30).move_to(sectorAngleInRadians.get_center())

        self.play(
            Transform(theta, sectorAngleInDegrees), FadeIn(convertingRadiansToDegrees),
            Transform(thetaText, MathTex(r"\theta = 120^\circ", color=WHITE).move_to(thetaText.get_center()))
            )

        convertingRadiansToDegreesSecond = MathTex(r"120^\circ \cdot \frac{\pi}{180}", color=BLUE).move_to(convertingRadiansToDegrees.get_center())

        self.play(Transform(convertingRadiansToDegrees, convertingRadiansToDegreesSecond))

        self.wait(1)

        convertingRadiansToDegreesThird = MathTex(r"120^\circ \cdot \frac{\pi}{180} \approx 2{,}09 \text{ rad}", color=BLUE).move_to(convertingRadiansToDegrees.get_center())

        newArrow = CurvedArrow(convertingRadiansToDegreesThird.get_center() + RIGHT * 2.5, sectorAreaDegreesText.get_center() + RIGHT * 0.9 + DOWN * 0.25, color=BLUE)

        self.play(Transform(convertingRadiansToDegrees, convertingRadiansToDegreesThird), Create(newArrow))

        self.wait(1)

        sectorAreaDegreesTextSecond = MathTex(r"S_{\text{sektor}} \approx \frac{3^2 \cdot 2{,}09}{2} \text{ cm}^2", color=RED).move_to(sectorAreaDegreesText.get_center())

        self.play(FadeOut(newArrow), Transform(sectorAreaRadiansText, sectorAreaDegreesTextSecond))

        self.wait(1)

        sectorAreaDegreesTextThird = MathTex(r"S_{\text{sektor}} \approx 9{,}405 \text{ cm}^2", color=RED).move_to(sectorAreaDegreesText.get_center())

        self.play(Transform(sectorAreaRadiansText, sectorAreaDegreesTextThird))

        self.wait(1)

        # Perimeter and area of the circle

        diameterLine = Line(circle.get_center() + LEFT * 2, circle.get_center() + RIGHT * 2, color=BLUE)
        secondRadiusLine.rotate(PI / 2, about_point=circle.get_center()).set_color(BLUE)

        self.play(
            FadeOut(
                sectorAreaRadiansText,
                convertingRadiansToDegrees,
                sectorAngle,
                sectorLineOne,
                sectorLineTwo,
                theta,
                sectorArea,
                thetaText,
                secondRadiusLabel,
                arcThree,
            ),
            radiusLabel.animate.move_to(secondRadiusLine.get_center() + LEFT * 0.5),
            FadeIn(secondRadiusLine, diameterLine, diameterLabel.set_color(BLUE))
        )

        self.wait(1)

        perimeterCircle = Circle(2, color=RED, stroke_width=6).move_to(LEFT * 3)

        perimeterFormula = MathTex(r"C = 2\pi r", color=RED).next_to(diameterText, DOWN * 3)

        self.play(Write(perimeterFormula), Create(perimeterCircle), run_time=1.5)

        transformedPerimeterFormula = MathTex(r"C = 2\cdot\pi \cdot 3\text{ cm}", color=RED).move_to(perimeterFormula.get_center())

        self.play(Transform(perimeterFormula, transformedPerimeterFormula))

        self.wait(1)

        transformedPerimeterFormulaTwo = MathTex(r"C = 6\pi \text{ cm}", color=RED).move_to(perimeterFormula.get_center())

        self.play(Transform(perimeterFormula, transformedPerimeterFormulaTwo))

        self.wait(1)

        finalPerimeterFormula = MathTex(r"C = 6\pi  \approx   18{,}85\text{ cm}", color=RED).move_to(perimeterFormula.get_center())

        self.play(Transform(perimeterFormula, finalPerimeterFormula))

        self.wait(1)

        self.play(FadeOut(perimeterCircle), perimeterFormula.animate.set_fill(WHITE))

        self.wait(1)

        self.play(
            FadeOut(
                VGroup(
                    secondRadiusLine,
                    radiusLabel,
                    diameterLabel,
                    diameterLine,
                )
            )
        )

        self.wait(0.5)

        circleFillHack = AnnularSector(
            inner_radius=0,
            outer_radius=2,
            start_angle=0,
            angle=TAU,
            color=RED,
        ).move_to(circle.get_center())

        areaText = MathTex(r"S = \pi r^2", color=RED).next_to(perimeterFormula, DOWN)
        newRadius = Line(circle.get_center(), circle.get_center() + RIGHT * 2, color=RED)

        self.play(
            Write(areaText),
            Create(newRadius)
        )
        
        self.play(
            Create(circleFillHack, run_time=4, rate_func=double_smooth)
        )

        self.wait(1)

        transformedAreaTextZero = MathTex(r"S = \pi \cdot 3^2\text{ cm}^2", color=RED).move_to(areaText.get_center())

        self.play(Transform(areaText, transformedAreaTextZero))

        transformedAreaText = MathTex(r"S = \pi  \cdot 3 \cdot 3\text{ cm}^2", color=RED).move_to(areaText.get_center())

        self.play(Transform(areaText, transformedAreaText))

        self.wait(1)

        transformedAreaTextTwo = MathTex(r"S = 9\pi \text{ cm}^2", color=RED).move_to(areaText.get_center())

        self.play(Transform(areaText, transformedAreaTextTwo))

        self.wait(1)

        finalAreaFormula = MathTex(r"S = 9\pi  \approx   28{,}27\text{ cm}^2", color=RED).move_to(areaText.get_center())

        self.play(Transform(areaText, finalAreaFormula), FadeOut(newRadius))

        self.wait(1)

        self.play(FadeOut(circleFillHack), areaText.animate.set_fill(WHITE))
        
        finalAngle = Angle(secondRadiusLine, diameterLine, radius=0.75, color=BLUE, quadrant=(1, -1))
        finalTheta = MathTex(r"\theta", color=BLUE).move_to(finalAngle.get_center() + RIGHT * 0.075)
        self.play(
            FadeIn(diameterLine, secondRadiusLine, diameterLabel, radiusLabel, finalAngle),
            Write(finalTheta)
        )

        self.play(
            VGroup(
                radiusText,
                diameterText,
                perimeterFormula,
                areaText,
            ).animate.shift(UP * 0.75)
        )

        # Final screen of formulas

        sectorAreaFormulaDegreesFinal = MathTex(r"S_{\text{sektor}} =\frac{r^2 \cdot \frac{\theta \cdot \pi}{180}}{2} \text{ cm}^2").move_to(RIGHT * 4.25 + DOWN)
        sectorAreaDegreesTextFinal = MathTex(r"\text{Kraadides: }").next_to(sectorAreaFormulaDegreesFinal, LEFT)
        sectorAreaFormulaRadiansFinal = MathTex(r"S_{\text{sektor}} = \frac{r^2 \cdot \theta}{2} \text{ cm}^2").next_to(sectorAreaFormulaDegreesFinal, DOWN * 1.5)
        sectorAreaRadiansTextFinal = MathTex(r"\text{Radiaanides: }").next_to(sectorAreaFormulaRadiansFinal, LEFT)
        circleAngleText.set_color(BLUE)

        self.play(
            FadeIn(
                sectorAreaFormulaDegreesFinal,
                sectorAreaFormulaRadiansFinal,
                sectorAreaDegreesTextFinal,
                sectorAreaRadiansTextFinal,
                circleAngleText.next_to(circle, UP * 0.8)
            )
        )

        self.wait(3)

        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )