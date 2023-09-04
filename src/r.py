def head(mat):
    header = mat.pop(0)
    sets_num = header[0]
    elements = header[1]
    return sets_num, elements

def cost(elems, lines_mat):
    cont = 0
    costs = []
    while cont < int(elems):
        i = lines_mat.pop(0)
        cont += len(i)
        costs = costs + i
    return costs

def structure(lines_mat):
    constraints = []
    indexes = []
    while len(lines_mat) != 0:
        cont = 0
        size = lines_mat.pop(0)
        const = []

        while cont < int(size[0]):
            i = lines_mat.pop(0)
            cont += len(i)
            const = const + i
        constraints.append(const)
        indexes.append(cont)
    return indexes, constraints

def read_file (file_name):
    df = open(file_name, 'r')
    lines = df.readlines()
    lines_mat = []
    for i in range(0, len(lines)):
        lines_mat.append(lines[i].split())
    sets, elems = head(lines_mat)
    costs = cost(elems, lines_mat)
    costs = [int(i) for i in costs] #str -> int

    indexes, constraints = structure(lines_mat)

    for i in range(len(constraints)):
        constraints[i] = [int(j) for j in constraints[i]]
    sets = int(sets)
    elems = int(elems)

    return sets, elems, costs, constraints