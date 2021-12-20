data = open('dec_1\\Dec_1_data', 'r').read().split('\n')


def count_increased():
    inc_counter = 0

    for i in range(len(data) - 1):
        if int(data[i + 1]) > int(data[i]):
            inc_counter += 1
    return inc_counter


def count_increased_triples():
    triple_counter = 0
    prev_triple = 0

    for i in range(len(data) - 2):
        triple_sum = int(data[i]) + int(data[i + 1]) + int(data[i + 2])
        if int(triple_sum) > prev_triple and i != 0:
            triple_counter += 1
        prev_triple = triple_sum
    return triple_counter


print("increased: ", count_increased())
print("increased (triples): ", count_increased_triples())
