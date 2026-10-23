function solution(spell, dic) {
    let sortedList = []
    for (let d of dic) {
        sortedList.push(d.split("").sort().join(""))
    }
    return sortedList.includes(spell.sort().join("")) ? 1 : 2;
}