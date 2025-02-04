class Solution(object):
    def isIsomorphic(self, s, t):
        if len(s) != len(t):  # If lengths are different, return False
            return False

        s_map = {}  # Maps characters from s to t
        t_map = {}  # Maps characters from t to s

        for s_char, t_char in zip(s, t):  # Check each character pair
            if s_char in s_map:
                if s_map[s_char] != t_char:
                    return False
            else:
                if t_char in t_map:
                    return False
                s_map[s_char] = t_char
                t_map[t_char] = s_char

        return True  # Return True if all mappings are consistent
