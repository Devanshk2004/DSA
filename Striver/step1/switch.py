class Solution:
    def whichWeekDay(self, day):
        day_dict = {
            1: "Monday",
            2: "Tuesday",
            3: "Wednesday",
            4: "Thursday",
            5: "Friday",
            6: "Saturday",
            7: "Sunday"
        }
        return day_dict.get(day, "Invalid Error")

sol = Solution()
day = int(input())
print(sol.whichWeekDay(day))