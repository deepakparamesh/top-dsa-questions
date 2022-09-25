/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var reverseList = function(head) {
    let prev =  null;
    
    while(head) {
        // storing the future value in next
        let next = head.next;
        
        // Actual implementation
        head.next = prev;
        prev = head;
        
        // moving the pointer to process next;
        head = next;
    }
    
    return prev;
};