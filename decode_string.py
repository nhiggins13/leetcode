class Solution:
    def decodeString(self, s: str) -> str:

        nums = []
        strs = []
        results = ""
        curr_str = ""
        curr_num = ""

        for l in s:

            if l.isalpha():
                curr_str += l
            elif l.isdigit():
                curr_num += l
            elif l == "[":
                nums.append(int(curr_num))
                strs.append(curr_str)
                curr_num = ""
                curr_str = ""
            else:
                curr_str *= nums.pop()

                if len(strs) > 0:
                    curr_str = strs.pop() + curr_str
                else:
                    results += curr_str
                    curr_str = ""

        return results + curr_str
