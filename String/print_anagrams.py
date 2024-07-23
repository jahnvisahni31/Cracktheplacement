#User function Template for python3

class Solution:
    def Anagrams(self, words, n):
        '''
        words: list of word
        n:      no of words
        return : list of group of anagram {list will be sorted in driver code (not word in grp)}
        '''
        
        #code here
        d={}
        for i in words:
            w="".join(sorted(i))
            if w not in d.keys():
               d[w]=[i]
            else:
                d[w].append(i)
        return d.values()
