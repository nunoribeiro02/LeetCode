/**
 * @param {string} str
 * @return {string}
 */
var maximumOddBinaryNumber = function(str) {
    let ones = false;
    let res = "";
    let add = 0;
    for (let c of str){
        if (c == '1' && !ones){
            res = res + c;
            ones = true
        }
        else if (c == '1'){
            add++;
        }
        else if (c == '0'){
            res = c + res;
        }
    }

    // Finish adding 1's in the beginning
    while (add > 0){
        add--;
        res = '1' + res;
    }

    return res;
};

/*
Space: O(1);
Time: O(n^2);
*/