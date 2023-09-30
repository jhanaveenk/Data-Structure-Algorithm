class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        len_p= len(p)
        p_dict={}
        for x in p:
            p_dict[x] = p_dict.get(x, 0) + 1
        i,j=0,0
        dummy_str, ans = {}, []
        while j < len(s):
            dummy_str[s[j]] = dummy_str.get(s[j], 0) + 1
            if j-i+1 == len(p):
                if dummy_str == p_dict:
                        ans.append(i)
                dummy_str[s[i]] -=1
                if dummy_str[s[i]] == 0:
                    dummy_str.pop(s[i])
                i+=1
            j+=1
        return ans