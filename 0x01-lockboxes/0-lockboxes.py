#!/usr/bin/python3
"""
0-lockboxes
Determine if all boxes can be opened
"""

def canUnlockAll(boxes):
    """
    Determine if all boxes can be unlocked

    Args:
        boxes (list of lists): Each index represents a box and contains keys

    Returns:
        bool: True if all boxes can be opened, else False
    """
    if not boxes:
        return False

    opened = set()  # Keep track of boxes we can open
    to_visit = [0]  # Start with the first box

    while to_visit:
        current = to_visit.pop()
        if current not in opened:
            opened.add(current)
            # Add keys to boxes we haven't opened yet
            for key in boxes[current]:
                if 0 <= key < len(boxes) and key not in opened:
                    to_visit.append(key)

    return len(opened) == len(boxes)
