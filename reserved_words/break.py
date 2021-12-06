"""
we use 'break' when we want to stop a cycle when a condition is true
"""

for i in range(10):
    if i == 3:
        print("cycle is broke")
        break
    print(i)
