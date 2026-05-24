# UPDATE PROPERTY
from db import connect_db

def add_property():
    print("Add Property Function Running")

def view_properties():
    from db import connect_db

    conn = connect_db()
    cursor = conn.cursor()

    query = "SELECT * FROM properties"

    cursor.execute(query)

    properties = cursor.fetchall()

    print("\n--- PROPERTY LIST ---")

    for property in properties:
        print(f"""
Property ID : {property[0]}
property tittle: {property[1]}
property type : {property[2]}
Location    : {property[3]}
Price       : {property[4]}
Owner name : {property[5]}
Status      : {property[6]}
-----------------------------
""")

    conn.close()    


def update_property():

    conn = connect_db()
    cursor = conn.cursor()

    property_id = int(input("Enter Property ID to update: "))
    new_price = int(input("Enter new price: "))

    query = """
    UPDATE properties
    SET price = %s
    WHERE property_id = %s
    """

    values = (new_price, property_id)

    cursor.execute(query, values)

    conn.commit()

    print("✅ Property Updated Successfully!")

    conn.close()


# DELETE PROPERTY
def delete_property():

    conn = connect_db()
    cursor = conn.cursor()

    property_id = int(input("Enter Property ID to delete: "))

    query = "DELETE FROM properties WHERE property_id = %s"

    cursor.execute(query, (property_id,))

    conn.commit()

    print("✅ Property Deleted Successfully!")

    conn.close()
    # SEARCH PROPERTY
def search_property():

    conn = connect_db()

    cursor = conn.cursor()

    print("\nSearch Property By:")
    print("1. Location")
    print("2. Property Type")
    print("3. Price Below")

    choice = input("Enter choice: ")

    # SEARCH BY LOCATION
    if choice == "1":

        location = input("Enter Location: ")

        query = """
        SELECT * FROM properties
        WHERE location = %s
        """

        cursor.execute(query, (location,))

    # SEARCH BY TYPE
    elif choice == "2":

        ptype = input("Enter Property Type (Rent/Sale): ")

        query = """
        SELECT * FROM properties
        WHERE property_type = %s
        """

        cursor.execute(query, (ptype,))

    # SEARCH BY PRICE
    elif choice == "3":

        price = int(input("Enter Maximum Price: "))

        query = """
        SELECT * FROM properties
        WHERE price <= %s
        """

        cursor.execute(query, (price,))

    else:

        print("Invalid Choice")
        return

    rows = cursor.fetchall()

    print("\n===== SEARCH RESULTS =====")

    for row in rows:

        print("\n--------------------------------")

        print("Property ID :", row[0])
        print("Name        :", row[1])
        print("Type        :", row[2])
        print("Location    :", row[3])
        print("Price       :", row[4])
        print("Owner       :", row[5])
        print("Status      :", row[6])

        print("--------------------------------")

    conn.close()

# BOOK PROPERTY
def book_property():

    conn = connect_db()

    cursor = conn.cursor()

    customer_name = input("Enter Customer Name: ")

    property_id = int(input("Enter Property ID to Book: "))

    # CHECK PROPERTY STATUS
    query = """
    SELECT status FROM properties
    WHERE property_id = %s
    """

    cursor.execute(query, (property_id,))

    result = cursor.fetchone()

    # PROPERTY NOT FOUND
    if not result:

        print("\n❌ Property Not Found!")

        conn.close()

        return

    # PROPERTY ALREADY BOOKED
    if result[0].lower() != "available":

        print("\n❌ Property Not Available!")

        conn.close()

        return

    # INSERT BOOKING
    booking_query = """
    INSERT INTO bookings (customer_name, property_id)
    VALUES (%s, %s)
    """

    cursor.execute(booking_query, (customer_name, property_id))

    # UPDATE PROPERTY STATUS
    update_query = """
    UPDATE properties
    SET status = 'Booked'
    WHERE property_id = %s
    """

    cursor.execute(update_query, (property_id,))

    conn.commit()

    print("\n✅ Property Booked Successfully!")

    conn.close()  

    # CANCEL BOOKING
def cancel_booking():

    conn = connect_db()

    cursor = conn.cursor()

    booking_id = int(input("Enter Booking ID to Cancel: "))

    # GET PROPERTY ID
    query = """
    SELECT property_id FROM bookings
    WHERE booking_id = %s
    """

    cursor.execute(query, (booking_id,))

    result = cursor.fetchone()

    # BOOKING NOT FOUND
    if not result:

        print("\n❌ Booking Not Found!")

        conn.close()

        return

    property_id = result[0]

    # DELETE BOOKING
    delete_query = """
    DELETE FROM bookings
    WHERE booking_id = %s
    """

    cursor.execute(delete_query, (booking_id,))

    # UPDATE PROPERTY STATUS
    update_query = """
    UPDATE properties
    SET status = 'Available'
    WHERE property_id = %s
    """

    cursor.execute(update_query, (property_id,))

    conn.commit()

    print("\n✅ Booking Cancelled Successfully!")

    conn.close()  
    # COMPANY DASHBOARD
def company_dashboard():

    conn = connect_db()

    cursor = conn.cursor()

    # TOTAL PROPERTIES
    cursor.execute("SELECT COUNT(*) FROM properties")

    total_properties = cursor.fetchone()[0]

    # AVAILABLE PROPERTIES
    cursor.execute("""
    SELECT COUNT(*) FROM properties
    WHERE status = 'Available'
    """)

    available_properties = cursor.fetchone()[0]

    # BOOKED PROPERTIES
    cursor.execute("""
    SELECT COUNT(*) FROM properties
    WHERE status = 'Booked'
    """)

    booked_properties = cursor.fetchone()[0]

    # SOLD PROPERTIES
    cursor.execute("""
    SELECT COUNT(*) FROM properties
    WHERE status = 'Sold'
    """)

    sold_properties = cursor.fetchone()[0]

    # TOTAL BOOKINGS
    cursor.execute("SELECT COUNT(*) FROM bookings")

    total_bookings = cursor.fetchone()[0]

    print("\n===================================")
    print("        COMPANY DASHBOARD")
    print("===================================")

    print(f"\nTotal Properties      : {total_properties}")

    print(f"Available Properties  : {available_properties}")

    print(f"Booked Properties     : {booked_properties}")

    print(f"Sold Properties       : {sold_properties}")

    print(f"Total Bookings        : {total_bookings}")

    print("\n===================================")

    conn.close()

    # ANALYTICS DASHBOARD
def analytics_dashboard():

    conn = connect_db()

    cursor = conn.cursor()

    # TOTAL PROPERTIES
    cursor.execute("SELECT COUNT(*) FROM properties")
    total_properties = cursor.fetchone()[0]

    # AVAILABLE PROPERTIES
    cursor.execute("""
    SELECT COUNT(*) FROM properties
    WHERE status = 'Available'
    """)
    available_properties = cursor.fetchone()[0]

    # BOOKED PROPERTIES
    cursor.execute("""
    SELECT COUNT(*) FROM properties
    WHERE status = 'Booked'
    """)
    booked_properties = cursor.fetchone()[0]

    # AVERAGE PRICE
    cursor.execute("""
    SELECT AVG(price) FROM properties
    """)
    average_price = cursor.fetchone()[0]

    # MAX PRICE
    cursor.execute("""
    SELECT MAX(price) FROM properties
    """)
    max_price = cursor.fetchone()[0]

    print("\n===================================")
    print("     REAL ESTATE ANALYTICS")
    print("===================================")

    print(f"\nTotal Properties     : {total_properties}")

    print(f"Available Properties : {available_properties}")

    print(f"Booked Properties    : {booked_properties}")

    print(f"Average Price        : ₹{round(average_price,2)}")

    print(f"Highest Price        : ₹{max_price}")

    print("\n===================================")

    conn.close()
import matplotlib.pyplot as plt

# PROPERTY STATUS CHART
def property_chart():

    conn = connect_db()

    cursor = conn.cursor()

    # AVAILABLE COUNT
    cursor.execute("""
    SELECT COUNT(*) FROM properties
    WHERE status = 'Available'
    """)
    available = cursor.fetchone()[0]

    # BOOKED COUNT
    cursor.execute("""
    SELECT COUNT(*) FROM properties
    WHERE status = 'Booked'
    """)
    booked = cursor.fetchone()[0]

    labels = ["Available", "Booked"]

    values = [available, booked]

    plt.figure(figsize=(6,6))

    plt.pie(values, labels=labels, autopct='%1.1f%%')

    plt.title("Property Status Analysis")

    plt.show()

    conn.close()
 # CITY WISE PRICE ANALYSIS
def city_price_chart():

    conn = connect_db()

    cursor = conn.cursor()

    query = """
    SELECT location, AVG(price)
    FROM properties
    GROUP BY location
    ORDER BY AVG(price) DESC
    LIMIT 15
    """

    cursor.execute(query)

    data = cursor.fetchall()

    cities = []
    prices = []

    for row in data:

        cities.append(row[0])

        prices.append(float(row[1]) / 10000000)

    # MODERN STYLE
    plt.style.use('dark_background')

    # FIGURE SIZE
    fig, ax = plt.subplots(figsize=(16,8))

    # COLORS
    colors = plt.cm.Blues_r(
        [i/len(cities) for i in range(len(cities))]
    )

    # HORIZONTAL BAR CHART
    bars = ax.barh(
        cities,
        prices,
        color=colors,
        edgecolor='white'
    )

    # HIGHEST VALUE ON TOP
    ax.invert_yaxis()

    # TITLE
    ax.set_title(
        "Top 15 Cities By Average Property Prices",
        fontsize=24,
        fontweight='bold',
        pad=20
    )

    # AXIS LABELS
    ax.set_xlabel(
        "Average Price (Crores ₹)",
        fontsize=14
    )

    ax.set_ylabel(
        "Cities",
        fontsize=14
    )

    # GRID
    ax.grid(
        axis='x',
        linestyle='--',
        alpha=0.3
    )

    # REMOVE EXTRA BORDER
    ax.spines['top'].set_visible(False)

    ax.spines['right'].set_visible(False)

    # VALUE LABELS
    for bar in bars:

        width = bar.get_width()

        ax.text(
            width + 0.05,
            bar.get_y() + bar.get_height()/2,
            f'₹{width:.2f}Cr',
            va='center',
            fontsize=10,
            fontweight='bold'
        )

    # LAYOUT
    plt.tight_layout()

    # SHOW GRAPH
    plt.show()

    conn.close()