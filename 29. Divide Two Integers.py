class Solution(object):
    def divide(self, dividend, divisor):
        if (dividend // divisor) > (2 ** 31 - 1):
            return 2 ** 31 - 1
        elif (dividend // divisor) < (-2 ** 31):
            return -2 ** 31
        else:
            if dividend >= 0 and divisor >= 0:
                return dividend // divisor
            elif dividend < 0 and divisor < 0:
                return (-dividend) // (-divisor)
            else:
                return -(abs(dividend) // abs(divisor))
