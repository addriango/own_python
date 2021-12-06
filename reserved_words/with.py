"""
we use 'with' keyword when we want to manage a text file
or make a request to network. It is useful because close
automaticly file or conection, even tough a exception is raised.
It avoid unexpected behaviors in the request or file.
"""
# 1) without using with statement

file = open('/root/git/python/reserved_words/test.txt', 'w')

file.write('hello world !')

file.close()

# 2) using with statement

# with open('/root/git/python/reserved_words/test.txt', 'w') as file:

#     file.write('hello using with ! \n')
