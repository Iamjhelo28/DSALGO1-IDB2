from LinkedBinaryTree import LinkedBinaryTree as Tree

# Part 1
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

# --- Equation 1: (3 * 5) - ((4 * 5) + (6 - 7)) ---
tree1 = Tree()
root1 = tree1._add_root('-')
left1 = tree1._add_left(root1, '*')
right1 = tree1._add_right(root1, '+')

tree1._add_left(left1, 3)
tree1._add_right(left1, 5)

sub_left1 = tree1._add_left(right1, '*')
sub_right1 = tree1._add_right(right1, '-')

tree1._add_left(sub_left1, 4)
tree1._add_right(sub_left1, 5)
tree1._add_left(sub_right1, 6)
tree1._add_right(sub_right1, 7)

print_traversals(tree1, "Equation 1")

# --- Equation 2: ((a + b) * c) - (d - e) ---
tree2 = Tree()
root2 = tree2._add_root('-')
left2 = tree2._add_left(root2, '*')
right2 = tree2._add_right(root2, '-')

sub_left2 = tree2._add_left(left2, '+')
tree2._add_left(sub_left2, 'a')
tree2._add_right(sub_left2, 'b')
tree2._add_right(left2, 'c')

tree2._add_left(right2, 'd')
tree2._add_right(right2, 'e')

print_traversals(tree2, "Equation 2")

# --- Equation 3: ((a ^ b) + (c + d)) + ((e * f) / (g + h)) ---
tree3 = Tree()
root3 = tree3._add_root('+')
left3 = tree3._add_left(root3, '+')
right3 = tree3._add_right(root3, '/')

sub_left3 = tree3._add_left(left3, '^')
tree3._add_left(sub_left3, 'a')
tree3._add_right(sub_left3, 'b')

sub_right3 = tree3._add_right(left3, '+')
tree3._add_left(sub_right3, 'c')
tree3._add_right(sub_right3, 'd')

sub_left_right3 = tree3._add_left(right3, '*')
tree3._add_left(sub_left_right3, 'e')
tree3._add_right(sub_left_right3, 'f')

sub_right_right3 = tree3._add_right(right3, '+')
tree3._add_left(sub_right_right3, 'g')
tree3._add_right(sub_right_right3, 'h')

print_traversals(tree3, "Equation 3")

# --- Equation 4: (a + b) / (c * (d - (e ^ f))) ---
tree4 = Tree()
root4 = tree4._add_root('/')
left4 = tree4._add_left(root4, '+')
right4 = tree4._add_right(root4, '*')

tree4._add_left(left4, 'a')
tree4._add_right(left4, 'b')

sub_right4 = tree4._add_right(right4, '-')
tree4._add_left(right4, 'c')

tree4._add_left(sub_right4, 'd')
sub_right4_right = tree4._add_right(sub_right4, '^')
tree4._add_left(sub_right4_right, 'e')
tree4._add_right(sub_right4_right, 'f')

print_traversals(tree4, "Equation 4")

# --- Equation 5: ((a - b) + c) * ((d + e) * (f / g)) ---
tree5 = Tree()
root5 = tree5._add_root('*')
left5 = tree5._add_left(root5, '+')
right5 = tree5._add_right(root5, '*')

sub_left5 = tree5._add_left(left5, '-')
tree5._add_left(sub_left5, 'a')
tree5._add_right(sub_left5, 'b')
tree5._add_right(left5, 'c')

sub_right5 = tree5._add_left(right5, '+')
tree5._add_left(sub_right5, 'd')
tree5._add_right(sub_right5, 'e')

sub_right5_right = tree5._add_right(right5, '/')
tree5._add_left(sub_right5_right, 'f')
tree5._add_right(sub_right5_right, 'g')

print_traversals(tree5, "Equation 5")

# Creating the tree for Equation 6:
# (((5 + 2) * (2 - 1)) / ((2 + 9) + ((7 - 2) - 1)) * 8)
tree7 = Tree()
root7 = tree7._add_root('*')

# Left subtree of root6 (multiplication)
left7 = tree7._add_left(root7, '/')
left7_left = tree7._add_left(left7, '*')

# Left subtree of left6_left (5 + 2)
sub_left_left = tree7._add_left(left7_left, '+')
tree7._add_left(sub_left_left, 5)
tree7._add_right(sub_left_left, 2)

# Right subtree of left6_left (2 - 1)
sub_right_left = tree7._add_right(left7_left, '-')
tree7._add_left(sub_right_left, 2)
tree7._add_right(sub_right_left, 1)

# Right subtree of left6 (addition)
right7 = tree7._add_right(left7, '+')
right7_left = tree7._add_left(right7, '+')
tree7._add_left(right7_left, 2)
tree7._add_right(right7_left, 9)

# Left subtree of right6 (7 - 2)
right7_right = tree7._add_right(right7, '-')
sub_right_right = tree7._add_left(right7_right, '-')
tree7._add_left(sub_right_right, 7)
tree7._add_right(sub_right_right, 2)

# Final multiplication and division operations
tree7._add_right(right7_right, 1)
tree7._add_right(root7, 8)

# Print the traversals
print_traversals(tree7, "Equation 6")


# Part 2


# Creating the tree for Equation 6:
# (((5 + 2) * (2 - 1)) / ((2 + 9) + ((7 - 2) - 1)) * 8)
tree6 = Tree()
root6 = tree6._add_root('*')

# Left subtree of root6 (multiplication)
left6 = tree6._add_left(root6, '/')
left6_left = tree6._add_left(left6, '*')

# Left subtree of left6_left (5 + 2)
sub_left_left = tree6._add_left(left6_left, '+')
tree6._add_left(sub_left_left, 5)
tree6._add_right(sub_left_left, 2)

# Right subtree of left6_left (2 - 1)
sub_right_left = tree6._add_right(left6_left, '-')
tree6._add_left(sub_right_left, 2)
tree6._add_right(sub_right_left, 1)

# Right subtree of left6 (addition)
right6 = tree6._add_right(left6, '+')
right6_left = tree6._add_left(right6, '+')
tree6._add_left(right6_left, 2)
tree6._add_right(right6_left, 9)

# Left subtree of right6 (7 - 2)
right6_right = tree6._add_right(right6, '-')
sub_right_right = tree6._add_left(right6_right, '-')
tree6._add_left(sub_right_right, 7)
tree6._add_right(sub_right_right, 2)

# Final multiplication and division operations
tree6._add_right(right6_right, 1)
tree6._add_right(root6, 8)

# Print the traversals
print_traversals(tree6, "Equation 6")