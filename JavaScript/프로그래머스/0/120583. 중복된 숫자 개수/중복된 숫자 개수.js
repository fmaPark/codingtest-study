function solution(array, n) {
    let m = new Map()
    for (let num of array) {
        m.set(num, (m.get(num) ?? 0) + 1)
    }
    return m.get(n) ?? 0;
}