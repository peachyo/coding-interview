class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        row=defaultdict(list)
        col=defaultdict(list)

        m = len(picture)
        n=len(picture[0])
        for i in range(m):
            count = 0
            for j in range(n):
                if picture[i][j]=='B':
                    row[i].append(j)
                    col[j].append(i)
                    
        count=0
        for r, c in row.items():
            if len(c)>1:
                continue
            if c[0] in col and len(col[c[0]])==1:
                count+=1
        return count