from rpython.rlib import jit


class OpCode():
    LOAD_CONST = 0
    LOAD_VAR = 1
    ADD = 2
    MULTIPLY = 3
    DIVIDE = 4
    SUBTRACT = 5
    MOD = 6
    STORE_VAR = 7
    PRINT = 8
    INPUT = 9
    CMPNEQ = 10
    CMPEQ = 11
    CMPLT = 12
    CMPGT = 13
    JMP = 14
    CALL = 15
    MAKE_FUNCTION = 16
    RETURN = 17
    PASS = 18


_stack_effects = [
    1,  # LOAD_CONST
    1,  # LOAD_VAR
    -1,  # ADD
    -1,  # MULTIPLY
    -1,  # DIVIDE
    -1,  # SUBTRACT
    -1,  # MOD
    -1,  # STORE_VAR
    -1,  # PRINT
    1,  # INPUT
    -2,  # CMPNEQ
    -2,  # CMPEQ
    -2,  # CMPLT
    -2,  # CMPGT
    0,  # JMP
    0,  # CALL
    0,  # MAKE_FUNCTION
    0,  # RETURN
    0,  # PASS
]


@jit.elidable
def stack_effect(opcode):
    assert opcode >= 0 and opcode < len(_stack_effects)
    return _stack_effects[opcode]