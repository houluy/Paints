class PaintBrush:
    def __init__(
        self,
        color='black',
        x_border=(-1.2, 1.2),
        y_border=(1.3, -1.1),
        x_step=0.04,
        y_step=-0.09,
    ):
        self.x_border = x_border
        self.y_border = y_border
        self.x_step = x_step
        self.y_step = y_step
        self.x_num = int((x_border[1] - x_border[0]) / x_step)
        self.y_num = int((y_border[1] - y_border[0]) / y_step)
        self._form_field()

    def equation(self, x, y):
        return 0

    def draw_logic(self, x, y):
        res = self.equation(x, y)
        return False if res > 0 else True

    def _form_field(self):
        self.field = [
            (
                self.x_border[0] + x*self.x_step,
                self.y_border[0] + y*self.y_step
            )
            for y in range(self.y_num)
            for x in range(self.x_num)
        ]

    def paint(self):
        last_x, last_y = self.field[0]
        for x, y in self.field:
            if y < last_y:
                print()
            last_x, last_y = x, y
            if self.draw_logic(x, y):
                print('*', end='')
            else:
                print(' ', end='')
        print()

class PaintHeart(PaintBrush):
    def equation(self, x, y):
        return (x**2 + y**2 - 1)**3 + (x**2)*(y**3)

class PaintHeart2(PaintBrush):
    def equation(self, x, y):
        return (x**2 + (5*y/4 - abs(x)**(0.5))**2 - 1)

pb = PaintHeart2()
pb.paint()
