def open_connection(db):
    print("Opening database connection...")
    db["connection"] = True


def perform_operations(db):
    if not db["connection"]:
        raise ConnectionError("Connection is not open.")
    print("Performing database operations...")


def close_connection(db):
    if db["connection"]:
        print("Closing database connection...")
        db["connection"] = None


def main():
    db = {"connection": None}

    try:
        open_connection(db)
        perform_operations(db)

    except ConnectionError as error:
        print(f"Error: {error}")

    finally:
        close_connection(db)
        print("End of the program.")


main()
