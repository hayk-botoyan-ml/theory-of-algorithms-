def find_min_drops(floors: int) -> int:
    covered_floors = 0
    for drops in range(1, floors + 1):
        covered_floors += drops
        if covered_floors >= floors:
            return drops
    return floors



if __name__ == "__main__":
    floors = 100
    drops = find_min_drops(floors)

    print(f"Min drops: {drops}")
