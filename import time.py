import time
from datetime import datetime, timedelta

# Initial setup
k = 5  # Total number of parking slots
unique_id = [[f"SLOT-{i+1}" for i in range(k)], [1]*k]  # ID + Availability (1 = free, 0 = occupied)
time_duration = [[], []]  # Customer index, requested durations
slot_num = []  # Track assigned slot numbers

# Get customer data
n = int(input("Enter number of customers: "))
for i in range(n):
    duration = int(input(f"Enter desired parking time for Customer {i+1} (in minutes): "))
    time_duration[0].append(i)
    time_duration[1].append(duration)

    # Search for vacant slot
    slot_found = False
    for s in range(k):
        if unique_id[1][s] == 1:
            slot_num.append(s)
            unique_id[1][s] = 0
            print(f"Customer {i+1} allotted {unique_id[0][s]}")
            slot_found = True
            break
    if not slot_found:
        print(f"No slots available for Customer {i+1}")
        slot_num.append(-1)  # Mark unassigned slot

print("\n--- Parking Simulation ---\n")

# Begin simulation
now = datetime.now()

for x in range(0, min(k, len(slot_num))):
    if x >= len(slot_num):
        print(f"Index {x} is out of range for slot_num list. Skipping.")
        continue

    if slot_num[x] == -1:
        continue  # Skip if no slot assigned

    
    if time_duration[1][x] <= 30:
        # Customer parked within time limit
        if x == 0:
            for j in range(0, time_duration[1][x]):
                time.sleep(0.25)  # Simulate time
                minutes_to_add = j + 1
                time_delta = timedelta(minutes=minutes_to_add)
                new_time = now + time_delta
                new_time_formatted = new_time.strftime("%H:%M")
                print(f"Time: {new_time_formatted}")
                j += 1

            now = new_time
            print(f"\nTime when slot {unique_id[0][slot_num[x]]} becomes vacant: {new_time_formatted}")
            unique_id[1][slot_num[x]] = 1
            print(f"Slot number {unique_id[0][slot_num[x]]} is now vacant.\n")
            continue

    else:
        # Customer exceeded time limit
        time_passed = 0
        for j in range(0, time_duration[1][x] - time_passed):
            time.sleep(0.5)
            minutes_to_add = j + 1
            time_delta = timedelta(minutes=minutes_to_add)
            new_time = now + time_delta
            new_time_formatted = new_time.strftime("%H:%M")
            print(f"Time: {new_time_formatted}")

            if j == 31:
                continue

            if j == 30 - time_passed - 1:
                for z in range(0, k):
                    if unique_id[1][slot_num[x]] == 0:
                        unique_id[1][slot_num[x]] = 1
                        print(f"\nSlot number {unique_id[0][slot_num[x]]} is now vacant.")
                        print(f"Time when slot {unique_id[0][slot_num[x]]} becomes vacant: {new_time_formatted}")
                        print(f"Person who parked in slot {unique_id[0][slot_num[x]]} exceeded time limit!")
                        print(">>> You exceeded your parking time limit! <<<")
                        break

        now = new_time
        fine = (time_duration[1][x] - 30) * 10
        print(f"Kindly pay the specified fine: ₹{fine}\n")

print("--- Parking Simulation Ended ---")
