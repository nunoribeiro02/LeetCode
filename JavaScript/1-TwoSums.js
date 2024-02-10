var twoSum = function(nums, target) {

    let solution = [0,0];
    let len = nums.length
    let numsCopy = nums.slice();
    for (i = 0; i < len ; i++){
        let targetArr = target - nums[i];

        // Remove First element
        numsCopy.splice(0, 1);
        
        if (numsCopy.includes(targetArr)){
            solution = [i, nums.lastIndexOf(targetArr)]
            break;
        }
    }

    return solution;
}