function solution(array) {
    return Number(array.sort((x, y) => x - y).splice(Math.floor(array.length/2), 1));
}