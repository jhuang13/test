# 套路：
'''
# 查找目标：
1. 排序
2. 指针，双向指针，多重双向指针
3. hashmap
4. 二分搜索

# 链表：
1. dummy node

# 连续段落查询：
1. 滑动窗口

# 生成字符串等数据：
1. 递归

'''

#无重复字符的最长子串
from collections import (defaultdict)


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window_start = 0
        window_end = 0
        result = 0
        current_set = set()
        result_str = ''
        for i in range(len(s)):
            c = s[i]
            if c not in current_set:
                current_set.add(c)
                window_end = i
            else:
                while c in current_set:
                    current_set.remove(s[window_start])
                    window_start += 1
                current_set.add(c)

            temp = window_end - window_start + 1
            result_str = s[window_start: window_end+1]
            if temp > result:
                result=temp
        # print(result_str)
        return result

# c = Solution()
# c = c.lengthOfLongestSubstring('asdweaewcesaf')
# print(c)

#最长回文子串
class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ''
        def build_result(center_a, center_b, palindrome_count):
            res = s[
                center_a - palindrome_count:center_b + palindrome_count + 1
            ]
            return res

        length = len(s)

        for i in range(length):
            palindrome_count = 0
            left = i - 1
            right = i + 1
            while left > 0 and right < length:
                if s[left] == s[right]:
                    palindrome_count += 1
                    left -= 1
                    right += 1
                else:
                    break
            temp_res_length = 2 * palindrome_count + 1
            if temp_res_length > len(result):
                result = build_result(i , i, palindrome_count)

            if i + 1 < length and s[i] == s[i+1]:
                palindrome_count = 0
                left = i - 1
                right = i + 2
                while left > 0 and right < length:
                    if s[left] == s[right]:
                        palindrome_count += 1
                        left -= 1
                        right += 1
                    else:
                        break
                temp_res_length = 2 * palindrome_count + 2
                if temp_res_length > len(result):
                    result = build_result(i, i+1, palindrome_count)

        return result

# c = Solution()
# c = c.longestPalindrome('asdweaewcesaffas')
# print(c)

#Z 字形变换
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        result_dict = {}
        for i in range(numRows):
            result_dict[i] = ''
        block_len = numRows * 2 - 2

        for i in range(len(s)):
            pre_pos = i % block_len
            if pre_pos < numRows:
                pos = pre_pos
            else:
                pos = numRows - (pre_pos - numRows) - 2
            print(s[i], pos, pre_pos)
            result_dict[pos] += s[i]

        return ''.join(list(result_dict.values()))

# c = Solution()
# c = c.convert('PAYPALISHIRING', 4)
# print(c)

#三数之和
class Solution:
    def threeSum(self, nums) -> list:
        # three sum to be 0
        results = []
        nums =sorted(nums)
        print(nums)
        num_dict = defaultdict(int)
        for num in nums:
            num_dict[num] += 1
        length =len(nums)

        max_num = nums[length - 1]

        for i in range(length):
            # optimization
            if i > 1:
                if nums[i] == nums[i-1]:
                    continue

            # optimization
            if nums[i] > 0:
                continue

            rest = 0 - nums[i]

            # 解法1： 遍历加上集合值查询
            for j in range(i + 1, length):
                num = nums[j]

                # optimization
                if j > i + 1:
                    if num == nums[j-1]:
                        continue

                target = rest - num

                # optimization
                if target <= max_num and target in num_dict:
                    if target > num:
                        results.append([nums[i], num, target])
                    elif target == num:
                        if target != 0:
                            if num_dict[target] > 1:
                                results.append([nums[i], num, target])
                        else:
                            if num_dict[target] > 2:
                                results.append([nums[i], num, target])


            # 解法2： 双向指针
            # pointer_start = i + 1
            # pointer_end = length - 1
            # while pointer_start < pointer_end:

        return results

# c = Solution()
# c = c.threeSum([-1,0,1,2,0,-1,0,2,-4])
# print(c)

# 电话号码的字母组合
class Solution:
    phoneMap = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",
    }
    def letterCombinations(self, digits: str) -> list:
        if not digits:
            return []
        first = digits[0]
        current_digits = list(Solution.phoneMap[first])
        children_strings = self.letterCombinations(digits[1:])
        if children_strings:
            results = []

            for child in children_strings:
                for digit in current_digits:
                    results.append(digit + child)
        else:
            results = current_digits
        return results

print(Solution().letterCombinations('346'))
