data = open('C:\\Users\\emmaf\\PycharmProjects\\AOC21\\dec_3\\dec_3_data', 'r').read().split('\n')


def get_power_consumption():
    gamma_rate = ""
    epsilon_rate = ""

    for i in range(len(data[0])):

        zero_count = 0
        one_count = 0

        for number in data:
            if number[i] == "1":
                one_count += 1
            elif number[i] == "0":
                zero_count += 1

        gamma_rate += "1" if one_count > zero_count else "0"
        epsilon_rate += "1" if one_count < zero_count else "0"

    power_consumption = int(gamma_rate, 2) * int(epsilon_rate, 2)

    print("gamma rate: ", gamma_rate, ", ", int(gamma_rate, 2))
    print("epsilon rate: ", epsilon_rate, ", ", int(epsilon_rate, 2))
    print("power consumption: ", power_consumption)


def get_oxygen_generator_rating():
    gamma_rate = "000100011100"
    epsilon_rate = 0
    candidates = data.copy()

    for i in range(len(candidates[0])):

        zero_count = 0
        one_count = 0

        for number in candidates:
            if number[i] == "1":
                one_count += 1
            elif number[i] == "0":
                zero_count += 1
        if len(candidates) > 1:
            current_value = "1" if one_count >= zero_count else "0"
            remaining_numbers = [number for number in candidates if number[i] == current_value]
            candidates = remaining_numbers
    oxygen_generator_rating = candidates[0]
    return int(oxygen_generator_rating, 2)

#101011100000
def get_co2_scrubber_rating():
    candidates = data.copy()
    for i in range(len(candidates[0])):

        zero_count = 0
        one_count = 0

        for number in candidates:
            if number[i] == "1":
                one_count += 1
            elif number[i] == "0":
                zero_count += 1
        if len(candidates) > 1:
            current_value = "1" if one_count < zero_count else "0"
            remaining_numbers = [number for number in candidates if number[i] == current_value]
            candidates = remaining_numbers
    co2_scrubber_rating = candidates[0]
    return int(co2_scrubber_rating, 2)
    print(candidates)


get_power_consumption()
print(get_oxygen_generator_rating())
print(get_co2_scrubber_rating())

print("life support rating: ", get_oxygen_generator_rating() * get_co2_scrubber_rating())
