"""
Context managers allows to properly manage resources, we can specify exactly
what we want to set up  and tear down when working with certain objects
"""

"""
f = open('sampleContextManager.txt', 'w')
f.write('Lorem Ipsum is simply dummy text of the printing and typesetting '
        'industry.')
f.close()
"""

with open('sampleContextManager.txt', 'w') as f:
    f.write('Context managers allows to properly manage resources, we can specify exactly \n'
            'what we want to set up  and tear down when working with certain objects')
    f.read()


