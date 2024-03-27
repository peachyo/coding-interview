class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        all = 0
        for dir, move in shift:
            if dir == 0:
                all-=move
            else:
                all+=move
        all%=len(s)
        if all>=0:
            return s[-all:]+s[:-all]
        else:
            return s[all:]+s[:all]