import unittest
import statistics

# the analyze function takes in an var arguent of numbers
# it should return a dicitonary of {'mean':0,'median':0,'mode':0,'largest':0,'smallest':0}
def analyze(*nums):
    my_mean = statistics.mean(nums)
    my_median = statistics.median(nums)
    my_mode = statistics.mode(nums)
    my_smallest = 0
    my_largest = 0
    for num in nums:
        if num < my_mean:
            my_smallest = num
        if num > my_mean:
            my_largest = num

       
    
    return {"mean": my_mean, "median": my_median, "mode": my_mode, "largest": my_largest, "smallest": my_smallest}


########################### TESTS ##############################################################
class TestMethods(unittest.TestCase):

    def test_analyze_1(self):
        data = analyze(1,2,2,2,3)
        self.assertDictEqual(data, {'mean':2,'median':2,'mode':2, 'largest':3,'smallest':1})
        

    def test_analyze_2(self):
        data = analyze(10,5,10,200,-65)
        self.assertDictEqual(data, {'mean':32,'median':10,'mode':10, 'largest':200,'smallest':-65})
        


if __name__ == '__main__':
    unittest.main()
