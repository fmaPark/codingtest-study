function solution(arr)
{
    var answer = [];
    let lastEle = -1
    for (let e of arr) {
        if (e !== lastEle) {
            answer.push(e)
        }
        lastEle = e
    }
    
    return answer;
}