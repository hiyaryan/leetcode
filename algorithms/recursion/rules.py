# Recursion

# Rules
# 1. Identify base case
# 2. Identify recursive case
# 3. Return when needed

# Usually there are two returns, one for the base case and one for the recursive case.


# Simple recursion example
def inception(counter):
    print(counter)

    if counter > 3:
        return "done"

    counter += 1
    return inception(counter)


def main():
    counter = 0

    print(inception(counter))


if __name__ == "__main__":
    main()
