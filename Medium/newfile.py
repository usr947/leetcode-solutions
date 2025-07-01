class Solution(object):
    def convert(self, s, numRows):
        if numRows == 1:
            return s  # no need for break here

        rl = [""] * numRows  # create a list of strings for each row
        current_Row = 0
        going_down = False

        for i in range(len(s)):
            rl[current_Row] += s[i]  # put the character in the current row

            # If you're at top or bottom, change direction
            if current_Row == 0 or current_Row == numRows - 1:
                going_down = not going_down

            # Move pointer up or down based on direction
            if going_down:
                current_Row += 1
            else:
                current_Row -= 1

        return "".join(rl)  # combine all rows into one string
sol = Solution()
print(sol.convert("PAYPALISHIRING", 3))