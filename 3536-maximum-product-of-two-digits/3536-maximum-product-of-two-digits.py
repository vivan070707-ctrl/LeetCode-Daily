class Solution:
    def maxProduct(self, n: int) -> int:
        largest = 0
        second_largest = 0
        
        while n > 0:
            n, digit = divmod(n, 10)
            
            if digit > largest:
                second_largest = largest
                largest = digit
            elif digit > second_largest:
                second_largest = digit
                
        return largest * second_largest

        