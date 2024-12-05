class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = [] #create empty list to store opening brackets
        for char in s: #loop through each element of the string
            if char in '({[': #if element is an open bracket append it to the list
                stack.append(char)
            else: #otherwise if its closing, remove the opening bracket from the list
                #if the string is not valid for following bracket rules return False
                if not stack or \
                    (char == ')' and stack[-1] != '(') or \
                    (char == '}' and stack[-1] != '{') or \
                    (char == ']' and stack[-1] != '['):
                    return False
                stack.pop()
        return not stack #if stack is empty then all opening brackets have been matched with closing bracket return True,
        # if there are some left unmatched then return False

s = Solution().isValid("()[]{}")
print(s)
s = Solution().isValid("([])")
print(s)
s = Solution().isValid("([])()")
print(s)