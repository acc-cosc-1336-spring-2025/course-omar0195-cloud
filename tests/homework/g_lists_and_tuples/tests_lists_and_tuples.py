import unittest

from src.homework.g_lists_and_tuples.lists import get_p_distance
from src.homework.g_lists_and_tuples.lists import get_p_distance_matrix

class Test_Config(unittest.TestCase):
    
    def test_get_p_distance(self):
        list1 = ['T','T','T','C','C','A','T','T','T','A']
        list2 = ['G','A','T','T','C','A','T','T','T','C']

    def test_get_p_distance_matrix(self):
        list1 = [
 ['T','T','T','C','C','A','T','T','T','A'],
 ['G','A','T','T','C','A','T','T','T','C'],
 ['T','T','T','C','C','A','T','T','T','T'],
 ['G','T','T','C','C','A','T','T','T','A']
]
        goal = [ 
[0.0, 0.4, 0.1, 0.1],
[0.4, 0.0, 0.4, 0.3],
[0.1, 0.4, 0.0, 0.2],
[0.1, 0.3, 0.2, 0.0]
]
        self.assertEqual(get_p_distance_matrix(list1), goal)
        

