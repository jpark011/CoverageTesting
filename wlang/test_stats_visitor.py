import unittest
import wlang.ast as ast
import wlang.stats_visitor as stats_visitor

class TestStatsVisitor (unittest.TestCase):
    def test_one (self):
        prg1 = "x := 10; print_state"
        ast1 = ast.parse_string (prg1)

        sv = stats_visitor.StatsVisitor ()
        sv.visit (ast1)
        # UNCOMMENT to run the test
        self.assertEquals (sv.get_num_stmts (), 2)
        self.assertEquals (sv.get_num_vars (), 1)

    def test_if (self):
        prg1 = """
            x := 10;
            if x > 10 then
                x := 5
            else
                x := 15;
            print_state
        """
        ast1 = ast.parse_string (prg1)

        sv = stats_visitor.StatsVisitor ()
        sv.visit (ast1)
        # UNCOMMENT to run the test
        self.assertEquals (sv.get_num_stmts (), 5)
        self.assertEquals (sv.get_num_vars (), 1)

    def test_while (self):
        prg1 = """
            x := 10;
            y := 0;
            z := 0;
            while x > 0 do
                y := y + 1;
            print_state
        """
        ast1 = ast.parse_string (prg1)

        sv = stats_visitor.StatsVisitor ()
        sv.visit (ast1)
        # UNCOMMENT to run the test
        self.assertEquals (sv.get_num_stmts (), 6)
        self.assertEquals (sv.get_num_vars (), 3)

    def test_others (self):
        prg1 = """
        {
            x := 10;
            assert x = 10;
            havoc x;
            assume x > 0
        }
        """
        ast1 = ast.parse_string (prg1)

        sv = stats_visitor.StatsVisitor ()
        sv.visit (ast1)
        # UNCOMMENT to run the test
        self.assertEquals (sv.get_num_stmts (), 4)
        self.assertEquals (sv.get_num_vars (), 1)
