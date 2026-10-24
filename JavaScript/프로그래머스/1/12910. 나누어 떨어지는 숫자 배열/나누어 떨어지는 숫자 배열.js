function solution(arr, divisor) {
    var answer = [];
    for (let n of arr) {
        if (n % divisor === 0) {
            answer.push(n)
        }
    }
    
    if (answer.length === 0) {
        answer.push(-1)
    }
    return answer.sort((a, b) => a-b);
}