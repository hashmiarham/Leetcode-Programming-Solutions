class Solution(object):
    def sortPeople(self, names, heights):
        height_dict = {}
        sorted_arr = []
        for i in range(len(names)):
            height_dict[heights[i]] = names[i]
        heights.sort()
        for j in heights:
            sorted_arr.append(height_dict[j])
        return sorted_arr[::-1]