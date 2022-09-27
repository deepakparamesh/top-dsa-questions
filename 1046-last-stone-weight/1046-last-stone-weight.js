/**
 * @param {number[]} stones
 * @return {number}
 */
var lastStoneWeight = function (stones) {
    const maxHeap = getMaxHeap(stones);
    shrink(maxHeap);
    return !maxHeap.isEmpty() ? maxHeap.front().element : 0
};

const getMaxHeap = (stones) => {
    let maxHeap = new MaxPriorityQueue();
    for (const stone of stones) {
        maxHeap.enqueue(stone)
    }
    return maxHeap;
}

const shrink = (maxHeap) => {
    while (1 < maxHeap.size()) {
        const [ x, y ] = [ maxHeap.dequeue().element, maxHeap.dequeue().element ]
        const difference = x - y;
        if (difference > 0) maxHeap.enqueue(difference);
    }
}