from primitive_object import PrimitiveObject
from null import Null


class Char(PrimitiveObject):
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

    def eq(self, rhs):
        assert isinstance(rhs, PrimitiveObject)
        if isinstance(rhs, Null):
            return False
        else:
            assert isinstance(rhs, Char)
            result = self.value == rhs.value
            return result

    def neq(self, rhs):
        assert isinstance(rhs, PrimitiveObject)
        if isinstance(rhs, Null):
            return True
        else:
            assert isinstance(rhs, Char)
            result = self.value != rhs.value
            return result
