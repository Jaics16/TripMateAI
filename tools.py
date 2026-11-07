
from database import (
    get_all_packages,
    get_package_by_id,
    get_booking_by_id
)


def list_packages():
    """List all travel packages stored in the database."""

    packages = get_all_packages()

    if not packages:
        return {"success": False, "message": "No packages found."}

    return {
        "success": True,
        "packages": packages
    }


def get_package_details(package_id: str):
    """Get complete details of a travel package."""

    package = get_package_by_id(package_id)

    if not package:
        return {
            "success": False,
            "message": f"No package found with ID {package_id}."
        }

    return {
        "success": True,
        "package": package
    }


def calculate_package_price(
    package_id: str,
    adults: int,
    children: int
):
    """Calculate the total package price."""

    if adults < 0 or children < 0:
        return {
            "success": False,
            "message": "Guest numbers cannot be negative."
        }

    if adults + children <= 0:
        return {
            "success": False,
            "message": "At least one guest is required."
        }

    package = get_package_by_id(package_id)

    if not package:
        return {
            "success": False,
            "message": f"No package found with ID {package_id}."
        }

    adult_price = package["adult_price"]
    child_price = package["child_price"]

    adult_total = adults * adult_price
    child_total = children * child_price
    total = adult_total + child_total

    return {
        "success": True,
        "package_name": package["package_name"],
        "destination": package["destination"],
        "adults": adults,
        "children": children,
        "adult_price": adult_price,
        "child_price": child_price,
        "adult_total": adult_total,
        "child_total": child_total,
        "total_price": total,
        "currency": "INR"
    }


def lookup_booking(booking_id: str):
    """Look up a synthetic demonstration booking."""

    booking = get_booking_by_id(booking_id)

    if not booking:
        return {
            "success": False,
            "message": "No sample booking found with that ID."
        }

    return {
        "success": True,
        "booking": booking,
        "notice": "This is a synthetic demonstration booking."
    }


def run_tool(tool_name: str, arguments: dict):
    """Execute a tool requested by the AI assistant."""

    available_tools = {
        "list_packages": list_packages,
        "get_package_details": get_package_details,
        "calculate_package_price": calculate_package_price,
        "lookup_booking": lookup_booking
    }

    function = available_tools.get(tool_name)

    if not function:
        return {
            "success": False,
            "message": f"Unknown tool: {tool_name}"
        }

    try:
        return function(**arguments)

    except TypeError:
        return {
            "success": False,
            "message": "Invalid arguments supplied to the tool."
        }

    except Exception as error:
        return {
            "success": False,
            "message": f"Tool execution failed: {str(error)}"
        }


if __name__ == "__main__":

    print("\n========== TRIPMATE AI TOOL TESTING ==========\n")

    print("1. LIST PACKAGES")
    print(list_packages())

    print("\n2. PACKAGE DETAILS")
    print(get_package_details("KV001"))

    print("\n3. PRICE CALCULATION")
    print(calculate_package_price("KV001", 2, 1))

    print("\n4. BOOKING LOOKUP")
    print(lookup_booking("KVB1001"))

    print("\n5. UNKNOWN BOOKING")
    print(lookup_booking("INVALID123"))

    print("\n========== TESTING COMPLETED ==========")
