import random

def load_names(path):
    with open(path, encoding="utf-8") as file:
        new_list = []
        for line in file:
            name = line.strip()
            if name:
                new_list.append(name)
        return new_list

def generate_draw(names):
    if len(names) < 2:
        raise ValueError("At least 2 names are required to run a draw")
    if len(set(names)) != len(names):
        raise ValueError("Duplicate names are not allowed")

    shuffled = names.copy()
    random.shuffle(shuffled)
    shifted = shuffled[1:] + shuffled[:1]
    return dict(zip(shuffled, shifted))

if __name__ == "__main__":
    names = load_names("data.txt")
    print(generate_draw(names))



