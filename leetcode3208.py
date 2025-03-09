class Solution:
    def numberOfAlternatingGroups(self, colors, k):
        groups = 0
        for idx in range(len(colors)):
            if colors[idx % len(colors)] != colors[(idx + 1) % len(colors)]:
                for i in range(k):
                    if colors[(idx + k + i) % len(colors)] == colors[(idx + k + i + 1) % len(colors)]:
                        print(f"{colors[(idx + k) % len(colors)]} == {colors[(idx + k) % len(colors)]}")
                        break
                    print(f"{colors[(idx + k) % len(colors)]} != {colors[(idx + k) % len(colors)]}")
                print("groups += 1")
                groups += 1
        return groups