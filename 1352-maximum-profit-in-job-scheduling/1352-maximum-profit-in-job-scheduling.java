class Solution {

    class Job{
        int start;
        int end;
        int profit;

        Job(int start, int end, int profit){
            this.start = start;
            this.end = end;
            this.profit = profit;
        }
    }


    public int jobScheduling(int[] startTime, int[] endTime, int[] profit) {
        int n = startTime.length;

        if (n == 0) return 0;
        
        Job[] jobs = new Job[n];

        for(int i=0; i<n;i++){
            jobs[i] = new Job(startTime[i], endTime[i], profit[i]);
        }

        Arrays.sort(jobs, (a,b)-> a.end - b.end);

        int[] dp = new int[n];

        dp[0] = jobs[0].profit;

        for(int i = 1;i<n;i++){
            int excludeProfit = dp[i-1];

            int includeProfit = jobs[i].profit;

            int latestNonOverlapping = findLatestNonOverlapping(jobs, i);

            if(latestNonOverlapping != -1){
                includeProfit += dp[latestNonOverlapping];
            }

            dp[i] = Math.max(excludeProfit, includeProfit);
        }

        return dp[n-1];
    }

    private int findLatestNonOverlapping(Job[] jobs, int index){
        int target = jobs[index].start;
        int left = 0;
        int right = index - 1;
        int result = -1;

        while(left <= right){
            int mid = left + (right - left)/2;

            if(jobs[mid].end <= target){
                result = mid;
                left = mid+1;
            } else {
                right = mid-1;
            }
        }

        return result;
    }
}


// Time  1 2 3 4 5 6
//    0  -----
//    1    ---
//    2      ---
//    3      -----
// sort
// dp[i]
// Binary Search:

// include currentJob = profit[i] + maxProfit from jobs that end before current job starts
// exclude currentJob = maxProfil from previous job


// 1. Sort by end time: 
// 2. DP[i]: maxprofil using jobs from 0 to i
// 3. Binary Search: for each job, find the job that donn't overlap with i
// 4. dp[i] = max(dp[i-1], profit[i]+dp[lastNonOverlapping])



