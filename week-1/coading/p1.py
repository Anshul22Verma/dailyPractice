# problem: 2429. Minimize XOR
# ref: https://leetcode.com/problems/minimize-xor/description/

class Solution:
    def toBinary(self, num: int):
        binary, count = "", 0
        if num != 0:
            while num >= 1:
                if num % 2 == 0:
                    binary = "0" + binary
                    num = num // 2
                elif num % 2 == 1:
                    count += 1
                    binary = "1" + binary
                    num = num // 2
        else:
            return "", 0
        return binary, count
    
    def binaryToDec(self, bnum: str):
        num = 0
        for idx in range(len(bnum)):
            num += int(bnum[len(bnum) - (idx + 1)]) * 2**idx
        return num

    def minimizeXor(self, num1: int, num2: int) -> int:
        # TC: O(bits(num1) + bits(num2))
        # SC: 
        bnum1, c1 = self.toBinary(num1)  # O(bits(num1))
        bnum2, c2 = self.toBinary(num2)  # O(bits(num2))
        
        # O(bits(num2))
        b_d = list("0" * len(bnum1))
        bits_used, idx = 0, 0
        if c1 < c2:
            b_d = list(bnum1)
            bits_used += c1
        else:
            while bits_used < c2 and idx < len(bnum1):
                if bnum1[idx] == "1":
                    b_d[idx] = "1"
                    bits_used += 1
                    idx += 1
                else:
                    idx += 1
        
        idx = 1
        while bits_used < c2 and idx < len(bnum1):
            if b_d[len(b_d) - idx] == "0":
                b_d[len(b_d) - idx] = "1"
                bits_used += 1
                idx += 1
            else:
                idx += 1
        
        while bits_used < c2:
            b_d = ["1"] + b_d
            bits_used += 1
        return self.binaryToDec("".join(b_d))
