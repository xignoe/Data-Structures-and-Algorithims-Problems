static int getNode(SinglyLinkedListNode head, int positionFromTail) {
        SinglyLinkedListNode node = head;
        
        for (int i = 0; head.next != null; i++) {
            head = head.next;
            
            if (i >= positionFromTail) {
                node = node.next;
            }
            
        }
        
        return node.data;
        
    }
