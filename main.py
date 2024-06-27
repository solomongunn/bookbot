def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    print(file_contents)
if __name__ == "__main__":
    main()

with open("books/frankenstein.txt") as file:
    text = file.read()
    print(len(text.split()))
# This is how it would look as one line: print(len((open("books/frankenstein.txt").read()).split()))
