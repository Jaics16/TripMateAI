
import sqlite3
from pathlib import Path

# Project paths
BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
DATABASE_PATH = DATA_DIR / "tripmate.db"


def get_connection():
    """Create and return a connection to the SQLite database."""
    DATA_DIR.mkdir(parents=True, exist_ok=True)

    connection = sqlite3.connect(DATABASE_PATH)
    connection.row_factory = sqlite3.Row

    return connection


def initialize_database():
    """Create database tables and insert demo records."""

    connection = get_connection()
    cursor = connection.cursor()

    # Travel packages table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS packages (
            package_id TEXT PRIMARY KEY,
            package_name TEXT NOT NULL,
            destination TEXT NOT NULL,
            duration TEXT NOT NULL,
            adult_price REAL NOT NULL,
            child_price REAL NOT NULL,
            description TEXT NOT NULL
        )
    """)

    # Sample bookings table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS bookings (
            booking_id TEXT PRIMARY KEY,
            customer_name TEXT NOT NULL,
            package_id TEXT NOT NULL,
            travel_date TEXT NOT NULL,
            guests INTEGER NOT NULL,
            booking_status TEXT NOT NULL,
            FOREIGN KEY (package_id)
                REFERENCES packages(package_id)
        )
    """)

    # Demo travel packages
    packages = [
        (
            "KV001",
            "Munnar Hills Escape",
            "Munnar",
            "5 days / 4 nights",
            18500,
            12000,
            "Explore tea plantations, misty hills, waterfalls "
            "and scenic viewpoints in Munnar."
        ),
        (
            "KV002",
            "Alleppey Backwater Break",
            "Alleppey",
            "3 days / 2 nights",
            12500,
            8500,
            "Enjoy Kerala backwaters, traditional houseboats "
            "and peaceful village scenery."
        ),
        (
            "KV003",
            "Wayanad Nature Trail",
            "Wayanad",
            "4 days / 3 nights",
            15000,
            10000,
            "Discover forests, waterfalls, viewpoints "
            "and nature attractions in Wayanad."
        )
    ]

    cursor.executemany("""
        INSERT OR IGNORE INTO packages
        (package_id, package_name, destination, duration,
         adult_price, child_price, description)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, packages)

    # Synthetic sample bookings for demonstration only
    bookings = [
        (
            "KVB1001",
            "Demo Customer",
            "KV001",
            "2026-12-18",
            2,
            "Confirmed"
        ),
        (
            "KVB1002",
            "Sample Guest",
            "KV002",
            "2026-12-22",
            3,
            "Pending"
        )
    ]

    cursor.executemany("""
        INSERT OR IGNORE INTO bookings
        (booking_id, customer_name, package_id,
         travel_date, guests, booking_status)
        VALUES (?, ?, ?, ?, ?, ?)
    """, bookings)

    connection.commit()
    connection.close()

    print("TripMateAI database initialized successfully!")


def get_all_packages():
    """Return all available package records in the demo database."""

    connection = get_connection()

    rows = connection.execute(
        "SELECT * FROM packages ORDER BY package_id"
    ).fetchall()

    connection.close()

    return [dict(row) for row in rows]


def get_package_by_id(package_id):
    """Find a package using its package ID."""

    connection = get_connection()

    row = connection.execute(
        "SELECT * FROM packages WHERE package_id = ?",
        (package_id.upper(),)
    ).fetchone()

    connection.close()

    return dict(row) if row else None


def get_booking_by_id(booking_id):
    """Find a sample booking using its booking ID."""

    connection = get_connection()

    row = connection.execute("""
        SELECT
            bookings.*,
            packages.package_name,
            packages.destination
        FROM bookings
        LEFT JOIN packages
            ON bookings.package_id = packages.package_id
        WHERE bookings.booking_id = ?
    """, (booking_id.upper(),)).fetchone()

    connection.close()

    return dict(row) if row else None


if __name__ == "__main__":
    initialize_database()

    print("\nTravel packages:")
    for package in get_all_packages():
        print(
            f"{package['package_id']} - "
            f"{package['package_name']} - "
            f"₹{package['adult_price']:,.0f} per adult"
        )

    print("\nSample booking:")
    print(get_booking_by_id("KVB1001"))
