class Solution:
    def parseTernary(self, expression: str) -> str:
        while len(expression) != 1:
            questionMarkIndex = len(expression) -1
            while expression[questionMarkIndex] != '?':
                questionMarkIndex -= 1
            if expression[questionMarkIndex -1] == 'T':
                value = expression[questionMarkIndex+1]
            else:
                value = expression[questionMarkIndex+3]
            expression = expression[:questionMarkIndex-1]+value \
                + expression[questionMarkIndex + 4:]
        return expression
            
            
            