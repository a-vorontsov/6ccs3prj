from primitive_object import PrimitiveObject
from null import Null


class Integer(PrimitiveObject):
    __slots__ = ("value",)
    _immutable_fields_ = ("value",)

    def __init__(self, value):
        self.value = value

    def get_value(self):
        return self.value

    def get_string(self):
        return str(self.value)

    def pprint(self):
        print self.get_string()

    def add(self, rhs):
        assert isinstance(rhs, Integer)
        result = self.value + rhs.value
        return Integer(int(result))

    def sub(self, rhs):
        assert isinstance(rhs, Integer)
        result = self.value - rhs.value
        return Integer(int(result))

    def mul(self, rhs):
        assert isinstance(rhs, Integer)
        result = self.value * rhs.value
        return Integer(int(result))

    def div(self, rhs):
        assert isinstance(rhs, Integer)
        if rhs.value == 0:
            raise ValueError
        result = self.value // rhs.value
        return Integer(int(result))

    def mod(self, rhs):
        assert isinstance(rhs, Integer)
        result = self.value % rhs.value
        return Integer(int(result))

    def eq(self, rhs):
        assert isinstance(rhs, PrimitiveObject)
        if isinstance(rhs, Null):
            return False
        else:
            assert isinstance(rhs, Integer)
            result = self.value == rhs.value
            return result

    def neq(self, rhs):
        assert isinstance(rhs, PrimitiveObject)
        if isinstance(rhs, Null):
            return True
        else:
            assert isinstance(rhs, Integer)
            result = self.value != rhs.value
            return result

    def lt(self, rhs):
        assert isinstance(rhs, Integer)
        result = self.value < rhs.value
        return result

    def le(self, rhs):
        assert isinstance(rhs, Integer)
        result = self.value <= rhs.value
        return result

    def gt(self, rhs):
        assert isinstance(rhs, Integer)
        result = self.value > rhs.value
        return result

    def ge(self, rhs):
        assert isinstance(rhs, Integer)
        result = self.value >= rhs.value
        return result
