#Cab Booking & Fare Management System Using Python Functions and Data Structures:


rides = [] 
def calculate_fare(distance):
    fare = 50
    if distance <= 5:
        fare += distance * 15
    elif distance <= 15:
        fare += 5*15 + (distance-5)*12
    else:
        fare += 5*15 + 10*12 + (distance-15)*10
    return fare

def book_ride():
    print("\n--- Book Ride ---")
    name = input("Customer Name: ").strip()
    pickup = input("Pickup: ").strip()
    dest = input("Destination: ").strip()
    if not name or not pickup or not dest:
        print("Error! "); return
    if pickup.lower() == dest.lower():
        print("Error! "); return
    try:
        distance = float(input("Distance in KM: "))
        if distance <= 0:
            print("Error!"); return
    except ValueError:
        print("Error!"); return
    fare = calculate_fare(distance)
    ride = {'name': name, 'pickup': pickup, 'dest': dest, 'distance': distance, 'fare': fare}
    rides.append(ride)
    print(f"Booking Success! Fare: Rs.{fare}")

def view_rides():
    print("\n--- Ride History ---")
    if not rides:
        print("Ride is not booked!"); return
    for r in rides:
        print(f"{r['name']} | {r['pickup']} -> {r['dest']} | {r['distance']} KM | Rs.{r['fare']}")

def search_ride():
    name = input("Search Name: ").strip().lower()
    for r in rides:
        if r['name'].lower() == name:
            print(f"Found! {r}"); return
    print("Ride not found!")

def revenue_report():
    if not rides:
        print("No rides!"); return
    total = sum(r['fare'] for r in rides)
    avg = total / len(rides)
    print(f"Total Rides: {len(rides)}")
    print(f"Total Revenue: Rs.{total}")
    print(f"Average Fare: Rs.{avg:.2f}")

def longest_ride():
    # BONUS 1
    if not rides:
        print("No rides!"); return
    longest = max(rides, key=lambda x: x['distance'])
    print("\n========= LONGEST RIDE =========")
    print(f"Customer Name : {longest['name']}")
    print(f"Distance      : {longest['distance']} KM")

def highest_fare():
    # BONUS 2
    if not rides:
        print("No rides!"); return
    highest = max(rides, key=lambda x: x['fare'])
    print("\n========= HIGHEST FARE =========")
    print(f"Customer Name : {highest['name']}")
    print(f"Highest Fare  : Rs.{highest['fare']}")

def daily_summary():
    if not rides:
        print("No rides!"); 
        return
    total = sum(r['fare'] for r in rides)
    total_dist = sum(r['distance'] for r in rides)
    avg_dist = total_dist / len(rides)
    highest = max(rides, key=lambda x: x['fare'])
    print("\n========= DAILY REPORT =========")
    print(f"Total Rides       : {len(rides)}")
    print(f"Total Revenue     : Rs.{total}")
    print(f"Average Distance  : {avg_dist:} KM")
    print(f"Highest Fare      : Rs.{highest['fare']}")
    print("================================")

# Main Menu - Integration
while True:
    print("\n===== CAB BOOKING SYSTEM =====")
    print("1. Book Ride\n2. View Ride History\n3. Search Ride\n4. Revenue Report\n5. Longest Ride (BONUS 1)\n6. Highest Fare (BONUS 2)\n7. Daily Summary (BONUS 3)\n8. Exit")
    choice = input("Enter Choice: ")
    if choice == '1': book_ride()
    elif choice == '2': view_rides()
    elif choice == '3': search_ride()
    elif choice == '4': revenue_report()
    elif choice == '5': longest_ride()
    elif choice == '6': highest_fare()
    elif choice == '7': daily_summary()
    elif choice == '8':
        print("Bye!"); break
    else: print("Invalid Choice!!")