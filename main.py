from auth import login

from Property_ops import (
    add_property,
    view_properties,
    update_property,
    delete_property,
    search_property,
    book_property,
    cancel_booking,
    company_dashboard,
    analytics_dashboard,
    property_chart,
    city_price_chart
)

# =========================
# LOGIN SYSTEM
# =========================

users = login()

if not users:
    exit()

# USER ROLE
role = users[3]

# =========================
# MAIN APPLICATION LOOP
# =========================

while True:

    print("\n===================================")
    print("   PROPERTY MANAGEMENT SYSTEM")
    print("===================================")

    # =========================
    # ADMIN / CEO MENU
    # =========================

    if role.lower() in ["admin", "ceo"]:

        print("1. Company Dashboard")
        print("2. Analytics Dashboard")
        print("3. Property Status Chart")
        print("4. City Price Analysis")
        print("5. Add Property")
        print("6. View Properties")
        print("7. Update Property")
        print("8. Delete Property")
        print("9. Search Property")
        print("10. Exit")

        choice = input("\nEnter your choice: ")

        # COMPANY DASHBOARD
        if choice == "1":

            company_dashboard()

        # ANALYTICS DASHBOARD
        elif choice == "2":

            analytics_dashboard()

        # PROPERTY STATUS CHART
        elif choice == "3":

            property_chart()

        # CITY PRICE ANALYSIS
        elif choice == "4":

            city_price_chart()

        # ADD PROPERTY
        elif choice == "5":

            add_property()

        # VIEW PROPERTIES
        elif choice == "6":

            view_properties()

        # UPDATE PROPERTY
        elif choice == "7":

            update_property()

        # DELETE PROPERTY
        elif choice == "8":

            delete_property()

        # SEARCH PROPERTY
        elif choice == "9":

            search_property()

        # EXIT
        elif choice == "10":

            print("\nThank You!")

            break

        else:

            print("\nInvalid Choice!")

    # =========================
    # CUSTOMER MENU
    # =========================

    else:

        print("1. View Properties")
        print("2. Search Property")
        print("3. Book Property")
        print("4. Cancel Booking")
        print("5. Exit")

        choice = input("\nEnter your choice: ")

        # VIEW PROPERTIES
        if choice == "1":

            view_properties()

        # SEARCH PROPERTY
        elif choice == "2":

            search_property()

        # BOOK PROPERTY
        elif choice == "3":

            book_property()

        # CANCEL BOOKING
        elif choice == "4":

            cancel_booking()

        # EXIT
        elif choice == "5":

            print("\nThank You!")

            break

        else:

            print("\nInvalid Choice!")