# Name: Jhelo D. Palco
# Date: 12/06/2024
# Assignment Title: Term Project 2 Part 2

from LinkedBinaryTree import LinkedBinaryTree as Tree


def print_traversals(tree, equation_name):
    """Utility function to print traversals for a tree."""
    print(f"Preorder traversal for {equation_name}: ", end="")
    for position in tree.preorder():
        print(position.element(), end=" ")
    print()

    print(f"Inorder traversal for {equation_name}: ", end="")
    for position in tree.inorder():
        print(position.element(), end=" ")
    print()

    print(f"Postorder traversal for {equation_name}: ", end="")
    for position in tree.postorder():
        print(position.element(), end=" ")
    print("\n")


def build_tree_from_preorder_inorder(preorder, inorder):
    """
    Reconstruct a binary tree from given preorder and inorder sequences.

    Args:
    preorder (str): Preorder traversal sequence
    inorder (str): Inorder traversal sequence

    Returns:
    Tree: Reconstructed binary tree
    """
    if not preorder or not inorder:
        return None

    # Create tree and add root (first element of preorder)
    tree = Tree()
    root = tree._add_root(preorder[0])

    # Find the index of root in inorder to split left and right subtrees
    root_index = inorder.index(preorder[0])

    # Recursive helper to build subtrees
    def build_subtree(parent, pre_start, pre_end, in_start, in_end):
        if pre_start > pre_end or in_start > in_end:
            return

        # Current root is the first element in current preorder subset
        curr_root = preorder[pre_start]

        # Find index of current root in inorder to determine subtree sizes
        root_in_index = inorder.index(curr_root, in_start, in_end + 1)
        left_size = root_in_index - in_start

        # Add left subtree if exists
        if left_size > 0:
            left_child = tree._add_left(parent, preorder[pre_start + 1])
            build_subtree(
                left_child,
                pre_start + 1,
                pre_start + left_size,
                in_start,
                root_in_index - 1
            )

        # Add right subtree if exists
        if left_size < pre_end - pre_start:
            right_child = tree._add_right(parent, preorder[pre_start + left_size + 1])
            build_subtree(
                right_child,
                pre_start + left_size + 1,
                pre_end,
                root_in_index + 1,
                in_end
            )

    # Build the subtrees
    build_subtree(root, 0, len(preorder) - 1, 0, len(inorder) - 1)

    return tree


def main():
    # Equation 1
    eq1_preorder = "rabdceghf"
    eq1_inorder = "bdaeghcfr"
    eq1_tree = build_tree_from_preorder_inorder(eq1_preorder, eq1_inorder)
    print_traversals(eq1_tree, "Equation 1")

    # Equation 2
    eq2_preorder = "racdbefg"
    eq2_inorder = "cadrbefg"
    eq2_tree = build_tree_from_preorder_inorder(eq2_preorder, eq2_inorder)
    print_traversals(eq2_tree, "Equation 2")

    # Equation 3
    eq3_preorder = "racfbde"
    eq3_inorder = "afcrdbe"
    eq3_tree = build_tree_from_preorder_inorder(eq3_preorder, eq3_inorder)
    print_traversals(eq3_tree, "Equation 3")

    # Equation 4
    eq4_preorder = "racghabeif"
    eq4_inorder = "gchadriebf"
    eq4_tree = build_tree_from_preorder_inorder(eq4_preorder, eq4_inorder)
    print_traversals(eq4_tree, "Equation 4")


if __name__ == "__main__":
    main()