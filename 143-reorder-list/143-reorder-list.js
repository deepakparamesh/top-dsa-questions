/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {void} Do not return anything, modify head in-place instead.
 */
var reorderList = function(head) {
    if(!head) return;
    
    // have a slow and fast pointer
    let slow=head;
    let fast=head;
    
    //Finding the midway
    while(fast && fast.next){
        slow = slow.next;
        fast = fast.next.next;
    }
    
    // reverse the second half of linked list
    let prev = null;
    let curr = slow;
    while(curr){
        let next = curr.next;
        curr.next = prev;
        prev = curr;
        curr = next;
    }
    
    // Now swap between both first and second
    let first=head;
    let second = prev;
    while(second.next){
        // storing the first
        temp = first.next;
        // swapping happens here
        first.next = second;
        // this is becoming the next
        first= temp;
        
        // storing the second head
        temp = second.next;
        second.next = first;
        second = temp;
    }
};