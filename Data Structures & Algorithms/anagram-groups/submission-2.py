class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def hashFunction(value: str) -> int:
            freq = [0]*26
            ord_a = ord("a")
            hash_value = 0
            for s in value:
                freq[ord(s)-ord_a]+=1
            return hash(tuple(freq))

        hash_map = {}

        for string in strs:
            hash_value = hashFunction(string)
            if hash_map.get(hash_value) != None:
                hash_map[hash_value].append(string)
            else:
                hash_map[hash_value] = [string]
        return list(hash_map.values())