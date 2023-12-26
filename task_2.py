from collections import defaultdict


def solution():
    d = defaultdict(lambda: [])
    with open("task_2_input.txt", "r", encoding="utf-8") as f:
        data = f.read().splitlines()
        data = (d.split() for d in data)
        data = [(" ".join(d[:-1]).rstrip(), int(d[-1].rstrip())) for d in data]

    for name, time in data:
        d[name].append(time)

    for name, times in d.items():
        sum_times = sum(times)
        times = " ".join(str(i) for i in times)
        print(f"{name}: {times}; sum: {sum_times}")


if __name__ == "__main__":
    solution()
