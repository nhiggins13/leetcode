from house_robber import rob


def rob_circular(house_list):
    if len(house_list) ==1:
        return house_list[0]

    return max(rob(house_list[0:-1]), rob(house_list[1:]))