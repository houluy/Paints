from paintbrush import PaintBrush

class PaintHeart(PaintBrush):
    def equation(self, x, y):
        return (x**2 + y**2 - 1)**3 + (x**2)*(y**3)

class PaintHeart2(PaintBrush):
    def equation(self, x, y):
        return (x**2 + (5*y/4 - abs(x)**(0.5))**2 - 1)

