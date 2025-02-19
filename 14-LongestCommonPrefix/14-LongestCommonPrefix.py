class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""  # If list is empty, return empty string
    
        prefix = strs[0]  # Start with the first string as the prefix
    
        for s in strs[1:]:
            while not s.startswith(prefix):
                prefix = prefix[:-1]  # Reduce the prefix character by character
                if not prefix:
                    return ""  # If prefix becomes empty, return ""

        return prefix
        