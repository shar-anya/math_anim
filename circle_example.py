from manimlib.imports import *

class FirstDomain(Scene):
    def construct(self):
        # Before Transformation
        circle_domain = Circle() # creating circle mobject
        point_a = Dot(color=ORANGE) # creating a point (on the cirlce)
        point_b = Dot(color=PINK) # creating a point (inside the circle)
        point_c = Dot(color=BLUE) # creating a point (outside the circle)

        point_a.shift(1*RIGHT)
        point_b.shift(0.5*RIGHT+0.5*UP)
        point_c.shift(2*RIGHT+2*UP)

        # Labels for point

        label_point_a = TextMobject("A"); label_point_a.shift(1.3*RIGHT+0.3*DOWN)
        label_point_b = TextMobject("B"); label_point_b.shift(0.2*RIGHT+0.2*UP)
        label_point_c = TextMobject("C"); label_point_c.shift(2.7*RIGHT+1.7*UP)


        self.play(ShowCreation(circle_domain))
        self.play(ShowCreation(point_a), ShowCreation(point_b), ShowCreation(point_c))
        self.play(ShowCreation(label_point_a), ShowCreation(label_point_b), ShowCreation(label_point_c))
        self.wait(2)


        ## In video explanation
        intro_text1 = TextMobject(r"Consider a circle in a 2D plane with three points about it:"); intro_text1.scale(0.6)
        intro_text2 = TextMobject(r"one inside, one outside, and one on the boundary of the circle."); intro_text2.scale(0.6)
        intro_text1.shift(2.3*DOWN)
        intro_text2.shift(2.65*DOWN)
        self.play(ShowCreation(intro_text1))
        self.play(ShowCreation(intro_text2))
        self.wait(5)


        transformation_text1 = TextMobject(r" Imagine that the circle is squished and stretched so that it becomes an ellipse.");transformation_text1.scale(0.6)
        transformation_text2 = TextMobject(r""" When we do that, the \textbf{entire} 2D plane (including the circle and all the points)\
                                                will be stretched and squished"""); transformation_text2.scale(0.6)
        transformation_text1.shift(2.3*DOWN)
        transformation_text2.shift(2.85*DOWN)
        self.play(Transform(intro_text1, transformation_text1),FadeOut(intro_text2))
        self.wait(2)

        ellipse_range = Ellipse(width=4, height=1, color=BLUE)
        function_label_a = TextMobject("$f(A)$"); function_label_a.shift(2.4*RIGHT+0.3*DOWN); function_label_a.scale(0.75)
        function_label_b = TextMobject("$f(B)$"); function_label_b.shift(0.2*RIGHT); function_label_b.scale(0.75)
        function_label_c = TextMobject("$f(C)$"); function_label_c.shift(4*RIGHT+0.25*UP); function_label_c.scale(0.75)

        self.play(Transform(circle_domain, ellipse_range),
        ApplyMethod(point_a.shift, 1*RIGHT),
        ApplyMethod(point_b.shift, 0.5*RIGHT+0.25*DOWN),
        ApplyMethod(point_c.shift, 2*RIGHT+1*DOWN),
        Transform(label_point_a, function_label_a),
        Transform(label_point_b, function_label_b),
        Transform(label_point_c, function_label_c))
        self.wait(1)
        self.play(FadeIn(transformation_text2))
        self.wait(5)
        self.play(FadeOut(intro_text1), FadeOut(transformation_text2))
        self.wait(2)

        # AFTER TRANSFORMATION
        more_explanation = TextMobject(r"All the points on the plane will be \textit{transformed}.\\ \
            This stretching and squishing action is known as a Transformation, and is represented by $f$.\
            Eg: $f(x,y) = ( \sin(x), \cos(y) )$\\ \
            (i.e \textit{for all points x in the 2D plane, we calculate f(x,y)})"); more_explanation.scale(0.6);
        more_explanation.shift(2.3*DOWN)


        self.play(ShowCreation(more_explanation))
        self.wait(11)
