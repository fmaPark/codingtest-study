function solution(participant, completion) {
    let m = new Map();
    for (let p of participant) {
        m.set(p, (m.get(p) ?? 0) + 1)
    }
    
    for (let c of completion) {
        m.set(c, (m.get(c) ?? 0) - 1)
    }
    
    for (let [c, v] of m) {
        if (v >= 1) {
            return c
        }
    }
}