class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Stack to keep track of opening brackets
        stack = []
        
        # Mapping of closing to opening brackets
        bracket_map = {')': '(', '}': '{', ']': '['}
        
        # Iterate through each character in the string
        for char in s:
            if char in bracket_map:
                # Pop the top element from the stack if it's not empty, else assign a dummy value
                top_element = stack.pop() if stack else '#'
                
                # Check if the mapping for the closing bracket matches the top element of the stack
                if bracket_map[char] != top_element:
                    return False
            else:
                # It's an opening bracket, so push it onto the stack
                stack.append(char)
        
        # If the stack is empty, it means all brackets were matched correctly
        return not stack

# Example usage
solution = Solution()
print(solution.isValid("()"))         # Output: True
print(solution.isValid("()[]{}"))     # Output: True
print(solution.isValid("(]"))         # Output: False




    



  

