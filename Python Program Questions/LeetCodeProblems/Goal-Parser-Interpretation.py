#Question link: 1678. Goal Parser Interpretation
# https://leetcode.com/problems/goal-parser-interpretation/

class Solution:
    def interpret(self, command: str) -> str:
        return command.replace('G','G').replace('()','o').replace('(al)','al')

n=Solution()
print(n.interpret(command="G()(al)"))
