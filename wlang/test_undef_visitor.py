import unittest
import wlang.ast as ast
import wlang.undef_visitor as undef_visitor

class TestUndefsVisitor (unittest.TestCase):
    def test_one (self):
        prg1 = "x := 10; y := x + z"
        ast1 = ast.parse_string (prg1)

        uv = undef_visitor.UndefVisitor ()
        uv.check (ast1)
        # UNCOMMENT to run the test
        self.assertEquals (set ([ast.IntVar('z')]), uv.get_undefs ())

    def test_havoc (self):
        prg1 = """
            havoc x, y;
            if x > y then
                x := y
            else
                y := x;
            assert x = z;
            print_state
        """
        ast1 = ast.parse_string (prg1)

        uv = undef_visitor.UndefVisitor ()
        uv.check (ast1)
        # UNCOMMENT to run the test
        self.assertEquals (set ([ast.IntVar('z')]), uv.get_undefs ())

    def test_while (self):
        prg1 = """
            x := 10;
            assume x > 0;
            while x > 0 do
                x := x -1;
            print_state
        """
        ast1 = ast.parse_string (prg1)

        uv = undef_visitor.UndefVisitor ()
        uv.check (ast1)
        # UNCOMMENT to run the test
        self.assertEquals (set ([]), uv.get_undefs ())
