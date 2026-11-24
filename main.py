import os

LINE = (
    "Our standup is nine people reading their to-do lists out loud "
    "to a tenth person who is also reading a to-do list, but with "
    "more confidence."
)


def output_path():
    entry = os.environ.get("ENTRY_OUTPUT")
    if entry:
        return entry
    out_dir = os.environ.get("OUTPUT_DIR") or os.environ.get("MAKEFUN_OUTPUT_DIR")
    if out_dir:
        return os.path.join(out_dir, "entry.txt")
    return "/output/entry.txt"


def main():
    if not LINE.strip() or len(LINE) > 200:
        raise ValueError("entry line must be 1-200 non-blank characters")
    path = output_path()
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(LINE + "\n")
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
