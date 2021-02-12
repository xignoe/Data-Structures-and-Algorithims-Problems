static SinglyLinkedListNode removeDuplicates(SinglyLinkedListNode head) {

    if (head == null || head.next == null) {
        return head;
    } else if (head.data == head.next.data) {
        head = removeDuplicates(head.next);
    } else {
        head.next = removeDuplicates(head.next);
    } return head;

}