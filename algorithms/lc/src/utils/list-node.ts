/**
 * Definition for singly-linked list.
 */
export default class ListNode {
  val: number;
  next: ListNode | null;
  constructor(val?: number, next?: ListNode | null) {
    this.val = val === undefined ? 0 : val;
    this.next = next === undefined ? null : next;
  }
}

// Helper function to convert an array to a ListNode
export function arrayToList(arr: number[]): ListNode | null {
  if (arr.length === 0) {
    return null;
  }
  const head = new ListNode(arr[0]);
  let current = head;
  for (let i = 1; i < arr.length; i++) {
    current.next = new ListNode(arr[i]);
    current = current.next;
  }
  return head;
}

// Helper function to convert a ListNode to an array
export function listToArray(head: ListNode | null): number[] {
  const arr: number[] = [];
  let current = head;
  while (current !== null) {
    arr.push(current.val);
    current = current.next;
  }
  return arr;
}
