class Solution:
    def isPalindrome(self, x: int) -> bool:
        if (x<0 or (x%10==0 and x!=0)):
            return False
        rev=0
        while (x>rev):
            rem=x%10
            rev=rev*10+rem
            x=x//10
        if (x==rev or x==rev//10):
            return True
        else:
            return False
