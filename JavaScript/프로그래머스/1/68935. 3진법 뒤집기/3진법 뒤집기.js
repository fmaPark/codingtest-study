function solution(n) {
    let ternary = (n).toString(3)
    return parseInt(ternary.split("").reverse().join(""), 3);
}