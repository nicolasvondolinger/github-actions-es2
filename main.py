import unittest
from graph import count_components

class TestGraphComponents(unittest.TestCase):

    def test_original_graph(self):
        n = 5
        my_graph = {
            0: [1],
            1: [0, 2],
            2: [1],
            3: [4],
            4: [3]
        }
        self.assertEqual(count_components(n, my_graph), 2)

    def test_empty_graph(self):
        n = 0
        my_graph = {}
        self.assertEqual(count_components(n, my_graph), 0)

    def test_no_edges(self):
        n = 3
        my_graph = {
            0: [],
            1: [],
            2: []
        }
        self.assertEqual(count_components(n, my_graph), 3)

    def test_connected_graph(self):
        n = 4
        my_graph = {
            0: [1, 2, 3],
            1: [0, 2, 3],
            2: [0, 1, 3],
            3: [0, 1, 2]
        }
        self.assertEqual(count_components(n, my_graph), 1)

    def test_single_node(self):
        n = 1
        my_graph = {
            0: []
        }
        self.assertEqual(count_components(n, my_graph), 1)

    def test_multiple_components(self):
        n = 7
        my_graph = {
            0: [1],
            1: [0],
            2: [3],
            3: [2, 4],
            4: [3]
        }
        self.assertEqual(count_components(n, my_graph), 4)

if __name__ == '__main__':
    print("Iniciando execução dos testes...")
    print("---------------------------------")
    unittest.main(verbosity=2)