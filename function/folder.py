from pathlib import Path


def get_pictures(path: Path) -> tuple[Path, ...]:
    picture_list: list[Path] = list()

    queue: list[Path] = [path]

    while queue:
        current_path = queue.pop(0)

        if current_path.is_dir():
            queue += list(current_path.iterdir())
        else:
            if current_path.suffix.endswith((".png", ".jpg")):
                picture_list.append(current_path)

    return tuple(picture_list)


def main():
    print(get_pictures(Path("C:\\working_data\\image_cleaner")))


if __name__ == '__main__':
    main()
