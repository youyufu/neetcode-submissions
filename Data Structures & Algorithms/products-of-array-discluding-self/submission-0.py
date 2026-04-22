class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # find total product (skip 0)
        num0 = 0
        product = nums[0]
        for num in nums[1:]:
            if num == 0:
                num0 += 1
            else:
                product *= num
        # divide by nums[i] at each i
        output = []
        for i in range(len(nums)):
            if num0 == 0:
                output.append(int(product/nums[i]))
            elif num0 >= 2:
                output.append(0)
            elif nums[i] == 0: # num 0 == 1
                output.append(product)
            else:
                output.append(0)
        return output