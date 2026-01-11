Input = open("input.txt", 'r')
Output = open("output.txt", "w")

(n, m, a) = Input.readline().split()
(n, m, a) = (int(n), int(m), int(a))

moves_made = []
for i in range(a):
    move = Input.readline().strip().split(" ")
    moves_made.append((int(move[0]), int(move[1])))

total_num_squares = n*m
current_y_coordinate = m

while len(moves_made) > 0:
    moves_made.sort()
    lowest_x_move = moves_made[0]
    new_moves_made = moves_made.copy()
    for move in moves_made:
        if move[1] >= lowest_x_move[1]:
            new_moves_made.remove(move)

    total_num_squares -= (n-lowest_x_move[0]) * (current_y_coordinate - lowest_x_move[1])
    current_y_coordinate = lowest_x_move[1] 
    moves_made = new_moves_made.copy()


Output.write(str(total_num_squares))
Input.close()
Output.close()
