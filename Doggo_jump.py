from typing import List
class Solution:
    def canCross(self, boxes: List[int]) -> bool:
        stages = {x: set() for x in boxes}
        stages[0] = {0}
        end = boxes[-1]
        for key in boxes:
            steps = stages[key]
            if not steps:
                return False
            if any(map(lambda step: self.__jump(stages, step, key, end), steps)):
                return True
        return False
    def __jump(self, stages, step, start, end):
        steps = (step - 1, step, step + 1)
        for s in filter(lambda x: x > 0 and start + x in stages, steps):
            stages[start + s].add(s)
            if start + s == end:
                return True
        return False
val=Solution()
lists=list(map(int,input().split()))
print(val.canCross(lists))
