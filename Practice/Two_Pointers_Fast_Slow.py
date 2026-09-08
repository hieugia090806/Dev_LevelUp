class ListNode:
    def __init__(self, value):
        self.value = value  # Stores the data value of the node
        self.next = None   # Pointer to the next node in the list, defaults to None

def has_cycle(head):
    # If the list is empty or has only one element, a cycle cannot exist
    if not head or not head.next:
        return False
        
    slow = head  # The slow pointer (Tortoise) starts at the head
    fast = head  # The fast pointer (Hare) starts at the head
    
    # Continue traversing as long as the fast pointer doesn't reach the end of the list
    while fast and fast.next:
        slow = slow.next        # Slow pointer moves 1 step forward
        fast = fast.next.next   # Fast pointer moves 2 steps forward
        
        # If there is a cycle, the fast pointer will eventually lap the slow pointer
        if slow == fast:
            return True         # Cycle detected!
            
    # If fast pointer reaches the end (None), no cycle exists
    return False

# Test cases
if __name__ == "__main__":
    # Step 1: Create individual nodes: 1 -> 2 -> 3 -> 4
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    
    # Step 2: Link the nodes together sequentially
    node1.next = node2
    node2.next = node3
    node3.next = node4
    
    # Test 1: Check the linear list (No cycle yet)
    print(f"Does the list have a cycle? {has_cycle(node1)}")  # Output: False
    
    # Step 3: Create a cycle by pointing the tail node (4) back to an earlier node (2)
    node4.next = node2
    
    # Test 2: Check the list again (Cycle now exists)
    print(f"Does the list have a cycle? {has_cycle(node1)}")  # Output: True
