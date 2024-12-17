def tower_of_hanoi(n, source, target, auxiliary):
    """
    Solve the Tower of Hanoi problem and print each move.

    Parameters:
    n (int): Number of disks to move.
    source (str): The name of the source peg.
    target (str): The name of the target peg.
    auxiliary (str): The name of the auxiliary peg.
    """
    if n == 1:  # Base case: only one disk to move
        print(f"Move disk 1 from {source} to {target}")
        return

    # Move n-1 disks from source to auxiliary using target as buffer
    tower_of_hanoi(n - 1, source, auxiliary, target)

    # Move the nth disk from source to target
    print(f"Move disk {n} from {source} to {target}")

    # Move the n-1 disks from auxiliary to target using source as buffer
    tower_of_hanoi(n - 1, auxiliary, target, source)


def main():
    """Entry point of the program."""
    num_disks = int(input("Enter the number of disks: "))
    print(f"\nSolving Tower of Hanoi for {num_disks} disks:\n")
    tower_of_hanoi(num_disks, 'A', 'C', 'B')  # A is source, C is target, B is auxiliary


if __name__ == "__main__":
    main()
