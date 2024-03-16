"""
692. Top K Frequent Words

Given an array of strings words and an integer k, return the k most frequent strings.

Return the answer sorted by the frequency from highest to lowest.
Sort the words with the same frequency by their lexicographical order.
"""
class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        if len(words) == 0:
            return None
        if k ==0:
            return None

        words_dict = {}
        freq_set = set()
        words_dict_extended = {}
        result = []

        for w in words:
            if w in words_dict:
                words_dict[w] += 1
            else:
                words_dict[w] = 1

        for word, freq in words_dict.items():

            if freq in words_dict_extended:
                words_dict_extended[freq].append(word)
            else:
                words_dict_extended[freq] = [word]

        print(words_dict_extended)
        count = 0
        for i in sorted(words_dict_extended, reverse=True):
            print(i)
            for w in sorted(words_dict_extended[i]):
                print(w)
                result.append(w)
                count +=1
                if count >= k:
                    break

            if count >= k:
                break
        return result


if __name__ == '__main__':

    s= Solution()

    words = ["the","day","is","sunny","the","the","the","sunny","is","is"]
    k = 4

    print(s.topKFrequent(words, k))