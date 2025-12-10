class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def max_level_sum(root):
    """
    Returns (level_index, level_sum) for the level
    with the maximum sum. If multiple levels tie,
    return the one with the smallest index.
    For empty tree, return (None, 0).
    """
    if root is None:
        return (None, 0)

    from collections import deque

    queue = deque([root])
    level = 0
    best_level = 0
    best_sum = root.value  # level 0 sum

    while queue:
        level_size = len(queue)
        current_sum = 0

        for _ in range(level_size):
            node = queue.popleft()
            current_sum += node.value

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        # Check if this level beats the current best
        if current_sum > best_sum:
            best_sum = current_sum
            best_level = level

        level += 1

    return best_level, best_sum