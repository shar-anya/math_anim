#line 112
dot1 = Dot(color = MAROON_C, radius = 0.07)
dot1.shift(self.graph_origin + X_TICKS_DISTANCE*RIGHT)
dot2 = dot1.copy()
dot2.shift(X_TICKS_DISTANCE*RIGHT)
dot3 = dot1.copy()
dot3.shift(X_TICKS_DISTANCE*2*RIGHT)

#line 115
dot1b = Dot(color = BLUE_C, radius = 0.07)
dot1b.shift(self.graph_origin + Y_TICKS_DISTANCE*np.sin(1)*UP)
dot2b = Dot(color = BLUE_E, radius = 0.07)
dot2b.shift(self.graph_origin + Y_TICKS_DISTANCE*np.sin(2)*UP)
dot3b = Dot(color = BLUE_D, radius = 0.07)
dot3b.shift(self.graph_origin + Y_TICKS_DISTANCE*np.sin(3)*UP)

#line 121
dotlabel1 = TextMobject("1"); dotlabel1.scale(0.5)
dotlabel1.shift(self.graph_origin+(X_TICKS_DISTANCE)*RIGHT+ 0.3*DOWN)
dotlabel2 = TextMobject("2"); dotlabel2.scale(0.5)
dotlabel2.shift(self.graph_origin+(2*X_TICKS_DISTANCE)*RIGHT+ 0.3*DOWN)
dotlabel3 = TextMobject("3"); dotlabel3.scale(0.5)
dotlabel3.shift(self.graph_origin+(3*X_TICKS_DISTANCE)*RIGHT+ 0.3*DOWN)

# line 133
self.play(ApplyMethod(dot1a.shift, np.sin(1)*Y_TICKS_DISTANCE*UP), ShowCreation(dot1b))
self.play(ApplyMethod(dot2a.shift, np.sin(2)*Y_TICKS_DISTANCE*UP), ShowCreation(dot2b))
self.play(ApplyMethod(dot3a.shift, np.sin(3)*Y_TICKS_DISTANCE*UP), ShowCreation(dot3b))

#line 141
dash1 = Rectangle(height = 0.01, width = 0.1, color = BLUE_D)
dash2 = dash1.copy()
dash1.shift(self.graph_origin+ Y_TICKS_DISTANCE*UP)
dash2.shift(self.graph_origin+ Y_TICKS_DISTANCE*DOWN)

#line 149
arrowtip1 = ArrowTip(color = MAROON_C)
arrowtip2 = ArrowTip(color = MAROON_C, start_angle = 0)
arrowtip1.scale(0.5)
arrowtip2.scale(0.5)
arrowtip1.shift(self.graph_origin+ 4.7*X_TICKS_DISTANCE*LEFT)
arrowtip2.shift(self.graph_origin+ 4.7*X_TICKS_DISTANCE*RIGHT)
