class Solution:

    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        if n == 1:
            return nums[0]
        if k == 1:
            return max(nums)
        else:
            sum_arr = []
            max_sum = sum(nums[0:k])
            s = max_sum
            print(max_sum)
            #sum_arr.append(max_sum))
            for i in range(k, n):
                s = s - nums[i-k] + nums[i]
                print("num i:",nums[i])
                print("s",s)
                #s = sum(nums[(i-k):(i)])
                if s > max_sum:
                    max_sum = s
                #arrSum = sum_arr[i-k] - nums[i-k] + nums[i]
                #sum_arr.append(arrSum)

        #return max(sum_arr)/k
        print(max_sum)
        return float(max_sum)/float(k)