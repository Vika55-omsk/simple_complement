import unittest
import networkx as nx
import main
import os
class Test(unittest.TestCase):
    def testGraph(self):
        prog = main.SimpleComplement()
        prog.filename=os.path.abspath("test.net")
        prog.G=nx.read_pajek(prog.filename)
        s = prog._funcFind()
        self.assertTrue(s.number_of_nodes() is 5)
