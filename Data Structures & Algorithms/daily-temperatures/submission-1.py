class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        temps = []
        res = [0] * len(temperatures)

        for idx, temp in enumerate(temperatures):

            while temps and temp > temps[-1][0]:
                old_temp, old_idx = temps.pop()
                print(temp, idx, old_temp, old_idx)
                res[old_idx] = idx - old_idx
            temps.append((temp, idx)) 
            print(f"temps: {temps}")
        
        return res
        