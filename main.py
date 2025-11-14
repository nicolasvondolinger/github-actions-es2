import unittest
from graph import count_components

class TestGraphComponents(unittest.TestCase):
    """
    Conjunto de testes para a função count_components.
    """

    def test_original_graph(self):
        """ Teste 1: Grafo original do exemplo (2 componentes) """
        n = 5
        # Grafo não direcionado
        my_graph = {
            0: [1],
            1: [0, 2],
            2: [1],
            3: [4],
            4: [3]
        }
        self.assertEqual(count_components(n, my_graph), 2)

    def test_empty_graph(self):
        """ Teste 2: Grafo vazio (n=0) """
        n = 0
        my_graph = {}
        self.assertEqual(count_components(n, my_graph), 0)

    def test_no_edges(self):
        """ Teste 3: Grafo sem arestas (n=3) """
        n = 3
        # Nós 0, 1, 2 existem, mas não têm arestas
        my_graph = {
            0: [],
            1: [],
            2: []
        }
        self.assertEqual(count_components(n, my_graph), 3)

    def test_connected_graph(self):
        """ Teste 4: Grafo totalmente conectado (n=4) """
        n = 4
        my_graph = {
            0: [1, 2, 3],
            1: [0, 2, 3],
            2: [0, 1, 3],
            3: [0, 1, 2]
        }
        self.assertEqual(count_components(n, my_graph), 1)

    def test_single_node(self):
        """ Teste 5: Grafo com um único nó (n=1) """
        n = 1
        my_graph = {
            0: []
        }
        self.assertEqual(count_components(n, my_graph), 1)

    def test_multiple_components(self):
        """ Teste 6: Grafo com múltiplos componentes (n=7) """
        n = 7
        # Componentes: {0, 1}, {2, 3, 4}, {5}, {6}
        my_graph = {
            0: [1],
            1: [0],
            2: [3],
            3: [2, 4],
            4: [3]
            # Nós 5 e 6 não têm arestas
        }
        self.assertEqual(count_components(n, my_graph), 4)

if __name__ == '__main__':
    """
    Executa os testes quando o script é chamado diretamente.
    """
    print("Iniciando execução dos testes...")
    print("---------------------------------")
    unittest.main(verbosity=2)