# Hanoi Tower
# 盘子数量
n = 3

# 初始化三根银针
hanoi_twoer = {
    "A": {
        "name": "A针",
        "disks": []
    },
    "B": {
        "name": "B针",
        "disks": []
    },
    "C": {
        "name": "C针",
        "disks": []
    }
}

A = hanoi_twoer["A"]
B = hanoi_twoer["B"]
C = hanoi_twoer["C"]

step = [0]

for i in range(1, n+1):
    A["disks"].append(i)

def log_activity(total_steps):
    if (total_steps[0] == 0):
        print("-------初始状态-------")
    else:
        print("-------第 " + str(total_steps[0]) + " 步-------")
    for i in range(0, n):
        # print tower A
        str_tower = "| "
        if (len(A["disks"]) < n - i):
            str_tower = str_tower + " "
        else:
            str_tower = str_tower + str(A["disks"][len(A["disks"]) - (n - i)])
        str_tower = str_tower + " |"
        # print tower B
        str_tower = str_tower + "| "
        if (len(B["disks"]) < n - i):
            str_tower = str_tower + " "
        else:
            str_tower = str_tower + str(B["disks"][len(B["disks"]) - (n - i)])
        str_tower = str_tower + " |"
        # print tower C
        str_tower = str_tower + "| "
        if (len(C["disks"]) < n - i):
            str_tower = str_tower + " "
        else:
            str_tower = str_tower + str(C["disks"][len(C["disks"]) - (n - i)])
        str_tower = str_tower + " |"
        print(str_tower)
    
    print("  A    B    C  ")
    print("----------------------")
    total_steps[0] = total_steps[0] + 1

log_activity(step)
def move_hanoi_tower(numDisks, source_rod, middle_rod, target_rod):
    if (numDisks == 1):
        target_rod.insert(0, source_rod.pop(0))
        log_activity(step)
    else:
        move_hanoi_tower(numDisks-1, source_rod, target_rod, middle_rod)
        target_rod.insert(0, source_rod.pop(0))
        log_activity(step)
        move_hanoi_tower(numDisks-1, middle_rod, source_rod, target_rod)

move_hanoi_tower(n, A["disks"], B["disks"], C["disks"])
