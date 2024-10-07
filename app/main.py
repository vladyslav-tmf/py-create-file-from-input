def main() -> None:
    filename = input("Enter name of the file: ")
    full_filename = f"{filename}.txt"
    content_lines = []

    while True:
        line = input("Enter new line of content: ")
        if line.lower() == "stop":
            break
        content_lines.append(line)

    with open(full_filename, "w", encoding="utf-8") as file:
        for line in content_lines:
            file.write(line + "\n")

    print(f"File name: \"{full_filename}\"")
    print("File content:")

    for line in content_lines:
        print(line)


if __name__ == "__main__":
    main()
