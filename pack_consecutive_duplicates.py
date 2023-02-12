# Write a Python program to pack consecutive duplicates of a given list of elements in to sublists.
# original list: [0,0,1,2,3,4,4,5,6,6,6,7,8,9,4,4]
# After packing consecutive duplicates of the said list elements into sublists:
# [[0,0],[1],[2],[3],[4,4],[5],[6,6,6],[7],[8],[9],[4,4]]

data = [0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
out = [[data[0]]]
for it1, it2 in zip(data, data[1:]):
    if it1 == it2:
        out[-1].append(it2)
    else:
        out.append([it2])
print(out)
