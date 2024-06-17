import plyvel

# Change this path to the actual path where LevelDB is stored
LEVELDB_PATH = '/path/to/your/leveldb'

def fetch_values_from_leveldb(db_path):
    db = plyvel.DB(db_path, create_if_missing=False)
    values = {}
    for key, value in db:
        values[key.decode('utf-8')] = value.decode('utf-8')
    db.close()
    return values

def main():
    values = fetch_values_from_leveldb(LEVELDB_PATH)
    print("Stored values in LevelDB:")
    for key, value in values.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    main()
