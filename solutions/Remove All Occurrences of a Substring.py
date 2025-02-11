class Solution(object):
    def removeOccurrences(self, s, part):
        """
        :type s: str
        :type part: str
        :rtype: str
        """
        stack = []
        part_length = len(part)

        for char in s:
            stack.append(char)
            if len(stack) >= part_length and "".join(stack[-part_length:]) == part:
                for _ in range(part_length):
                    stack.pop()
        return "".join(stack)