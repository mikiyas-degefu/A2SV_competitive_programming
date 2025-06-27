# Problem: Expression Add Operators - https://leetcode.com/problems/expression-add-operators/description/

class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        result = []

        def backtrack(idx, path, val, prev_operand):
            if idx == len(num):
                if val == target:
                    result.append(path)
                return
            for i in range(idx, len(num)):
                if i != idx and num[idx] == '0':
                    break
                
                cur_str = num[idx:i+1]
                cur_num = int(cur_str)
                
                if idx == 0:
                    backtrack(i + 1, cur_str, cur_num, cur_num)
                else:
                    backtrack(i + 1, path + '+' + cur_str, val + cur_num, cur_num )
                    backtrack(i + 1, path + '-' + cur_str, val - cur_num, -cur_num )
                    backtrack(i + 1, path + '*' + cur_str, val - prev_operand + prev_operand * cur_num, prev_operand * cur_num )
        
        backtrack(0, "", 0, 0)
        return result

