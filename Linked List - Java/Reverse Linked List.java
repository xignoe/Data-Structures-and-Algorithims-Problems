static SinglyLinkedListNode reverse(SinglyLinkedListNode head) {
        if (head == null) {
            return head;
        }
            

        SinglyLinkedListNode current = null;
        SinglyLinkedListNode previous = null;

        while(head != null) {
            previous = current;
            current = head;
            head = head.next;
            current.next = previous;
        }

        return current;

}
