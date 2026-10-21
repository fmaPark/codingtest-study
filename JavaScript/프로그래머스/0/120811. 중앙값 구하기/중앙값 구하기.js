function solution(array) {
    const sorted = array.sort((x, y) => x - y)
    return sorted[Math.floor(array.length/2)]
}