names = ["John", "edy", "Jane", "Kane"]
scores = [90, 95, 80, 75]

print('{0:<10} {0:<5}'.format("Name", "Score"))

for index in range(len(names)):
    name = names[index]
    score = scores[index]
    print('{0:<10} {0:<5}'.format(name, scores))
