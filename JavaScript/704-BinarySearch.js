var search = function(nums, target) {
    let left = 0; let right = nums.length -1; 

    while (left <= right){
        let mid = Math.floor((left + right) /2);
        const n = nums[mid];

        if (n > target){
            right = mid -1;
        }
        else if (n < target){
            left = mid +1 
        }
        else if (n == target){
            return mid;
        }
    }

    return -1;
};

/*
Space: O(1)
Time: O(log n)
*/

