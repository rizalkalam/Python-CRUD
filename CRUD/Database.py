from . import Operation

DB_NAME = "data.txt"
TEMPLATE = {
    "pk":"XXXXXX",
    "created_at":"yyyy-mm-dd",
    # "updated_at":"yyyy-mm-dd",
    "artist":255*" ",
    "album":255*" ",
    "song":255*" ",
}

def init_console():
    try:
        with open(DB_NAME, "r") as file:
            print("Database ready")
    except:
        print("Database not found")
        with open("data.txt", "w", encoding="utf-8") as file:
            Operation.create_first_data()
            