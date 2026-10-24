function getResult(array, command) {
    return array.slice(command[0]-1, command[1]).sort((a, b) => a-b)[command[2]-1]
}

function solution(array, commands) {
    let answer = []
    // commends 순회하며 모든 배열 자르고 연산
    for (let c of commands) {
        answer.push(getResult(array, c))
    }
    return answer;
}