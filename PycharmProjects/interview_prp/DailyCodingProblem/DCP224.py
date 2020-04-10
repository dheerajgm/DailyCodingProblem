class Solution:
    def min_postive_missed(self, list):
        res =1
        for i in list:
            if i>0:
                if i > res:
                    break
                res += i
        return res

if __name__ == '__main__':
    A = Solution()
    print(A.min_postive_missed([-3,-1,1, 2, 3, 10]))