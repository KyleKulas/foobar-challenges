def solution(times, time_limit):
    """
    [
    [0, 2, 2, 2, -1],  # 0 = Start
    [9, 0, 2, 2, -1],  # 1 = Bunny 0
    [9, 3, 0, 2, -1],  # 2 = Bunny 1
    [9, 3, 2, 0, -1],  # 3 = Bunny 2
    [9, 3, 2, 2,  0],  # 4 = Bulkhead
    ]
    """
    move_limit = 6

    def recurse(times, position, time, bunnies, bunnies_to_collect, move_count):

        # print(position, time, bunnies, move_count)
        if position == len(times) - 1 and bunnies_to_collect == len(bunnies) and time >= 0:
            return bunnies
        elif move_count == move_limit:
            return None
        else:
            
            for index, move in enumerate(times[position]):
                if not index == position:
                    if position > 0 and position < len(times) - 1:
                        bunnies.add(position - 1)
                    bunny_copy = bunnies.copy()
                    
                    answer = recurse(times, index, time - move, bunny_copy, bunnies_to_collect, move_count + 1)
                    if answer:
                            return answer
            return None               

  
    for bunnies_to_collect in range(len(times) - 2, 0, -1):
        # print("bunnies_to_collect", bunnies_to_collect)
        answer = recurse(times, 0, time_limit, set(), bunnies_to_collect, 0)
        if answer:
            return list(answer)
    return []

print(solution([[0, 2, 2, 2, -1], [9, 0, 2, 2, -1], [9, 3, 0, 2, -1], [9, 3, 2, 0, -1], [9, 3, 2, 2, 0]], 1))