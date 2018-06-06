from paintbrush import PaintBrush


class Ellipse(PaintBrush):
    def __init__(
        self,
        x_border=(-2.4, 2.4),
        y_border=(-1.5, 1.5),
        x_step=0.05,
    ):
        super().__init__(
            x_border=x_border,
            y_border=y_border,
            x_step=x_step,
        )

    def equation(self, x, y):
        return (x**2/5 + y**2/2 - 1)
