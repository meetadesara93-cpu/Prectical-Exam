import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class Tracker:
    def __init__(self, file_name="expense_data.csv"):
        self.file = file_name
        try:
            self.df = pd.read_csv(self.file)
        except FileNotFoundError:
            # Create empty DataFrame if file doesn't exist
            self.df = pd.DataFrame(columns=["Date", "Amount", "Category", "Description"])
        self.df.fillna(0, inplace=True)

    # -----------
    def add(self, date, amount, category, desc):
        entry = f"{date},{amount},{category},{desc}\n"
        with open(self.file, "a") as f:
            f.write(entry)
        print("Expense recorded!")

    # ------------------
    def summary(self):
        print("\n------ Expense Summary ------")
        avg_val = np.round(self.df["Amount"].mean(), 2)
        total_val = self.df["Amount"].sum()
        print(f"Average Expense: {avg_val}")
        print(f"Total Expense  : {total_val}")

    # --------------
    def visualize(self):
        print("\nAvailable Graphs:")
        print("1. Bar Chart (Category vs Amount)")
        print("2. Line Graph (Date vs Amount)")
        print("3. Pie Chart (Category share)")
        print("4. Histogram (Expense distribution)")

        try:
            choice = int(input("Pick option (1-4): "))
        except ValueError:
            print("Please enter a number between 1-4")
            return

        if choice == 1:
            self.df.groupby("Category")["Amount"].sum().plot(kind="bar", figsize=(9, 5))
            plt.title("Expenses by Category")
            plt.xlabel("Category")
            plt.ylabel("Amount")
            plt.xticks(rotation=45)

        elif choice == 2:
            self.df.groupby("Date")["Amount"].sum().plot(kind="line", marker="o", figsize=(10, 5))
            plt.title("Expenses Over Time")
            plt.xlabel("Date")
            plt.ylabel("Amount")
            plt.xticks(rotation=45)

        elif choice == 3:
            self.df.groupby("Category")["Amount"].sum().plot(kind="pie", autopct="%1.1f%%", figsize=(7, 7))
            plt.title("Category-wise Expense Distribution")
            plt.ylabel("")

        elif choice == 4:
            self.df["Amount"].plot(kind="hist", bins=8, edgecolor="black", figsize=(9, 5))
            plt.title("Expense Amount Histogram")
            plt.xlabel("Amount")
            plt.ylabel("Count")

        else:
            print("Wrong option!")
            return

        plt.tight_layout()
        plt.show()

    # ---------------
    def report(self):
        rep = self.df.groupby("Category")["Amount"].sum().reset_index()
        print("\n------ Expense Report ------")
        print(rep)

    # ---------------
    def filter_data(self, rule):
        try:
            filtered = self.df.query(rule)
            print("\n------ Filtered Data ------")
            print(filtered)
        except Exception as e:
            print("Invalid filter:", e)


# ---------------
def main():
    tracker = Tracker()

    while True:
        print("\n====== EXPENSE TRACKER ======")
        print("1. Add Expense")
        print("2. Summary")
        print("3. Visualize")
        print("4. Report")
        print("5. Filter Data")
        print("6. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Enter a valid number (1-6).")
            continue

        if choice == 1:
            d = input("Enter Date (YYYY-MM-DD): ")
            a = float(input("Enter Amount: "))
            c = input("Enter Category: ")
            desc = input("Enter Description: ")
            tracker.add(d, a, c, desc)

        elif choice == 2:
            tracker.summary()

        elif choice == 3:
            tracker.visualize()

        elif choice == 4:
            tracker.report()

        elif choice == 5:
            cond = input("Enter condition (e.g. Amount > 100 or Category == 'Food'): ")
            tracker.filter_data(cond)

        elif choice == 6:
            print("👋 Goodbye!")
            break

        else:
            print(" Invalid choice!")


if __name__ == "__main__":
    main()