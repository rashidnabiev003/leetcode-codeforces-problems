lines_count = int(input())
command_1 = ''
command_1_score = 0
command_2 = ''
command_2_score = 0


for _ in range(lines_count):
    command = input()
    if (command is not None and command_1 == '') or command == command_1:
        command_1 = command
        command_1_score += 1
    else:
        command_2 = command
        command_2_score += 1

print(command_1 if command_1_score > command_2_score else command_2)