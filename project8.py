
import numpy as np

arr = None

print("\nWelcome to NumPy Analyzer")
print("1. Create Array")
print("2. Mathematical Operations")
print("3. Combine or Split")
print("4. Search, Sort, Filter")
print("5. Statistics")
print("6. Exit")

while True:

    ch = input("\nEnter choice: ")

    if ch == "1":
        print("\nSelect the type of array to create:")
        print("1. 1D Array")
        print("2. 2D Array")
        print("3. 3D Array")

        op = input("Enter your choice: ")

        if op == "1":
            n = int(input("Enter the number of elements: "))
            a = list(map(int, input("Enter elements separated by space: ").split()))

            if len(a) != n:
                print("Enter", n, "elements!")
                continue

            arr = np.array(a)

        elif op == "2":
            r = int(input("Enter the number of rows: "))
            c = int(input("Enter the number of columns: "))

            a = list(map(int, input("Enter " + str(r*c) + " elements separated by space: ").split()))

            if len(a) != r*c:
                print("Enter", r*c, "elements!")
                continue

            arr = np.array(a).reshape(r, c)

        elif op == "3":
            l = int(input("Enter the number of layers: "))
            r = int(input("Enter the number of rows: "))
            c = int(input("Enter the number of columns: "))

            a = list(map(int, input("Enter " + str(l*r*c) + " elements separated by space: ").split()))

            if len(a) != l*r*c:
                print("Enter", l*r*c, "elements!")
                continue

            arr = np.array(a).reshape(l, r, c)

        else:
            print("Invalid choice!")
            continue

        print("\nArray created successfully:")
        print(arr)

    elif ch == "2":
        if arr is None:
            print("Create array first!")
            continue

        b = list(map(int, input("Enter elements separated by space: ").split()))

        if len(b) != arr.size:
            print("Enter", arr.size, "elements!")
            continue

        b = np.array(b).reshape(arr.shape)

        print("1. Add  2. Subtract  3. Multiply  4. Divide")
        op = input("Choice: ")

        if op == "1":
            print(arr + b)
        elif op == "2":
            print(arr - b)
        elif op == "3":
            print(arr * b)
        elif op == "4":
            if np.all(b != 0):
                print(arr / b)
            else:
                print("Cannot divide by zero!")
        else:
            print("Invalid choice!")

    elif ch == "3":
        if arr is None:
            print("Create array first!")
            continue

        print("1. Combine")
        print("2. Split")
        op = input("Choice: ")

        if op == "1":
            b = list(map(int, input("Enter elements separated by space: ").split()))

            if len(b) != arr.size:
                print("Enter", arr.size, "elements!")
                continue

            b = np.array(b).reshape(arr.shape)
            result = np.concatenate((arr, b), axis=0)

            print("Combined Array:")
            print(result)

        elif op == "2":
            result = np.array_split(arr, 2, axis=0)

            print("Split Array:")
            for part in result:
                print(part)

        else:
            print("Invalid choice!")

    elif ch == "4":
        if arr is None:
            print("Create array first!")
            continue

        print("1. Search  2. Sort  3. Filter")
        op = input("Choice: ")

        if op == "1":
            print(np.where(arr == int(input("Enter value: "))))

        elif op == "2":
            print(np.sort(arr, axis=-1))

        elif op == "3":
            print(arr[arr > int(input("Enter threshold: "))])

        else:
            print("Invalid choice!")

    elif ch == "5":
        if arr is None:
            print("Create array first!")
            continue

        print("1. Sum  2. Mean  3. Median  4. Std  5. Variance")
        op = input("Choice: ")

        functions = [np.sum, np.mean, np.median, np.std, np.var]

        if op in ["1", "2", "3", "4", "5"]:
            print(functions[int(op) - 1](arr))
        else:
            print("Invalid choice!")

    elif ch == "6":
        print("Thank you! Goodbye!")
        break

    else:
        print("Invalid choice!")
