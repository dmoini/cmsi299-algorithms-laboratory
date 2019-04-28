import sys
import heapq


def check_order(jaguars):
    wrong_pos = 0
    for i in range(num_jaguars):
        if (i + 1 != jaguars[i]):
            wrong_pos += 1
    return wrong_pos

def reorder_jaguars(jaguars, king_pos, index_diff, queue, level, seen_orders):
    if (king_pos - 1 + index_diff >= 0 and king_pos - 1 + index_diff < num_jaguars):
        new_jaguars = jaguars.copy()
        new_jaguars[king_pos - 1] = new_jaguars[king_pos - 1 + index_diff]
        new_jaguars[king_pos - 1 + index_diff] = 1
        if (new_jaguars not in seen_orders):
            seen_orders.append(new_jaguars)
            heapq.heappush(queue, ((check_order(new_jaguars) + level + 1), new_jaguars, level + 1))

def expand_node(jaguars, queue, level, seen_orders):
    king_pos = jaguars.index(1) + 1
    reorder_jaguars(jaguars, king_pos, 4, queue, level, seen_orders)
    reorder_jaguars(jaguars, king_pos, -4, queue, level, seen_orders)
    if (king_pos % 4 == 0):
        reorder_jaguars(jaguars, king_pos, -3, queue, level, seen_orders)
    else:
        reorder_jaguars(jaguars, king_pos, 1, queue, level, seen_orders)

    if (king_pos % 4 == 1):
        reorder_jaguars(jaguars, king_pos, 3, queue, level, seen_orders)
    else:
        reorder_jaguars(jaguars, king_pos, -1, queue, level, seen_orders)


num_jaguars = int(sys.stdin.readline())
case = 1

while (num_jaguars != 0):
    jaguars = list(map(int, sys.stdin.readline().strip().split()))
    cutoff_level = -1
    order_found = False

    while (not order_found):
        cutoff_level += 1
        print("cutoff level is " + str(cutoff_level))

        queue = []
        seen_orders = []
        heapq.heappush(queue, (check_order(jaguars), jaguars, 0))
        seen_orders.append(jaguars)
        # node stores tuple: [heurestic, jaguar order, level]

        while queue:
            # print("Seen orders is " + str(seen_orders))
            # print("The queue is " + str(queue))
            node = heapq.heappop(queue)
            if node[2] == cutoff_level:
                if check_order(node[1]) == 0:
                    order_found = True
                    break
            else:
                expand_node(node[1], queue, node[2], seen_orders)

    print("Set {}:\n{}".format(case, cutoff_level))
    case += 1

    num_jaguars = int(sys.stdin.readline())