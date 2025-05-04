import time

# Time-based greeting
def time_based_greeting():
    from datetime import datetime
    hour = datetime.now().hour
    if hour < 12:
        return "Good Morning!"
    elif hour < 18:
        return "Good Afternoon!"
    else:
        return "Good Evening!"

# Menu display
def show_menu():
    print("\n--- Customer Support Topics ---")
    print("1. Track Order")
    print("2. Cancel Order")
    print("3. Return Product")
    print("4. Refund Status")
    print("5. Payment Methods")
    print("6. Exchange Policy")
    print("7. Talk to Human Agent")
    print("0. Exit Chat")

# Chatbot functions for each topic
def track_order():
    print("🧾 You can track your order in the 'My Orders' section of your account.")

def cancel_order():
    print("❌ You can cancel your order before it is shipped from the order details page.")

def return_product():
    print("📦 Products can be returned within 7 days of delivery via 'My Orders' > Return.")

def refund_status():
    print("💰 Refunds are processed within 5-7 working days after the product is picked up.")

def payment_methods():
    print("💳 We accept UPI, Debit/Credit Cards, Net Banking, and Cash on Delivery.")

def exchange_policy():
    print("🔁 Exchange is available on selected products only. Check the product page.")

def human_support():
    print("📞 Please wait while we connect you to a human agent...")
    time.sleep(2)
    print("👨‍💼 All our agents are currently busy. Please describe your issue, and we’ll get back soon!")

# Main chatbot logic
def chatbot():
    print("🤖 Chatbot:", time_based_greeting())
    print("Welcome to ShopSmart Customer Support Chat!")
    print("How can I assist you today?")

    while True:
        show_menu()
        choice = input("\nEnter your option (0-7): ")

        if choice == "1":
            track_order()
        elif choice == "2":
            cancel_order()
        elif choice == "3":
            return_product()
        elif choice == "4":
            refund_status()
        elif choice == "5":
            payment_methods()
        elif choice == "6":
            exchange_policy()
        elif choice == "7":
            human_support()
        elif choice == "0":
            print("🤖 Chatbot: Thank you for chatting with us. Have a great day! 👋")
            break
        else:
            print("❗ Invalid option. Please enter a number from 0 to 7.")

        time.sleep(1)

# Run the chatbot
chatbot()
