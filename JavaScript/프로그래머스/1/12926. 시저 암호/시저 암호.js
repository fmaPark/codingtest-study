function shift(c, n) {
    const base = (c === c.toUpperCase()) ? 65 : 97
    const idx = c.charCodeAt(0) - base
    const shifted = (idx + n) % 26
    return String.fromCharCode(shifted + base)
}

function solution(s, n) {
    var answer = '';
    for (let c of s) {
        if (c === " ") {
            answer += c
        } else {
            answer += shift(c, n)
        }
    }
    return answer;
}