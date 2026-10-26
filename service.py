from draw import generate_draw
from storage import load_draws, save_draws

def get_result(category, name, names, path):
    draws = load_draws(path)

    if category not in draws:
        draws[category] = generate_draw(names)
        save_draws(path, draws)

    if name not in draws[category]:
        raise ValueError(f"Name '{name}' is not part of the '{category}' draw")

    return draws[category][name]
