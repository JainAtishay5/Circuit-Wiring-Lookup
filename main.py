
import csv

# ==========================================
# CIRCUIT WIRING LOOKUP SYSTEM
# ==========================================

CSV_FILE = "circuit_wiring.csv"

headers = ["Cable", "Power TB", "Power No", "RTD", "RTD No"]


def generate_data():
    rows = []

    for circuit_num in range(1, 73):

        # Every 6 circuits use a new TB and DTM
        block = (circuit_num - 1) // 6

        tb = f"tb{block + 2}"
        dtm = f"dtm{block + 1}"

        # RTD number resets after every 6 circuits
        rtd_num = ((circuit_num - 1) % 6) + 1

        cable = f"c{circuit_num}"

        rows.append([cable, tb, "1", dtm, f"{rtd_num}a"])
        rows.append([cable, tb, "2", dtm, f"{rtd_num}b"])
        rows.append([cable, tb, "g", dtm, "b"])
        rows.append([cable, "", "", dtm, "shield"])

    # Save all data into CSV
    with open(CSV_FILE, "w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow(headers)

        for row in rows:
            writer.writerow(row)

            # Blank row between circuits
            if row[0] != "":
                pass

    return rows


def display_circuit(rows, circuit):

    result = [row for row in rows if row[0] == circuit]

    if not result:
        print("Circuit not found.\n")
        return

    # Keep the original table-style output
    print()
    print(
        f"{'Cable':>5} {'Power TB':>8} "
        f"{'Power No':>8} {'RTD':>5} {'RTD No':>8}"
    )

    for row in result:
        cable, power_tb, power_no, rtd, rtd_no = row

        print(
            f"{cable:>5} {power_tb:>8} "
            f"{power_no:>8} {rtd:>5} {rtd_no:>8}"
        )

    print()


# ==========================================
# MAIN PROGRAM
# ==========================================

data = generate_data()

print("Circuit Wiring Lookup System")
print("Circuits available: c1 to c72")
print("Type 'exit' to close the program.\n")

while True:

    circuit = input("Enter circuit (e.g. c1, c12): ").strip().lower()

    if circuit == "exit":
        print("Program closed.")
        break

    display_circuit(data, circuit)
