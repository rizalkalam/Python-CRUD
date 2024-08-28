import os
import CRUD as CRUD

if __name__ == "__main__":
    operating_system = os.name

    match operating_system:
            case "posix": os.system("clear")
            case "nt": os.system("cls")
         
    print("Welcome to the MusicDB!")
    print("=======================")

    # check the db
    CRUD.init_console()

    while(True):
        match operating_system:
            case "posix": os.system("clear")
            case "nt": os.system("cls")

        print("Welcome to the MusicDB!")
        print("=======================")

        print(f"1. Read Data")
        print(f"2. Create Data")
        print(f"3. Update Data")
        print(f"4. Delete Data\n")

        user_option = input("Choose: ")

        match user_option:
            case "1": CRUD.read_console()
            case "2": CRUD.create_console()
            case "3": CRUD.update_console()
            case "4": CRUD.delete_console()

        is_done = input("Done (y/n)?")
        if is_done == "y" or is_done == "Y":
            break

    print("Thanks")