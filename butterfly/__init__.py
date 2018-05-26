from paintbrush import PaintBrush

class PaintButterfly(PaintBrush):
    def equation(self, x, y):
        return ( y**6 + x**6 - x**2)
