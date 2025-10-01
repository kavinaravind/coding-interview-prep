import ListNode from '../utils/list-node';

export function mergeTwoLists(list1: ListNode | null, list2: ListNode | null): ListNode | null {
  const head = new ListNode();
  let curr = head;

  while (list1 !== null && list2 !== null) {
    if (list1.val <= list2.val) {
      curr.next = list1;
      list1 = list1.next;
    } else {
      curr.next = list2;
      list2 = list2.next;
    }
    curr = curr.next;
  }

  curr.next = list1 || list2;
  return head.next;
}
