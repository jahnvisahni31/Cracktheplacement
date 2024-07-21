class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        su = sum(cost)
        su_g = sum(gas)
        if su > su_g:
            return -1
        c = 0
        s = 0
        for i in range(len(gas)):
            c += gas[i] - cost[i]
            if c < 0:
                c = 0
                s = i+1
        return s
