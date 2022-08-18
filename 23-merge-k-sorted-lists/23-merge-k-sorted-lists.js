/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode[]} lists
 * @return {ListNode}
 */
var merge = function (l1, l2) {
    let tempNode = new ListNode(0);
    let current = tempNode;

    while (l1 && l2) {
        if (l1.val < l2.val) {
            current.next = l1;
            l1 = l1.next;
        } else {
            current.next = l2;
            l2 = l2.next;
        }
        current = current.next;
    }
    if (l1) current.next = l1;
    if (l2) current.next = l2;

    return tempNode.next;
};

var mergeKLists = function (lists) {
    let root = lists[0];

    for (let i = 1; i < lists.length; i++) {
        root = merge(root, lists[i]);
    }
    return root || null;
};

// [1,4,5],[1,3,4],[2,6],[0,7]

// [1,4,5],[1,3,4] => [1,3,4,4,5][2,6] => [1,2,3,4,4,5,6]

// By using the merge sort strategy
// []

// O(n log(k))
// O

// Time -> O(k*n) 
// Space -> O(k) // check about the time complexity.

