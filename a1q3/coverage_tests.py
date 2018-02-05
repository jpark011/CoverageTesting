import unittest
from a1q3 import M

class CoverageTests (unittest.TestCase):
    def test_1 (self):
        """Comment"""
        o = M ()
        # NC
        o.m([], 0)
        o.m([1], 0)
        o.m([1,2], 0)
        o.m([1,2,3], 0)
        pass

    def test_2 (self):
        """Comment"""
        o = M ()
        # NC
        o.m([], 0)
        o.m([1], 0)
        o.m([1,2], 0)
        o.m([1,2,3], 0)
        # need 1 more case for EC
        o.m([], 1)
        pass

    def test_3 (self):
        """Comment"""
        o = M ()
        # EPC does not differ from EC
        # since infeasible edge pairs exist
        # those feasible are covered by EC
        pass

    def test_4 (self):
        """Comment"""
        o = M ()
        # Similar to EPC, PPC does not differ from EC
        # since infeasible prime paths exist
        # and those feasilbe are already covered by EC
        pass
