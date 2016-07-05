from support import lib,ffi
from qcgc_test import QCGCTest

class GrayStackTestCase(QCGCTest):
    def test_create(self):
        """Test creation"""
        for i in range(100):
            s = lib.qcgc_gray_stack_create(i)
            self.assertEqual(s.size, i)
            self.assertEqual(s.index, 0)

    def test_push_pop(self):
        """Test push/pop"""
        stack = lib.qcgc_gray_stack_create(1000)
        pythonstack = list()

        for i in range(1000):
            stack = lib.qcgc_gray_stack_push(stack, ffi.cast("object_t *", i))
            pythonstack.append(ffi.cast("object_t *", i))

        self.assertEqual(stack.index, 1000)

        while pythonstack:
            p = lib.qcgc_gray_stack_pop(stack);
            self.assertEqual(p, pythonstack.pop())

        self.assertEqual(stack.index, 0)

    def test_grow(self):
        """Test automatic growing"""
        stack = lib.qcgc_gray_stack_create(10)
        pythonstack = list()

        for i in range(1000):
            stack = lib.qcgc_gray_stack_push(stack, ffi.cast("object_t *", i))
            pythonstack.append(ffi.cast("object_t *", i))

        self.assertEqual(stack.index, 1000)

        while pythonstack:
            p = lib.qcgc_gray_stack_pop(stack);
            self.assertEqual(p, pythonstack.pop())

        self.assertEqual(stack.index, 0)