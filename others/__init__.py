from paintbrush import PaintBrush, PaintBrushIntersection


class Descartes(PaintBrush):
    def equation(self, x, y):
        return (x**3 + y**3 - 3*2*x*y)


class Dk(PaintBrush):
    def __init__(
        self,
        x_border=(-2, 2),
        y_border=(1.5, -3),
        x_step=0.05,
        y_step=-0.05
    ):
        super().__init__(
            x_border=x_border,
            y_border=y_border,
            x_step=x_step,
            y_step=y_step,
        )

    def equation(self, x, y):
        return (x**2 + y*2 - 1)**3 - (x**2)*(y**3) - 1


class Mouse(PaintBrush):
    def __init__(
        self,
        x_border=(-1.2, 1.2),
        y_border=(1.3, -1.1),
        x_step=0.04,
        y_step=-0.09
    ):
        super().__init__(
            x_border=x_border,
            y_border=y_border,
            x_step=x_step,
            y_step=y_step,
        )

    def equation(self, x, y):
        return (x**2 + y**2 - 1)**3 - (x**2)*(y**3) + 0.1


class Parabola(PaintBrushIntersection):
    def __init__(
        self,
        x_border=(-1, 1),
        y_border=(-0.5, 0.5),
        x_step=0.1,
        y_step=0.1,
        **kwargs
    ):
        super().__init__(
            x_border=x_border,
            y_border=y_border,
            x_step=x_step,
            y_step=y_step,
        )

    def equation(self, x, y):
        return (x**2/2 + y**2/3 - 1)

    def equation_under(self, x, y):
        return ((x + 0.5)**2/2 + y**2/3 - 1)
