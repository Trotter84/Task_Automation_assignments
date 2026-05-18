import os
import xml.etree.ElementTree as ET


tree = ET.parse('customers.xml')
root = tree.getroot()

dst_path = "emails"

os.makedirs(dst_path, exist_ok=True)

# ==================== EMAIL FORMAT ====================
def format_email(customer):
    email_txt = """
    Subject: Your Order Confirmation - Order {order_number}
    
    Hi {first_name},

    Thank you for your recent order from NeuShop. Here is a summary of your purchase:
    
        Order Number: {order_number}
        Item: {item}
        Order Total: ${order_total}
        Estimated Delivery: {delivery_date}
    
    If you have any questions about your order, reply to this email or contact
    us at support@NeuShop.com. Please have your order number ready when you reach out.
    
    Thanks again for shopping with us, {first_name}. We hope you enjoy your {item}!
    
    Best,
    The NeuShop Team
    """.format(
            first_name=customer.find('first_name').text,
            order_number=customer.find('order_number').text,
            item=customer.find('item').text,
            order_total=customer.find('order_total').text,
            delivery_date=customer.find('delivery_date').text
        )
    return email_txt
    

for customer in root:
    order_email = f"order_{customer.find('order_number').text}.txt"
    dst_file = os.path.join(dst_path, order_email)
    with open(dst_file, 'w') as txt_file:
        txt_file.write(format_email(customer))
    print(f"Created: {dst_path}/{order_email}")