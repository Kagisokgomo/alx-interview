#!/usr/bin/python3

def canUnlockAll(boxes):
    # Set to keep track of unlocked boxes
    unlocked = set()
    unlocked.add(0)  # The first box is unlocked by default
    
    # Use a list as a stack to process boxes
    stack = [0]
    
    while stack:
        current_box = stack.pop()
        
        # Try to unlock other boxes using keys from the current box
        for key in boxes[current_box]:
            if key not in unlocked and key < len(boxes):
                unlocked.add(key)
                stack.append(key)
    
    # If all boxes are unlocked, return True
    return len(unlocked) == len(boxes)
