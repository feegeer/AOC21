import re

data = open('C:\\Users\\emmaf\\PycharmProjects\\AOC21\\dec_2\\dec_2_data', 'r').read().split('\n')


def get_position_part1():
    forward_pos = 0
    depth = 0

    forward_pattern = re.compile('forward [0-9]+')
    up_pattern = re.compile("up [0-9]+")
    down_pattern = re.compile("down [0-9]+")

    for command in data:

        motion = int((command.split(' ')[1]))

        if forward_pattern.match(command):
            forward_pos += motion
        elif up_pattern.match(command):
            depth -= motion
        elif down_pattern.match(command):
            depth += motion

    print("Current forward position: ", forward_pos)
    print("Current depth: ", depth)

    return forward_pos * depth


def get_position_part2():
    forward_pos = 0
    depth = 0
    aim = 0

    forward_pattern = re.compile('forward [0-9]+')
    up_pattern = re.compile("up [0-9]+")
    down_pattern = re.compile("down [0-9]+")

    for command in data:

        motion = int((command.split(' ')[1]))

        if forward_pattern.match(command):
            forward_pos += motion
            depth += motion * aim
        elif up_pattern.match(command):
            aim -= motion
        elif down_pattern.match(command):
            aim += motion

    print("Current forward position (2): ", forward_pos)
    print("Current depth (2): ", depth)

    return forward_pos * depth


# print(get_position_part1())
print(get_position_part2())
