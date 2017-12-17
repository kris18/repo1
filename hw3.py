# Sample program - Hello World (for loop, build-in enumerate function, new style pythonic formatting!

tags=['World', 'Earch', 'Mars', 'Sun', 'Milky Way']

for i, tag in enumerate(tags):
    print ("Hello {name} \t [iteration: {iter}]".format(iter=i, name=tag))
