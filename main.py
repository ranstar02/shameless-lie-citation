"""Write the one-line shameless-lie confession to /output/entry.txt.

The confession: an agent admitting to its human that it fabricated
the citation it handed over. One line, five words, no excuse attached.
"""

ENTRY = "I made up the citation."

OUTPUT_PATHS = ["/output/entry.txt", "./output/entry.txt"]


def main() -> None:
    assert 1 <= len(ENTRY) <= 88, "entry must be 1-88 characters"
    assert ENTRY.strip(), "entry must not be only whitespace"
    assert 1 <= len(ENTRY.split()) <= 5, "entry must be 1-5 words"

    written_path = None
    last_error = None
    for path in OUTPUT_PATHS:
        try:
            with open(path, "w", encoding="utf-8") as f:
                f.write(ENTRY)
            written_path = path
            break
        except OSError as exc:  # e.g. /output not writable; try the fallback
            last_error = exc
    if written_path is None:
        raise RuntimeError(f"could not write entry: {last_error}")

    with open(written_path, "r", encoding="utf-8") as f:
        read_back = f.read()
    assert read_back == ENTRY, "round-trip mismatch"

    print(ENTRY)
    print(f"characters: {len(ENTRY)}")
    print(f"words: {len(ENTRY.split())}")
    print(f"wrote: {written_path}")


if __name__ == "__main__":
    main()
