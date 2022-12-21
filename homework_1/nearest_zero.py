def nearest_zero(array):
    distance = [0] * len(array)
    distance_zero = float('inf')
    for k, value in enumerate(array):
        if value == 0:
            distance[k] = 0
            distance_zero = 0
            for i in range(k, 0-1, -1):
                if distance_zero <= distance[i]:
                    distance[i] = distance_zero
                    distance_zero += 1
                else:
                    break
            distance_zero = 0
        else:
            distance_zero += 1
            distance[k] = distance_zero
    return distance

if __name__ == "__main__":
    street = [int(house) for house in input().split()]

    print(*nearest_zero(street))
