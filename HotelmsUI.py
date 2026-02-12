import tkinter as tk
from tkinter import ttk, messagebox
from datetime import date


class HotelManagementApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Hewing Hotel Management System")
        self.root.geometry("900x650")
        self.root.resizable(False, False)
        
        # Customer data
        self.customer = {
            'name': '',
            'address': '',
            'checkin': '',
            'checkout': '',
            'room_no': 101,
            'id_type': '',
            'id_number': ''
        }
        
        # Bill data
        self.room_rent = 0
        self.restaurant_bill = 0
        self.laundry_bill = 0
        self.game_bill = 0
        self.service_charge = 1800
        
        # Price lists
        self.room_prices = {
            'Type A (Deluxe)': 6000,
            'Type B (Superior)': 5000,
            'Type C (Standard)': 4000,
            'Type D (Economy)': 3000
        }
        
        self.restaurant_items = {
            'Water': 20,
            'Tea': 10,
            'Breakfast Combo': 90,
            'Lunch': 110,
            'Dinner': 150
        }
        
        self.laundry_items = {
            'Shorts': 3,
            'Trousers': 4,
            'Shirt': 5,
            'Jeans': 6,
            'Suit': 8
        }
        
        self.game_items = {
            'Table Tennis': 60,
            'Bowling': 80,
            'Snooker': 70,
            'Video Games': 90,
            'Pool': 50
        }
        
        self.setup_ui()
        
    def setup_ui(self):
        # Header
        header = tk.Frame(self.root, bg="#2c3e50", height=80)
        header.pack(fill=tk.X)
        header.pack_propagate(False)
        
        title = tk.Label(header, text="★ WELCOME TO HEWING HOTEL ★", 
                        font=("Arial", 24, "bold"), fg="white", bg="#2c3e50")
        title.pack(expand=True)
        
        # Main container
        main_container = tk.Frame(self.root, bg="#ecf0f1")
        main_container.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Left panel - Customer Info & Room
        left_panel = tk.Frame(main_container, bg="#ecf0f1")
        left_panel.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5)
        
        # Customer Information Section
        self.create_customer_section(left_panel)
        
        # Room Selection Section
        self.create_room_section(left_panel)
        
        # Right panel - Services
        right_panel = tk.Frame(main_container, bg="#ecf0f1")
        right_panel.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=5)
        
        # Restaurant Section
        self.create_restaurant_section(right_panel)
        
        # Laundry Section
        self.create_laundry_section(right_panel)
        
        # Game Section
        self.create_game_section(right_panel)
        
        # Bottom panel - Bill Summary
        self.create_bill_section()
        
    def create_section_frame(self, parent, title):
        frame = tk.LabelFrame(parent, text=title, font=("Arial", 11, "bold"),
                             bg="#ecf0f1", fg="#2c3e50", padx=10, pady=5)
        frame.pack(fill=tk.X, pady=5)
        return frame
        
    def create_customer_section(self, parent):
        frame = self.create_section_frame(parent, "Customer Information")
        
        # Name
        tk.Label(frame, text="Name:", bg="#ecf0f1").grid(row=0, column=0, sticky="w", pady=2)
        self.name_entry = tk.Entry(frame, width=25)
        self.name_entry.grid(row=0, column=1, pady=2, padx=5)
        
        # Address
        tk.Label(frame, text="Address:", bg="#ecf0f1").grid(row=1, column=0, sticky="w", pady=2)
        self.address_entry = tk.Entry(frame, width=25)
        self.address_entry.grid(row=1, column=1, pady=2, padx=5)
        
        # Check-in Date
        tk.Label(frame, text="Check-in:", bg="#ecf0f1").grid(row=2, column=0, sticky="w", pady=2)
        self.checkin_entry = tk.Entry(frame, width=25)
        self.checkin_entry.grid(row=2, column=1, pady=2, padx=5)
        self.checkin_entry.insert(0, date.today().strftime("%Y-%m-%d"))
        
        # Check-out Date
        tk.Label(frame, text="Check-out:", bg="#ecf0f1").grid(row=3, column=0, sticky="w", pady=2)
        self.checkout_entry = tk.Entry(frame, width=25)
        self.checkout_entry.grid(row=3, column=1, pady=2, padx=5)
        
        # Government ID Type
        tk.Label(frame, text="Govt ID Type:", bg="#ecf0f1").grid(row=4, column=0, sticky="w", pady=2)
        self.id_type_combo = ttk.Combobox(frame, values=['Aadhar Card', 'PAN Card', 'Passport', 'Driving License', 'Voter ID'], width=22, state="readonly")
        self.id_type_combo.grid(row=4, column=1, pady=2, padx=5)
        self.id_type_combo.set('Aadhar Card')
        
        # Government ID Number
        tk.Label(frame, text="Govt ID No:", bg="#ecf0f1").grid(row=5, column=0, sticky="w", pady=2)
        self.id_number_entry = tk.Entry(frame, width=25)
        self.id_number_entry.grid(row=5, column=1, pady=2, padx=5)
        
        # Room Number
        tk.Label(frame, text="Room No:", bg="#ecf0f1").grid(row=6, column=0, sticky="w", pady=2)
        self.room_no_label = tk.Label(frame, text="101", bg="#ecf0f1", font=("Arial", 10, "bold"))
        self.room_no_label.grid(row=6, column=1, sticky="w", pady=2, padx=5)
        
        # Save button
        save_btn = tk.Button(frame, text="Save Customer Info", bg="#27ae60", fg="white",
                            command=self.save_customer_info)
        save_btn.grid(row=7, column=0, columnspan=2, pady=10)
        
    def create_room_section(self, parent):
        frame = self.create_section_frame(parent, "Room Selection")
        
        # Room type
        tk.Label(frame, text="Room Type:", bg="#ecf0f1").grid(row=0, column=0, sticky="w", pady=2)
        self.room_type = ttk.Combobox(frame, values=list(self.room_prices.keys()), width=22, state="readonly")
        self.room_type.grid(row=0, column=1, pady=2, padx=5)
        self.room_type.set('Type A (Deluxe)')
        
        # Price display
        tk.Label(frame, text="Rate/Night:", bg="#ecf0f1").grid(row=1, column=0, sticky="w", pady=2)
        self.room_price_label = tk.Label(frame, text="Rs 6000", bg="#ecf0f1", fg="#e74c3c", 
                                         font=("Arial", 10, "bold"))
        self.room_price_label.grid(row=1, column=1, sticky="w", pady=2, padx=5)
        self.room_type.bind("<<ComboboxSelected>>", self.update_room_price)
        
        # Nights
        tk.Label(frame, text="No. of Nights:", bg="#ecf0f1").grid(row=2, column=0, sticky="w", pady=2)
        self.nights_spinbox = tk.Spinbox(frame, from_=1, to=365, width=23)
        self.nights_spinbox.grid(row=2, column=1, pady=2, padx=5)
        
        # Calculate button
        calc_btn = tk.Button(frame, text="Calculate Room Rent", bg="#3498db", fg="white",
                            command=self.calculate_room_rent)
        calc_btn.grid(row=3, column=0, columnspan=2, pady=10)
        
        # Room rent display
        self.room_rent_label = tk.Label(frame, text="Room Rent: Rs 0", bg="#ecf0f1", 
                                        font=("Arial", 10, "bold"), fg="#2c3e50")
        self.room_rent_label.grid(row=4, column=0, columnspan=2, pady=2)
        
    def create_service_section(self, parent, title, items, bill_callback):
        frame = self.create_section_frame(parent, title)
        
        # Item selection
        item_names = list(items.keys())
        item_combo = ttk.Combobox(frame, values=item_names, width=15, state="readonly")
        item_combo.grid(row=0, column=0, pady=2, padx=2)
        item_combo.set(item_names[0])
        
        # Quantity
        qty_spinbox = tk.Spinbox(frame, from_=1, to=100, width=5)
        qty_spinbox.grid(row=0, column=1, pady=2, padx=2)
        
        # Add button
        add_btn = tk.Button(frame, text="Add", bg="#9b59b6", fg="white", width=6,
                           command=lambda: bill_callback(item_combo, qty_spinbox))
        add_btn.grid(row=0, column=2, pady=2, padx=2)
        
        # Total label
        total_label = tk.Label(frame, text="Total: Rs 0", bg="#ecf0f1", font=("Arial", 9, "bold"))
        total_label.grid(row=1, column=0, columnspan=3, pady=2)
        
        return item_combo, qty_spinbox, total_label
        
    def create_restaurant_section(self, parent):
        self.rest_combo, self.rest_qty, self.rest_total = self.create_service_section(
            parent, "Restaurant (per item)", self.restaurant_items, self.add_restaurant_item)
        
    def create_laundry_section(self, parent):
        self.laundry_combo, self.laundry_qty, self.laundry_total = self.create_service_section(
            parent, "Laundry (per piece)", self.laundry_items, self.add_laundry_item)
        
    def create_game_section(self, parent):
        self.game_combo, self.game_qty, self.game_total = self.create_service_section(
            parent, "Games (per hour)", self.game_items, self.add_game_item)
        
    def create_bill_section(self):
        frame = tk.LabelFrame(self.root, text="Bill Summary", font=("Arial", 12, "bold"),
                             bg="#2c3e50", fg="white", padx=20, pady=10)
        frame.pack(fill=tk.X, padx=10, pady=5)
        
        # Bill items in a row
        bill_frame = tk.Frame(frame, bg="#2c3e50")
        bill_frame.pack(fill=tk.X)
        
        labels = [
            ("Room:", "room_bill_val", "0"),
            ("Restaurant:", "rest_bill_val", "0"),
            ("Laundry:", "laundry_bill_val", "0"),
            ("Games:", "game_bill_val", "0"),
            ("Service Charge:", "service_val", "1800"),
            ("GRAND TOTAL:", "grand_total_val", "1800")
        ]
        
        for i, (text, attr, val) in enumerate(labels):
            tk.Label(bill_frame, text=text, bg="#2c3e50", fg="white", 
                    font=("Arial", 10)).grid(row=0, column=i*2, padx=5)
            label = tk.Label(bill_frame, text=f"Rs {val}", bg="#2c3e50", fg="#f1c40f",
                           font=("Arial", 10, "bold"))
            label.grid(row=0, column=i*2+1, padx=5)
            setattr(self, attr, label)
        
        # Buttons
        btn_frame = tk.Frame(frame, bg="#2c3e50")
        btn_frame.pack(fill=tk.X, pady=10)
        
        tk.Button(btn_frame, text="Generate Bill", bg="#27ae60", fg="white", width=15,
                 font=("Arial", 10, "bold"), command=self.generate_bill).pack(side=tk.LEFT, padx=10)
        tk.Button(btn_frame, text="Reset All", bg="#e74c3c", fg="white", width=15,
                 font=("Arial", 10, "bold"), command=self.reset_all).pack(side=tk.LEFT, padx=10)
        tk.Button(btn_frame, text="Exit", bg="#7f8c8d", fg="white", width=15,
                 font=("Arial", 10, "bold"), command=self.root.quit).pack(side=tk.RIGHT, padx=10)
    
    # Event handlers
    def save_customer_info(self):
        name = self.name_entry.get().strip()
        if not name:
            messagebox.showwarning("Warning", "Please enter customer name!")
            return
            
        self.customer['name'] = name
        self.customer['address'] = self.address_entry.get().strip()
        self.customer['checkin'] = self.checkin_entry.get().strip()
        self.customer['checkout'] = self.checkout_entry.get().strip()
        self.customer['id_type'] = self.id_type_combo.get()
        self.customer['id_number'] = self.id_number_entry.get().strip()
        messagebox.showinfo("Success", f"Customer info saved!\nRoom No: {self.customer['room_no']}")
        
    def update_room_price(self, event=None):
        room_type = self.room_type.get()
        price = self.room_prices.get(room_type, 0)
        self.room_price_label.config(text=f"Rs {price}")
        
    def calculate_room_rent(self):
        room_type = self.room_type.get()
        price = self.room_prices.get(room_type, 0)
        try:
            nights = int(self.nights_spinbox.get())
        except ValueError:
            nights = 1
        self.room_rent = price * nights
        self.room_rent_label.config(text=f"Room Rent: Rs {self.room_rent}")
        self.update_bill_summary()
        
    def add_restaurant_item(self, combo, qty):
        item = combo.get()
        price = self.restaurant_items.get(item, 0)
        try:
            quantity = int(qty.get())
        except ValueError:
            quantity = 1
        self.restaurant_bill += price * quantity
        self.rest_total.config(text=f"Total: Rs {self.restaurant_bill}")
        self.update_bill_summary()
        
    def add_laundry_item(self, combo, qty):
        item = combo.get()
        price = self.laundry_items.get(item, 0)
        try:
            quantity = int(qty.get())
        except ValueError:
            quantity = 1
        self.laundry_bill += price * quantity
        self.laundry_total.config(text=f"Total: Rs {self.laundry_bill}")
        self.update_bill_summary()
        
    def add_game_item(self, combo, qty):
        item = combo.get()
        price = self.game_items.get(item, 0)
        try:
            hours = int(qty.get())
        except ValueError:
            hours = 1
        self.game_bill += price * hours
        self.game_total.config(text=f"Total: Rs {self.game_bill}")
        self.update_bill_summary()
        
    def update_bill_summary(self):
        self.room_bill_val.config(text=f"Rs {self.room_rent}")
        self.rest_bill_val.config(text=f"Rs {self.restaurant_bill}")
        self.laundry_bill_val.config(text=f"Rs {self.laundry_bill}")
        self.game_bill_val.config(text=f"Rs {self.game_bill}")
        
        grand_total = (self.room_rent + self.restaurant_bill + 
                      self.laundry_bill + self.game_bill + self.service_charge)
        self.grand_total_val.config(text=f"Rs {grand_total}")
        
    def generate_bill(self):
        if not self.customer['name']:
            messagebox.showwarning("Warning", "Please enter and save customer information first!")
            return
            
        subtotal = self.room_rent + self.restaurant_bill + self.laundry_bill + self.game_bill
        grand_total = subtotal + self.service_charge
        
        bill_text = f"""
{'='*50}
           HEWING HOTEL - INVOICE
{'='*50}

Customer Details:
-----------------
Name:        {self.customer['name']}
Address:     {self.customer['address']}
{self.customer['id_type']}:  {self.customer['id_number']}
Room No:     {self.customer['room_no']}
Check-in:    {self.customer['checkin']}
Check-out:   {self.customer['checkout']}

Bill Details:
-----------------
Room Rent:         Rs {self.room_rent:>10}
Restaurant Bill:   Rs {self.restaurant_bill:>10}
Laundry Bill:      Rs {self.laundry_bill:>10}
Game Bill:         Rs {self.game_bill:>10}
{'-'*35}
Sub Total:         Rs {subtotal:>10}
Service Charge:    Rs {self.service_charge:>10}
{'-'*35}
GRAND TOTAL:       Rs {grand_total:>10}

{'='*50}
     Thank you for staying with us!
{'='*50}
"""
        # Show bill in a new window
        bill_window = tk.Toplevel(self.root)
        bill_window.title("Invoice")
        bill_window.geometry("400x500")
        
        text_widget = tk.Text(bill_window, font=("Courier", 10), bg="#fff9e6")
        text_widget.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        text_widget.insert(tk.END, bill_text)
        text_widget.config(state=tk.DISABLED)
        
        # Increment room number for next customer
        self.customer['room_no'] += 1
        self.room_no_label.config(text=str(self.customer['room_no']))
        
    def reset_all(self):
        # Reset bills
        self.room_rent = 0
        self.restaurant_bill = 0
        self.laundry_bill = 0
        self.game_bill = 0
        
        # Reset entries
        self.name_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)
        self.checkin_entry.delete(0, tk.END)
        self.checkin_entry.insert(0, date.today().strftime("%Y-%m-%d"))
        self.checkout_entry.delete(0, tk.END)
        
        # Reset spinboxes
        self.nights_spinbox.delete(0, tk.END)
        self.nights_spinbox.insert(0, "1")
        
        # Reset labels
        self.room_rent_label.config(text="Room Rent: Rs 0")
        self.rest_total.config(text="Total: Rs 0")
        self.laundry_total.config(text="Total: Rs 0")
        self.game_total.config(text="Total: Rs 0")
        
        # Reset ID fields
        self.id_type_combo.set('Aadhar Card')
        self.id_number_entry.delete(0, tk.END)
        
        # Reset customer
        self.customer = {
            'name': '',
            'address': '',
            'checkin': '',
            'checkout': '',
            'room_no': self.customer['room_no'],
            'id_type': '',
            'id_number': ''
        }
        
        self.update_bill_summary()
        messagebox.showinfo("Reset", "All fields have been reset!")


def main():
    root = tk.Tk()
    app = HotelManagementApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
