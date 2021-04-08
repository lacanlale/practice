# Prompt: Describe how you could use a single array to implement three stacks
a = []
div = int(len(a)/3)
stack_1 = a[:div]
stack_2 = a[div:div*2]
stack_3 = a[div*2:]
