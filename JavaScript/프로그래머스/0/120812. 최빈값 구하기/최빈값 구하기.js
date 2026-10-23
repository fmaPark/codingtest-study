function solution(array) {
    const counter = new Map();

    for (const num of array) {
        counter.set(num, (counter.get(num) ?? 0) + 1)
    }
    
    const counts = [...counter.values()];
    const maxCount = Math.max(...counts);
    
    let numlist = []
    for (const [num, cnt] of counter) {
        if (cnt === maxCount) {
            numlist.push(num)
        }
    }
    
    if (numlist.length !== 1) {
        return -1
    } else {
        return numlist[0]
    }
    
}