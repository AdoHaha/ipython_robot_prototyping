
import unittest

import move_turtle


import math

class MoveTurtleTestCase(unittest.TestCase):
    """Tests for `move_turtle.py`."""

    def test_distance_zero(self):
        """When turtle is on the wall the distance should be zero"""
        
        
        
        
        
        
        self.assertEqual(move_turtle.measure_distance_front([0,0,0]),0)
        
        self.assertEqual(move_turtle.measure_distance_front([10,10,0]),0)
    
    def test_some_other_distances(self):
        """check if distances are all right in some non-symmetrical situations"""
        
        self.assertEqual(int(move_turtle.measure_distance_front([1,1,0])),9)
        
        self.assertEqual(int(move_turtle.measure_distance_front([9,9,-math.pi/2])),9)
    def test_pararel_distance(self):
        """When turtle is pararel to a wall, measure the distance and don't die"""
        
        self.assertEqual(int(move_turtle.measure_distance_front([5,5,0])),5)
        
    def test_single_wall_distance(self):
        """ when robot is heading towards the wall, return the distance to this wall"""
        
        self.assertEqual(int(move_turtle.measure_single_wall([5,5,0],
                                                        ([10,10],[0,-1]))[0]),5)
    
    def test_single_wall_failure(self):
        """ when robot is heading to some different wall, 
        the calculation should return false"""
        
        self.assertFalse(move_turtle.measure_single_wall([5,5,0],
                                                         ([0,0],[0,1]))[1])
    def test_single_wall_distance_zero(self):
        """when on particular wall, distance should be 0"""
        
        self.assertEqual(int(move_turtle.measure_single_wall([10,3,0],
                                                        ([10,10],[0,-1]))[0]),0)
if __name__ == '__main__':
    unittest.main()
