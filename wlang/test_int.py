# The MIT License (MIT)
# Copyright (c) 2016 Arie Gurfinkel

# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:

# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import unittest
import wlang.ast as ast
import wlang.int

class TestInt (unittest.TestCase):
    def test_asgn_stmt (self):
        prg1 = "x := 10; print_state"
        # test parser
        ast1 = ast.parse_string (prg1)
        printed = str(ast1)
        interp = wlang.int.Interpreter ()
        st = wlang.int.State ()
        st = interp.run (ast1, st)
        self.assertIsNotNone (st)
        # x is defined
        self.assertIn ('x', st.env)
        # x is 10
        self.assertEquals (st.env['x'], 10)
        # no other variables in the state
        self.assertEquals (len (st.env), 1)

    def test_block_stmt (self):
        prog = "{x := 10; print_state}"
        # test parser
        ast1 = ast.parse_string (prog)
        printed = str(ast1)
        interp = wlang.int.Interpreter ()
        st = wlang.int.State ()
        st = interp.run (ast1, st)
        self.assertIsNotNone (st)
        # x is defined
        self.assertIn ('x', st.env)
        # x is 10
        self.assertEquals (st.env['x'], 10)
        # no other variables in the state
        self.assertEquals (len (st.env), 1)

    def test_skip_stmt (self):
        prog = "skip; print_state"
        # test parser
        ast1 = ast.parse_string (prog)
        printed = str(ast1)
        interp = wlang.int.Interpreter ()
        st = wlang.int.State ()
        st = interp.run (ast1, st)
        self.assertIsNotNone (st)
        # no other variables in the state
        self.assertEquals (len (st.env), 0)

    def test_if_stmt(self):
        prog = """
            if true or true then
                x := 10;
            if false and true then
                x := 10;
            if not true and true then
                x := 10
            else
                x := 0
        """
        # test parser
        ast1 = ast.parse_string (prog)
        printed = str(ast1)
        interp = wlang.int.Interpreter ()
        st = wlang.int.State ()
        st = interp.run (ast1, st)
        self.assertIsNotNone (st)
        # x is defined
        self.assertIn ('x', st.env)
        # x is 10
        self.assertEquals (st.env['x'], 0)
        # no other variables in the state
        self.assertEquals (len (st.env), 1)

    def test_while_stmt(self):
        prog = """
            x := 10;
            while x > 0
            do {
                x := x-1;
                print_state
            }
        """
        # test parser
        ast1 = ast.parse_string (prog)
        printed = str(ast1)
        interp = wlang.int.Interpreter ()
        st = wlang.int.State ()
        st = interp.run (ast1, st)
        self.assertIsNotNone (st)
        # x is defined
        self.assertIn ('x', st.env)
        # x is 10
        self.assertEquals (st.env['x'], 0)
        # no other variables in the state
        self.assertEquals (len (st.env), 1)

    def test_assert_stmt(self):
        prog = """
            x := 10;
            assert x = 10;
            assert x = 0
        """
        # test parser
        ast1 = ast.parse_string (prog)
        printed = str(ast1)
        interp = wlang.int.Interpreter ()
        st = wlang.int.State ()
        st = interp.run (ast1, st)
        self.assertIsNotNone (st)
        # x is defined
        self.assertIn ('x', st.env)
        # x is 10
        self.assertEquals (st.env['x'], 10)
        # no other variables in the state
        self.assertEquals (len (st.env), 1)

    def test_assume_stmt(self):
        prog = """
            x := 10;
            assume x = 10
        """
        # test parser
        ast1 = ast.parse_string (prog)
        printed = str(ast1)
        interp = wlang.int.Interpreter ()
        st = wlang.int.State ()
        st = interp.run (ast1, st)
        self.assertIsNotNone (st)
        # x is defined
        self.assertIn ('x', st.env)
        # x is 10
        self.assertEquals (st.env['x'], 10)
        # no other variables in the state
        self.assertEquals (len (st.env), 1)

    def test_havoc_stmt(self):
        prog = """
            havoc x, y;
            print_state
        """
        # test parser
        ast1 = ast.parse_string (prog)
        printed = str(ast1)
        interp = wlang.int.Interpreter ()
        st = wlang.int.State ()
        st = interp.run (ast1, st)
        self.assertIsNotNone (st)
        # x is defined
        self.assertIn ('x', st.env)
        self.assertIn ('y', st.env)
        # x is 10
        # no other variables in the state
        self.assertEquals (len (st.env), 2)

    def test_arithmetic_exp(self):
        prog = """
            x := ((5 * 2) + 5) - ((-20 / 2) + 5);
            print_state
        """
        # test parser
        ast1 = ast.parse_string (prog)
        printed = str(ast1)
        interp = wlang.int.Interpreter ()
        st = wlang.int.State ()
        st = interp.run (ast1, st)
        self.assertIsNotNone (st)
        # x is defined
        self.assertIn ('x', st.env)
        # x is 10
        self.assertEquals (st.env['x'], 20)
        # no other variables in the state
        self.assertEquals (len (st.env), 1)

    def test_cannot_be_parsed(self):
        prog = """
            xyzzxcdsvbljnew
        """
        # test parser
        ast1 = ast.parse_string (prog)
        printed = str(ast1)
        interp = wlang.int.Interpreter ()
        st = wlang.int.State ()
        st = interp.run (ast1, st)

    # def test_parse_file(self):
    #     prog = ast.parse_file("wlang/test1.prg")
    #     # test parser
    #     ast1 = ast.parse_string (prog)
    #     printed = str(ast1)
    #     interp = wlang.int.Interpreter ()
    #     st = wlang.int.State ()
    #     st = interp.run (ast1, st)
    #     self.assertIsNotNone (st)
    #     # x is defined
    #     self.assertIn ('x', st.env)
    #     # x is 10
    #     self.assertEquals (st.env['x'], 10)
    #     # no other variables in the state
    #     self.assertEquals (len (st.env), 1)
