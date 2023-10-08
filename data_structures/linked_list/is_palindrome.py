from dataclasses import dataclass
from typing import Optional


@dataclass
class ListNode:
    val: int = 0
    next_node: Optional["ListNode"] = None


def is_palindrome(head: ListNode) -> bool:
    """
    Check if a linked list is a palindrome.

    Args:
        head: The head of the linked list.

    Returns:
        bool: True if the linked list is a palindrome, False otherwise.

    Examples:
        >>> is_palindrome(None)
        True

        >>> is_palindrome(ListNode(1))
        True

        >>> is_palindrome(ListNode(1, ListNode(2)))
        False

        >>> is_palindrome(ListNode(1, ListNode(2, ListNode(1))))
        True

        >>> is_palindrome(ListNode(1, ListNode(2, ListNode(2, ListNode(1)))))
        True
    """
    if not head:
        return True
    # split the list to two parts
    fast, slow = head.next_node, head
    while fast and fast.next_node:
        fast = fast.next_node.next_node
        slow = slow.next_node
    second = slow.next_node
    slow.next_node = None  # Don't forget here! But forget still works!
    # reverse the second part
    node = None
    while second:
        nxt = second.next_node
        second.next_node = node
        node = second
        second = nxt
    # compare two parts
    # second part has the same or one less node
    while node:
        if node.val != head.val:
            return False
        node = node.next_node
        head = head.next_node
    return True


def is_palindrome_stack(head: ListNode) -> bool:
    """
    Check if a linked list is a palindrome using a stack.

    Args:
        head (ListNode): The head of the linked list.

    Returns:
        bool: True if the linked list is a palindrome, False otherwise.

    Examples:
        >>> is_palindrome_stack(None)
        True

        >>> is_palindrome_stack(ListNode(1))
        True

        >>> is_palindrome_stack(ListNode(1, ListNode(2)))
        False

        >>> is_palindrome_stack(ListNode(1, ListNode(2, ListNode(1))))
        True

        >>> is_palindrome_stack(ListNode(1, ListNode(2, ListNode(2, ListNode(1)))))
        True
    """
    if not head or not head.next_node:
        return True

    # 1. Get the midpoint (slow)
    slow = fast = cur = head
    while fast and fast.next_node:
        fast, slow = fast.next_node.next_node, slow.next_node

    # 2. Push the second half into the stack
    stack = [slow.val]
    while slow.next_node:
        slow = slow.next_node
        stack.append(slow.val)

    # 3. Comparison
    while stack:
        if stack.pop() != cur.val:
            return False
        cur = cur.next_node

    return True


def is_palindrome_dict(head: ListNode) -> bool:
    """
    Check if a linked list is a palindrome using a dictionary.

    Args:
        head (ListNode): The head of the linked list.

    Returns:
        bool: True if the linked list is a palindrome, False otherwise.

    Examples:
        >>> is_palindrome_dict(None)
        True

        >>> is_palindrome_dict(ListNode(1))
        True

        >>> is_palindrome_dict(ListNode(1, ListNode(2)))
        False

        >>> is_palindrome_dict(ListNode(1, ListNode(2, ListNode(1))))
        True

        >>> is_palindrome_dict(ListNode(1, ListNode(2, ListNode(2, ListNode(1)))))
        True

        >>> is_palindrome_dict(\
            ListNode(\
                1, ListNode(2, ListNode(1, ListNode(3, ListNode(2, ListNode(1)))))))
        False
    """
    if not head or not head.next_node:
        return True
    d = {}
    pos = 0
    while head:
        if head.val in d:
            d[head.val].append(pos)
        else:
            d[head.val] = [pos]
        head = head.next_node
        pos += 1
    checksum = pos - 1
    middle = 0
    for v in d.values():
        if len(v) % 2 != 0:
            middle += 1
        else:
            step = 0
            for i in range(len(v)):
                if v[i] + v[len(v) - 1 - step] != checksum:
                    return False
                step += 1
        if middle > 1:
            return False
    return True


if __name__ == "__main__":
    import doctest

    doctest.testmod()
