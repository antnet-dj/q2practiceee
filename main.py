from pyscript import document, display


# num = {-1, 1, 1.5}

# week = {'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'}
# display('monday' in week, target="output1")


# A = {1, 2, 3}
# B = {3, 4, 5}

# # display(A|B, target="output1") #union
# # display(A&B, target="output1")
# display(B-A, target="output1") #difference
# display(A^B, target="output1") #symmetric difference

# ADDING: NOT UNIQUE
# UNION: UNIQUE

# A = {'burger', 'fries'}
# B = {'burger', 'fries', 'coke', 'pie'}

# display(A<=B, target="output1") #subset
# display(A<B, target="output1") #proper subset
# display(B<A, target="output1") #proper subset
# display(A>=B, target="output1") #superset
# display(B>A, target="output1") #proper superset

X = {'MATH 98', 'FIL97', 'ENG 94'}
Y = {'MATH98', 'FIL97', 'ENG94', 'CAT99'}

display(X.issuperset(Y), target="output1")