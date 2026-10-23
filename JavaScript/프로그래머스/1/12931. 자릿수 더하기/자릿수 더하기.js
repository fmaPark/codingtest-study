function solution(n) {
    return String(n).split('').reduce((acc, c) => {
        return acc + Number(c)
    }, 0);
}