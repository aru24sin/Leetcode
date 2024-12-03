class Solution(object):
    def isPrefixOfWord(self, sentence, searchWord):
        """
        :type sentence: str
        :type searchWord: str
        :rtype: int
        """
        sentence = sentence.split()
        preAmt = len(searchWord)

        for i,n in enumerate(sentence):
            if not(searchWord in n):
                continue
            elif searchWord in n:
                if n[:preAmt] == searchWord:
                    return i+1
        return -1