public class Solution 
{
    public bool CanPartitionKSubsets(int[] nums, int k) 
    {
        // calculate sum needed per group
        int sum = nums.Sum();              
        if(sum % k != 0) return false;  
        int groupSum = sum / k;
        
        return CanPartitionSubset(nums, groupSum, k, index: 0, currentSum : 0);
    }
    
    private bool CanPartitionSubset(
        int[] nums,
        int sum,
        int k,
        int index,
        int currentSum)
    {
        // Single bucket remaining implies we should be able to place last one as well and don't need
        // to explicitly check for it. Implied by we have already placed rest.
        if(k == 1)
        {
            return true;
        }
        else if(currentSum == sum)
        {            
            return CanPartitionSubset(
                nums,
                sum,
                k-1,
                index: 0,
                currentSum: 0);
        }
        else
        {
            for(int i = index; i < nums.Length; i++)
            {
                if(nums[i] == -1) continue;
                
                if(currentSum + nums[i] <= sum)
                {
                    int temp = nums[i];  
                    nums[i] = -1;
                    bool bCanPartition = CanPartitionSubset(
                        nums,
                        sum, 
                        k, 
                        i+1, 
                        currentSum + temp);
                    
                    if(bCanPartition) return true;
                    if(!bCanPartition) nums[i] = temp;
                }
            }
            
            return false;
        }
    }
}