'''
recursive call keeps on adding coordinates which are already their.
'''
def print_matrix(matrix):
    for row in matrix:
        print(row)
    print("")

def flood_fill_util(image, stack_, color):
    moves = [(-1,1),(-1,0),(-1,-1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
    curr_c = image[stack_[-1][0]][stack_[-1][1]]

    while len(stack_)!=0:
        sr,sc = stack_.pop()
        image[sr][sc]=color        
        for move in moves:
            if (sr + move[0] >= 0) and (sc + move[1] < len(image)):
                if curr_c==image[sr + move[0]][sc + move[1]]:
                    stack_.append((sr + move[0],sc + move[1]))


def flood_fill(image, sr, sc, color):
    stack_=[(sr,sc)]
    flood_fill_util(image,stack_,color)

image = [
            [1,1,1,1,1,1],
            [1,2,2,2,2,1],
            [1,3,2,2,3,1],
            [1,2,2,4,3,1],
            [1,2,3,4,3,1],
            [1,1,1,1,1,1]
        ]
print(len(image))
print_matrix(image)
flood_fill(image,2,2,7)
print_matrix(image)