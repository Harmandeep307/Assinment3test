# requisition_v2.py

def collect_requisition_data():
    print("\n--- Staff Requisition Entry ---")
    entries = []
    counter = 1000

    while True:
        date = input("Enter date (dd/mm/yyyy): ")
        staff_id = input("Staff ID: ")
        name = input("Staff Name: ")
        counter += 1
        req_id = f"REQ{counter}"

        print(f"Requisition ID created: {req_id}")

        entries.append({
            "date": date,
            "staff_id": staff_id,
            "staff_name": name,
            "requisition_id": req_id,
            "items": [],
            "total": 0.0,
            "status": "",
            "reference": None
        })

        more = input("Add another requisition? (yes/no): ").strip().lower()
        if more != "yes":
            break

    return entries


def input_items(entries):
    print("\n--- Enter Requisition Items ---")
    for req in entries:
        print(f"\nFor {req['staff_name']} ({req['requisition_id']}):")
        while True:
            item = input("Item name (or 'done' to finish): ").strip()
            if item.lower() == "done":
                break
            try:
                price = float(input(f"Price for {item}: $"))
                req["items"].append((item, price))
                req["total"] += price
            except ValueError:
                print("Invalid price. Please enter a numeric value.")

        print(f"Total for {req['staff_name']} so far: ${req['total']:.2f}")


def process_approvals(entries):
    print("\n--- Processing Approvals ---")
    for req in entries:
        total = req["total"]
        if total <= 500:
            req["status"] = "Approved"
            req["reference"] = f"{req['staff_id']}{req['requisition_id'][-3:]}"
        elif total <= 1000:
            req["status"] = "Pending"
        else:
            req["status"] = "Rejected"


def print_summaries(entries):
    print("\n--- Requisition Summary ---")
    for req in entries:
        print(f"\nID: {req['requisition_id']} | Staff: {req['staff_name']} | Total: ${req['total']:.2f}")
        print(f"Status: {req['status']}")
        if req["reference"]:
            print(f"Reference #: {req['reference']}")

    print("\n--- Summary Report ---")
    print(f"Total Requisitions: {len(entries)}")
    print("Approved:", sum(1 for r in entries if r["status"] == "Approved"))
    print("Pending:", sum(1 for r in entries if r["status"] == "Pending"))
    print("Rejected:", sum(1 for r in entries if r["status"] == "Rejected"))


# Run the program
if __name__ == "__main__":
    data = collect_requisition_data()
    input_items(data)
    process_approvals(data)
    print_summaries(data)
