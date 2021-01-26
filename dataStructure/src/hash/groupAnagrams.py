#!/usr/bin/env  python3

import time
class Solution:
    #def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    def groupAnagrams(self, strs):
        # 由于互为字母异位词的两个字符串包含的字母相同，
        # 因此两个字符串中的相同字母出现的次数一定是相同的，
        # 故可以将每个字母出现的次数使用字符串表示，作为哈希表的键。
        hashmapnums = {}
        res = []
        for i in range(len(strs)):
            counts = [0] * 26
            for ch in strs[i]:
                counts[ord(ch) - ord("a")] += 1
                pass
            if hashmapnums.__contains__(str(counts)):
                hashmapnums[str(counts)].append(strs[i])
            else:
                hashmapnums[str(counts)] = [strs[i]]
        #print(hashmapnums.values())
        return list(hashmapnums.values())
                    

    def isAnagram(self, s1, s2):
        lens1 = len(s1)
        lens2 = len(s2)
        if lens1 != lens2:
            return False
        hashmap = {}
        for i in range(len(s1)):
            if hashmap.__contains__(s1[i]):
                hashmap[s1[i]] += 1
            else:
                hashmap[s1[i]] = 1
        for i in range(len(s2)):
            if hashmap.__contains__(s2[i]):
                if hashmap[s2[i]] > 0:
                    hashmap[s2[i]] -= 1
                else:
                    return False
            else:
                return False
        return True

def main():
    s = Solution()

    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

    timeStamp1 = time.time()
    print(s.groupAnagrams(strs))
    timeStamp2 = time.time()
    """
    print(s.containsNearbyDuplicate1(nums,k))
    timeStamp3 = time.time()
    print(s.findRestaurantForce(list1,list2))
    timeStamp4 = time.time()
    """
    print(timeStamp2-timeStamp1)
    """
    print(timeStamp3-timeStamp2)
    print(timeStamp4-timeStamp3)
    """

if __name__ == '__main__':
    main()
