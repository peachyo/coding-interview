class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        if len(sentence1) != len(sentence2):
            return False

        map = defaultdict(set)
        for pair in similarityPairs:
            map[pair[0]].add(pair[1])
            map[pair[1]].add(pair[0])
        
        for i in range(len(sentence1)):
            if sentence1[i]==sentence2[i] or sentence2[i] in map[sentence1]:
                continue
            return False
        
        return True
        