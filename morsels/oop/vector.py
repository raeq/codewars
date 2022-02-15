class Vector:
    __slots__ = ["_x", "_y", "_z"]

    def __init__(self, *args, x=None, y=None, z=None, **kwargs):
        if len(args) == 3:
            x, y, z = args[0], args[1], args[2]
        self._x = x
        self._y = y
        self._z = z

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def z(self):
        return self._z

    def __eq__(self, other):
        if isinstance(other, Vector):
            return str(self) == str(other)
        else:
            return NotImplemented

    def __ne__(self, other):
        if isinstance(other, Vector):
            return str(self) != str(other)
        else:
            return NotImplemented

    def __rmul__(self, other):
        return self.__mul__(other)

    def __mul__(self, other):
        if isinstance(other, int):
            return Vector(other * self.x, other * self.y, other * self.z)
        else:
            return NotImplemented

    def __truediv__(self, other):
        if isinstance(other, int):
            return Vector(self.x / other, self.y / other, self.z / other)
        else:
            return NotImplemented

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y, self.z + other.z)
        else:
            return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y, self.z - other.z)
        else:
            return NotImplemented

    def __str__(self):
        return f"{self._x} {self._y} {self._z}"

    def __repr__(self):
        return f"{self.__class__.__name__}(x={self.x}, y={self.y}, z={self.z})"

    def __iter__(self):
        yield self.x
        yield self.y
        yield self.z
