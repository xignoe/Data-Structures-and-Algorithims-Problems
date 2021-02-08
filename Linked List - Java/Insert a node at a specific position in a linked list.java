
static SinglyLinkedListNode insertNodeAtPosition(SinglyLinkedListNode head, int data, int position) {
    SinglyLinkedListNode newNode = new SinglyLinkedListNode(data);

    SinglyLinkedListNode editNode = head;
        for (int i = 0; i < position-1; i++) {
            editNode = editNode.next;
        }
            
    SinglyLinkedListNode temp = editNode.next;
    editNode.next = newNode;
    newNode.next = temp;
                
    return head;
}