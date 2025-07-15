import tkinter as tk
from tkinter import ttk
import random
import hashlib
import json
from datetime import datetime

class TrapGodzGame:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Trap Godz 1.0")
        self.root.geometry("1400x900")  # Expanded window size
        
        # Initialize game state
        self.funds = 10000
        self.crypto_wallet = {"BTC": 0, "ETH": 0, "XMR": 0}
        self.inventory = {
            "Pressed Pills": 0,
            "Carfentanyl": 0,
            "Xene Analog": 0,
            "Mixed Colored Down": 0,
            "DMT": 0,
            "MDMA": 0,
            "Ketamine": 0,
            "PCP": 0,
            "Methamphetamine": 0,
            "GHB": 0,
            "LSD": 0,
            "Fentanyl": 0,
            "Research Chemicals": 0,
            "Meth": 0,
            "Fentanyl Blues": 0,
            "Xanax": 0,
            "Black Tar Heroin": 0
        }
        self.territory_control = {}
        self.security_level = 1
        self.logistics_network = []
        self.messages = []
        self.production_level = 1
        self.equipment = {
            "Basic Lab Equipment": False,
            "Intermediate Lab Equipment": False,
            "Advanced Lab Equipment": False
        }
        self.precursors = {
            "DMT Precursors": 0,
            "MDMA Precursors": 0,
            "Ketamine Precursors": 0,
            "PCP Precursors": 0,
            "Meth Precursors": 0,
            "GHB Precursors": 0,
            "LSD Precursors": 0,
            "Fentanyl Precursors": 0
        }
        self.vehicles = []
        self.vehicle_dealers = self.initialize_dealers()
        self.fraud_level = 1
        self.telegram_contacts = []
        self.dumps_inventory = []
        self.cvv_inventory = []
        self.fraud_equipment = {
            "Basic Skimmer": False,
            "CVV Scanner": False,
            "High-Tech Skimmer": False
        }
        
        self.setup_ui()
        self.initialize_cryptocurrency_system()
        self.setup_logistics_network()
        self.setup_communication_system()
        self.setup_production_ui()
        self.setup_vehicle_ui()
        self.setup_fraud_ui()
        self.initialize_telegram_network()

    def initialize_cryptocurrency_system(self):
        """Initialize cryptocurrency wallet and transaction system"""
        self.transaction_history = []
        self.current_blockchain_height = 0
        
    def setup_logistics_network(self):
        """Initialize shipping ports and routes"""
        # Eastern Canada ports
        self.ports = [
            {"name": "Montreal", "risk": 0.7, "capacity": 1000},
            {"name": "Toronto", "risk": 0.8, "capacity": 800},
            {"name": "Ottawa", "risk": 0.6, "capacity": 1200},
            {"name": "Halifax", "risk": 0.65, "capacity": 1500}
        ]
        
        # Ontario ports
        self.ontario_ports = [
            {"name": "Windsor", "risk": 0.75, "capacity": 900},
            {"name": "London", "risk": 0.7, "capacity": 1100},
            {"name": "Sudbury", "risk": 0.6, "capacity": 1300}
        ]
        
        # Import locations
        self.import_locations = {
            "China": {
                "suppliers": [
                    {"name": "Shanghai Chemical Co.", "risk": 0.85, "capacity": 2000},
                    {"name": "Beijing Research Labs", "risk": 0.9, "capacity": 1500},
                    {"name": "Guangzhou Pharma", "risk": 0.8, "capacity": 1800}
                ]
            },
            "South America": {
                "ports": [
                    {"name": "Buenos Aires", "risk": 0.75, "capacity": 1200},
                    {"name": "Rio de Janeiro", "risk": 0.7, "capacity": 1500},
                    {"name": "Lima", "risk": 0.8, "capacity": 1000}
                ]
            },
            "Europe": {
                "ports": [
                    {"name": "Amsterdam", "risk": 0.65, "capacity": 1400},
                    {"name": "Rotterdam", "risk": 0.7, "capacity": 1600},
                    {"name": "Hamburg", "risk": 0.75, "capacity": 1300}
                ]
            }
        }
        
        # Domestic routes
        self.routes = [
            {"origin": "Montreal", "destination": "Toronto", "risk": 0.4},
            {"origin": "Toronto", "destination": "Ottawa", "risk": 0.3},
            {"origin": "Ottawa", "destination": "Montreal", "risk": 0.4},
            {"origin": "Halifax", "destination": "Montreal", "risk": 0.5},
            {"origin": "Windsor", "destination": "Toronto", "risk": 0.35},
            {"origin": "London", "destination": "Toronto", "risk": 0.3},
            {"origin": "Sudbury", "destination": "Ottawa", "risk": 0.4}
        ]
        
        # Import routes
        self.import_routes = {
            "China": [
                {"origin": "Shanghai", "destination": "Vancouver", "risk": 0.85},
                {"origin": "Beijing", "destination": "Toronto", "risk": 0.9},
                {"origin": "Guangzhou", "destination": "Montreal", "risk": 0.8}
            ],
            "South America": [
                {"origin": "Buenos Aires", "destination": "Halifax", "risk": 0.75},
                {"origin": "Rio de Janeiro", "destination": "Montreal", "risk": 0.7},
                {"origin": "Lima", "destination": "Toronto", "risk": 0.8}
            ],
            "Europe": [
                {"origin": "Amsterdam", "destination": "Montreal", "risk": 0.65},
                {"origin": "Rotterdam", "destination": "Halifax", "risk": 0.7},
                {"origin": "Hamburg", "destination": "Toronto", "risk": 0.75}
            ]
        }

    def setup_ui(self):
        """Set up the enhanced game interface"""
        self.left_frame = ttk.Frame(self.root)
        self.left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        self.right_frame = ttk.Frame(self.root)
        self.right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        
        # Resource Display
        resource_frame = ttk.LabelFrame(self.left_frame, text="Resources")
        resource_frame.pack(fill=tk.X, padx=5, pady=5)
        
        # Funds display
        funds_label = ttk.Label(resource_frame,
                               text=f"Funds: ${self.funds:,}")
        funds_label.pack(pady=5)
        
        # Crypto wallet display
        crypto_label = ttk.Label(resource_frame,
                                text="Cryptocurrency Wallet:")
        crypto_label.pack()
        for coin, amount in self.crypto_wallet.items():
            label = ttk.Label(resource_frame,
                             text=f"{coin}: {amount:.8f}")
            label.pack()

        # Territory control display
        territory_frame = ttk.LabelFrame(self.left_frame, 
                                        text="Territory Control")
        territory_frame.pack(fill=tk.X, padx=5, pady=5)
        
        # Security level display
        security_frame = ttk.LabelFrame(self.left_frame,
                                       text="Security Systems")
        security_frame.pack(fill=tk.X, padx=5, pady=5)
        
        security_level = ttk.Label(security_frame,
                                  text=f"Security Level: {self.security_level}")
        security_level.pack()
        
        upgrade_btn = ttk.Button(security_frame,
                                text="Upgrade Security",
                                command=self.upgrade_security)
        upgrade_btn.pack(pady=5)

        # Market Frame
        market_frame = ttk.LabelFrame(self.right_frame, text="Market")
        market_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Product buttons
        for i, product in enumerate(self.inventory):
            btn = ttk.Button(market_frame,
                            text=f"Buy {product}",
                            command=lambda p=product: self.buy_product(p))
            btn.grid(row=i//2, column=i%2, padx=5, pady=5, sticky="nsew")

        # Logistics Frame
        logistics_frame = ttk.LabelFrame(self.right_frame, text="Logistics")
        logistics_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Shipping routes
        route_frame = ttk.LabelFrame(logistics_frame, text="Available Routes")
        route_frame.pack(fill=tk.X, padx=5, pady=5)
        
        for route in self.routes:
            btn = ttk.Button(route_frame,
                            text=f"{route['origin']} → {route['destination']}\nRisk: {route['risk']*100:.0f}%",
                            command=lambda r=route: self.ship_products(r))
            btn.pack(fill=tk.X, pady=2)

        # Import routes
        import_frame = ttk.LabelFrame(logistics_frame, text="Import Routes")
        import_frame.pack(fill=tk.X, padx=5, pady=5)
        
        for region, routes in self.import_routes.items():
            region_frame = ttk.LabelFrame(import_frame, text=region)
            region_frame.pack(fill=tk.X, padx=5, pady=5)
            
            for route in routes:
                btn = ttk.Button(region_frame,
                                text=f"{route['origin']} → {route['destination']}\nRisk: {route['risk']*100:.0f}%",
                                command=lambda r=route: self.import_products(r))
                btn.pack(fill=tk.X, pady=2)

        # Communication Frame
        comms_frame = ttk.LabelFrame(self.right_frame, text="Secure Communications")
        comms_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Contact list
        contact_list = tk.Listbox(comms_frame, height=5)
        for contact in self.contacts:
            contact_list.insert(tk.END, contact)
        contact_list.pack(fill=tk.X, padx=5, pady=5)
        
        # Message input
        message_var = tk.StringVar()
        message_entry = ttk.Entry(comms_frame, textvariable=message_var)
        message_entry.pack(fill=tk.X, padx=5, pady=5)
        
        send_btn = ttk.Button(comms_frame,
                             text="Send Encrypted Message",
                             command=lambda: self.send_message(message_var.get()))
        send_btn.pack(fill=tk.X, pady=5)

    def setup_production_ui(self):
        """Set up the production interface"""
        production_frame = ttk.LabelFrame(self.right_frame, text="Production")
        production_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Production level display
        level_frame = ttk.LabelFrame(production_frame, text="Production Level")
        level_frame.pack(fill=tk.X, padx=5, pady=5)
        
        level_label = ttk.Label(level_frame, 
                               text=f"Current Level: {self.production_level}")
        level_label.pack()
        
        upgrade_btn = ttk.Button(level_frame,
                                text="Upgrade Production Level",
                                command=self.upgrade_production)
        upgrade_btn.pack(pady=5)
        
        # Equipment status
        equipment_frame = ttk.LabelFrame(production_frame, text="Equipment Status")
        equipment_frame.pack(fill=tk.X, padx=5, pady=5)
        
        for equip in self.equipment:
            status = "Installed" if self.equipment[equip] else "Not Installed"
            label = ttk.Label(equipment_frame, 
                            text=f"{equip}: {status}")
            label.pack(pady=2)
        
        # Production buttons
        production_btns_frame = ttk.LabelFrame(production_frame, text="Available Products")
        production_btns_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Level 1 products
        level1_products = ["DMT", "MDMA", "Ketamine"]
        for i, product in enumerate(level1_products):
            btn = ttk.Button(production_btns_frame,
                            text=f"Produce {product}",
                            command=lambda p=product: self.produce_product(p))
            btn.grid(row=i//2, column=i%2, padx=5, pady=5, sticky="nsew")
        
        # Level 2 products
        level2_products = ["PCP", "Methamphetamine", "GHB"]
        for i, product in enumerate(level2_products):
            btn = ttk.Button(production_btns_frame,
                            text=f"Produce {product}",
                            command=lambda p=product: self.produce_product(p))
            btn.grid(row=(i+3)//2, column=(i+3)%2, padx=5, pady=5, sticky="nsew")
        
        # Level 3 products
        level3_products = ["LSD", "Fentanyl", "Research Chemicals"]
        for i, product in enumerate(level3_products):
            btn = ttk.Button(production_btns_frame,
                            text=f"Produce {product}",
                            command=lambda p=product: self.produce_product(p))
            btn.grid(row=(i+6)//2, column=(i+6)%2, padx=5, pady=5, sticky="nsew")

    def setup_vehicle_ui(self):
        """Set up the vehicle management interface"""
        vehicle_frame = ttk.LabelFrame(self.right_frame, text="Vehicle Management")
        vehicle_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Dealership selection
        dealer_frame = ttk.LabelFrame(vehicle_frame, text="Dealerships")
        dealer_frame.pack(fill=tk.X, padx=5, pady=5)
        
        dealer_types = list(self.vehicle_dealers.keys())
        for dealer_type in dealer_types:
            dealer_type_frame = ttk.LabelFrame(dealer_frame, text=dealer_type)
            dealer_type_frame.pack(fill=tk.X, padx=5, pady=5)
            
            dealers = self.vehicle_dealers[dealer_type]
            for dealer_name, dealer_info in dealers.items():
                btn = ttk.Button(dealer_type_frame,
                                text=f"{dealer_name} ({dealer_info['type']})",
                                command=lambda dn=dealer_name, dt=dealer_type: 
                                self.open_dealer(dn, dt))
                btn.pack(fill=tk.X, pady=2)

    def setup_fraud_ui(self):
        """Set up the fraud interface"""
        fraud_frame = ttk.LabelFrame(self.right_frame, text="Fraud Operations")
        fraud_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Fraud level display
        level_frame = ttk.LabelFrame(fraud_frame, text="Fraud Level")
        level_frame.pack(fill=tk.X, padx=5, pady=5)
        
        level_label = ttk.Label(level_frame, 
                               text=f"Current Level: {self.fraud_level}")
        level_label.pack()
        
        upgrade_btn = ttk.Button(level_frame,
                                text="Upgrade Fraud Level",
                                command=self.upgrade_fraud)
        upgrade_btn.pack(pady=5)
        
        # Equipment status
        equipment_frame = ttk.LabelFrame(fraud_frame, text="Fraud Equipment")
        equipment_frame.pack(fill=tk.X, padx=5, pady=5)
        
        for equip in self.fraud_equipment:
            status = "Installed" if self.fraud_equipment[equip] else "Not Installed"
            label = ttk.Label(equipment_frame, 
                            text=f"{equip}: {status}")
            label.pack(pady=2)
        
        # Telegram contacts
        contacts_frame = ttk.LabelFrame(fraud_frame, text="Telegram Contacts")
        contacts_frame.pack(fill=tk.X, padx=5, pady=5)
        
        for contact in self.telegram_contacts:
            btn = ttk.Button(contacts_frame,
                            text=f"{contact['name']} (Risk: {contact['risk']*100:.0f}%)",
                            command=lambda c=contact: self.contact_telegram(c))
            btn.pack(fill=tk.X, pady=2)
        
        # Fraud operations
        operations_frame = ttk.LabelFrame(fraud_frame, text="Available Operations")
        operations_frame.pack(fill=tk.X, padx=5, pady=5)
        
        # Dumps operations
        dumps_frame = ttk.LabelFrame(operations_frame, text="Dumps")
        dumps_frame.pack(fill=tk.X, padx=5, pady=5)
        
        for dump_type, info in self.dumps_types.items():
            if info["min_level"] <= self.fraud_level:
                btn = ttk.Button(dumps_frame,
                                text=f"Buy {dump_type} (${info['price']:,})",
                                command=lambda dt=dump_type: self.buy_dump(dt))
                btn.pack(fill=tk.X, pady=2)
        
        # CVV operations
        cvv_frame = ttk.LabelFrame(operations_frame, text="CVVs")
        cvv_frame.pack(fill=tk.X, padx=5, pady=5)
        
        for cvv_type, info in self.cvv_types.items():
            if info["min_level"] <= self.fraud_level:
                btn = ttk.Button(cvv_frame,
                                text=f"Buy {cvv_type} (${info['price']:,})",
                                command=lambda ct=cvv_type: self.buy_cvv(ct))
                btn.pack(fill=tk.X, pady=2)

    def initialize_telegram_network(self):
        """Initialize telegram fraud network"""
        self.telegram_contacts = [
            {"name": "Dumps_Supplier_001", "reputation": 0.8, "risk": 0.3},
            {"name": "CVV_Seller_002", "reputation": 0.7, "risk": 0.4},
            {"name": "Fraud_Tools_003", "reputation": 0.9, "risk": 0.2}
        ]
        
        # Available dumps
        self.dumps_types = {
            "Basic Dumps": {"price": 500, "risk": 0.4, "min_level": 1},
            "Premium Dumps": {"price": 1000, "risk": 0.5, "min_level": 2},
            "High-Limit Dumps": {"price": 2000, "risk": 0.6, "min_level": 3}
        }
        
        # Available CVVs
        self.cvv_types = {
            "Basic CVVs": {"price": 300, "risk": 0.35, "min_level": 1},
            "Verified CVVs": {"price": 800, "risk": 0.45, "min_level": 2},
            "High-Limit CVVs": {"price": 1500, "risk": 0.55, "min_level": 3}
        }

    def upgrade_security(self):
        """Upgrade security level and systems"""
        cost = 5000 * self.security_level
        if self.funds >= cost:
            self.funds -= cost
            self.security_level += 1
            self.update_ui()
            self.add_message(f"Security Level upgraded to {self.security_level}")
        else:
            self.add_message("Insufficient funds for security upgrade!")

    def upgrade_production(self):
        """Upgrade production level"""
        costs = {1: 15000, 2: 30000, 3: 50000}
        if self.production_level < 3:
            cost = costs[self.production_level]
            if self.funds >= cost:
                self.funds -= cost
                self.production_level += 1
                self.update_ui()
                self.add_message(f"Production Level upgraded to {self.production_level}!")
            else:
                self.add_message("Insufficient funds for production upgrade!")
        else:
            self.add_message("Maximum production level reached!")

    def upgrade_fraud(self):
        """Upgrade fraud level and capabilities"""
        costs = {1: 5000, 2: 15000, 3: 30000}
        if self.fraud_level < 3:
            cost = costs[self.fraud_level]
            if self.funds >= cost:
                self.funds -= cost
                self.fraud_level += 1
                self.update_ui()
                self.add_message(f"Fraud Level upgraded to {self.fraud_level}!")
            else:
                self.add_message("Insufficient funds for fraud level upgrade!")
        else:
            self.add_message("Maximum fraud level reached!")

    def buy_dump(self, dump_type):
        """Purchase dumps from telegram contact"""
        info = self.dumps_types[dump_type]
        if self.funds >= info["price"]:
            self.funds -= info["price"]
            self.dumps_inventory.append({
                "type": dump_type,
                "risk": info["risk"],
                "amount": 1
            })
            self.add_message(f"Purchased {dump_type}!")
            self.process_fraud_risk(info["risk"])
        else:
            self.add_message("Insufficient funds for dumps purchase!")

    def buy_cvv(self, cvv_type):
        """Purchase CVVs from telegram contact"""
        info = self.cvv_types[cvv_type]
        if self.funds >= info["price"]:
            self.funds -= info["price"]
            self.cvv_inventory.append({
                "type": cvv_type,
                "risk": info["risk"],
                "amount": 1
            })
            self.add_message(f"Purchased {cvv_type}!")
            self.process_fraud_risk(info["risk"])
        else:
            self.add_message("Insufficient funds for CVV purchase!")

    def process_fraud_risk(self, risk_level):
        """Process fraud risk and consequences"""
        if random.random() < risk_level:
            consequence = self.calculate_fraud_consequence()
            self.handle_fraud_consequence(consequence)

    def calculate_fraud_consequence(self):
        """Calculate fraud consequence based on fraud level"""
        consequences = {
            1: ["Account Freeze", "Small Fine", "Warning"],
            2: ["Account Lock", "Medium Fine", "Investigation"],
            3: ["Account Seizure", "Large Fine", "Arrest"]
        }
        return random.choice(consequences[self.fraud_level-1])

    def handle_fraud_consequence(self, consequence):
        """Handle fraud consequence"""
        if consequence == "Account Freeze":
            self.funds = int(self.funds * 0.8)
            self.add_message("Account frozen! Lost 20% of funds.")
        elif consequence == "Account Lock":
            self.funds = int(self.funds * 0.6)
            self.add_message("Account locked! Lost 40% of funds.")
        elif consequence == "Account Seizure":
            self.funds = 0
            self.add_message("Account seized! All funds lost.")
        elif consequence == "Small Fine":
            fine = min(5000, self.funds)
            self.funds -= fine
            self.add_message(f"Received small fine of ${fine:,}")
        elif consequence == "Medium Fine":
            fine = min(15000, self.funds)
            self.funds -= fine
            self.add_message(f"Received medium fine of ${fine:,}")
        elif consequence == "Large Fine":
            fine = min(30000, self.funds)
            self.funds -= fine
            self.add_message(f"Received large fine of ${fine:,}")
        elif consequence == "Warning":
            self.add_message("Received warning from authorities.")
        elif consequence == "Investigation":
            self.add_message("Under investigation. Be careful!")
        elif consequence == "Arrest":
            self.add_message("Game Over: Arrested for fraud activities!")

    def contact_telegram(self, contact):
        """Handle telegram contact interaction"""
        dialog = TelegramContactDialog(self.root, contact, self)
        self.root.wait_window(dialog)

class TelegramContactDialog(tk.Toplevel):
    def __init__(self, parent, contact, game):
        super().__init__(parent)
        self.title(f"Telegram Chat - {contact['name']}")
        self.game = game
        self.contact = contact
        
        # Dialog content
        self.setup_ui()
        
    def setup_ui(self):
        """Set up the telegram chat dialog"""
        # Contact info
        info_frame = ttk.LabelFrame(self, text="Contact Information")
        info_frame.pack(fill=tk.X, padx=5, pady=5)
        
        ttk.Label(info_frame, 
                 text=f"Name: {self.contact['name']}").pack()
        ttk.Label(info_frame, 
                 text=f"Reputation: {self.contact['reputation']*100:.0f}%").pack()
        ttk.Label(info_frame, 
                 text=f"Risk Level: {self.contact['risk']*100:.0f}%").pack()
        
        # Chat history
        chat_frame = ttk.LabelFrame(self, text="Chat History")
        chat_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        self.chat_text = tk.Text(chat_frame, height=10)
        self.chat_text.insert(tk.END, "Welcome to the fraud channel!\n")
        self.chat_text.config(state=tk.DISABLED)
        
        # Message input
        input_frame = ttk.LabelFrame(self, text="Message")
        input_frame.pack(fill=tk.X, padx=5, pady=5)
        
        self.message_var = tk.StringVar()
        message_entry = ttk.Entry(input_frame, textvariable=self.message_var)
        message_entry.pack(fill=tk.X, padx=5)
        
        send_btn = ttk.Button(input_frame,
                             text="Send",
                             command=self.send_message)
        send_btn.pack(fill=tk.X, pady=5)
        
    def send_message(self):
        """Handle message sending"""
        message = self.message_var.get()
        if message:
            self.chat_text.config(state=tk.NORMAL)
            self.chat_text.insert(tk.END, f"You: {message}\n")
            self.chat_text.config(state=tk.DISABLED)
            self.message_var.set("")
            
            # Simulate response
            response = self.generate_response(message)
            self.chat_text.config(state=tk.NORMAL)
            self.chat_text.insert(tk.END, f"{self.contact['name']}: {response}\n")
            self.chat_text.config(state=tk.DISABLED)
            
            if "interested" in response.lower():
                self.offer_products()
                
    def generate_response(self, message):
        """Generate response based on message"""
        responses = {
            "hello": "Welcome to our fraud services!",
            "dumps": "We have fresh dumps available. What's your budget?",
            "cvv": "Verified CVVs in stock. High balance available.",
            "price": "Prices vary based on quality and limit. DM for details.",
            "default": "I didn't understand that. Please be more specific."
        }
        return responses.get(message.lower(), responses["default"])
        
    def offer_products(self):
        """Show available products"""
        offer_frame = ttk.LabelFrame(self, text="Available Products")
        offer_frame.pack(fill=tk.X, padx=5, pady=5)
        
        for product_type, products in self.game.dumps_types.items():
            btn = ttk.Button(offer_frame,
                            text=f"{product_type} (${products['price']:,})",
                            command=lambda pt=product_type: self.game.buy_dump(pt))
            btn.pack(fill=tk.X, pady=2)
            
        for product_type, products in self.game.cvv_types.items():
            btn = ttk.Button(offer_frame,
                            text=f"{product_type} (${products['price']:,})",
                            command=lambda pt=product_type: self.game.buy_cvv(pt))
            btn.pack(fill=tk.X, pady=2)

class ShippingDialog(tk.Toplevel):
    def __init__(self, parent, route, game):
        super().__init__(parent)
        self.title("Trap Godz 1.0 - Shipping Products")
        self.game = game
        
        # Dialog content
        ttk.Label(self, text=f"Route: {route['origin']} → {route['destination']}").pack(pady=5)
        ttk.Label(self, text=f"Risk Level: {route['risk']*100:.0f}%").pack(pady=5)
        
        # Product selection
        product_frame = ttk.LabelFrame(self, text="Select Products")
        product_frame.pack(fill=tk.X, padx=5, pady=5)
        
        for product in self.game.inventory:
            frame = ttk.Frame(product_frame)
            frame.pack(fill=tk.X, pady=2)
            
            ttk.Label(frame, text=product).pack(side=tk.LEFT)
            var = tk.StringVar(value="0")
            entry = ttk.Entry(frame, textvariable=var, width=10)
            entry.pack(side=tk.RIGHT, padx=5)
            
            setattr(self, f"{product.lower().replace(' ', '_')}_quantity", var)
        
        # Buttons
        button_frame = ttk.Frame(self)
        button_frame.pack(fill=tk.X, pady=10)
        
        ttk.Button(button_frame, text="Ship", 
                   command=self.process_shipping).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Cancel", 
                   command=self.destroy).pack(side=tk.LEFT, padx=5)

    def process_shipping(self):
        """Process shipping operation"""
        products_to_ship = {}
        total_value = 0
        
        for product in self.game.inventory:
            qty_var = getattr(self, f"{product.lower().replace(' ', '_')}_quantity")
            quantity = int(qty_var.get())
            if quantity > 0:
                products_to_ship[product] = quantity
                total_value += quantity * self.game.get_base_price(product)
        
        if products_to_ship:
            success = random.random() > self.route['risk']
            if success:
                self.game.handle_successful_shipment(products_to_ship)
                self.game.add_message("Shipping successful!")
            else:
                self.game.handle_failed_shipment(total_value)
                self.game.add_message("Shipping failed! Products lost.")
        
        self.destroy()

class ImportDialog(tk.Toplevel):
    def __init__(self, parent, route, game):
        super().__init__(parent)
        self.title("Trap Godz 1.0 - Import Products")
        self.game = game
        self.route = route
        
        # Dialog content
        ttk.Label(self, text=f"Route: {route['origin']} → {route['destination']}").pack(pady=5)
        ttk.Label(self, text=f"Risk Level: {route['risk']*100:.0f}%").pack(pady=5)
        
        # Product selection
        product_frame = ttk.LabelFrame(self, text="Select Products")
        product_frame.pack(fill=tk.X, padx=5, pady=5)
        
        for product in self.game.inventory:
            frame = ttk.Frame(product_frame)
            frame.pack(fill=tk.X, pady=2)
            
            ttk.Label(frame, text=product).pack(side=tk.LEFT)
            var = tk.StringVar(value="0")
            entry = ttk.Entry(frame, textvariable=var, width=10)
            entry.pack(side=tk.RIGHT, padx=5)
            
            setattr(self, f"{product.lower().replace(' ', '_')}_quantity", var)
        
        # Buttons
        button_frame = ttk.Frame(self)
        button_frame.pack(fill=tk.X, pady=10)
        
        ttk.Button(button_frame, text="Import", 
                   command=self.process_import).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Cancel", 
                   command=self.destroy).pack(side=tk.LEFT, padx=5)

    def process_import(self):
        """Process import operation"""
        products_to_import = {}
        total_value = 0
        
        for product in self.game.inventory:
            qty_var = getattr(self, f"{product.lower().replace(' ', '_')}_quantity")
            quantity = int(qty_var.get())
            if quantity > 0:
                products_to_import[product] = quantity
                total_value += quantity * self.game.get_import_price(product)
        
        if products_to_import:
            success = random.random() > self.route['risk']
            if success:
                self.game.handle_successful_import(products_to_import)
                self.game.add_message("Import successful!")
            else:
                self.game.handle_failed_import(total_value)
                self.game.add_message("Import failed! Products lost.")
        
        self.destroy()

# Run the game
if __name__ == "__main__":
    game = TrapGodzGame()
    game.root.mainloop()
