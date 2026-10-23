function solution(array) {
    // map으로 숫자, 빈도를 Key value로 세팅
    // 최빈값의 빈도를 추출
    // 그 빈도에 해당하는 키를 추출해서 리턴
    
    const m = new Map();
    for (let num of array) {
        m.set(num, (m.get(num) || 0) +1)
    }
    
    const maxCount = Math.max(...m.values())
    const maxList = []
    for (let [k, v] of m) {
        if (v === maxCount) maxList.push(k)
    }
    
    if (maxList.length !== 1) return -1;
    return maxList[0]
}