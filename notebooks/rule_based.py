def generate_rule_based_reply(message):

    message = message.lower()

    if "refund" in message:
        return (
            "We apologize for the inconvenience. "
            "Your refund request has been forwarded to our billing team. "
            "You will receive an update within 2-3 business days."
        )

    elif "delay" in message or "late" in message:
        return (
            "We are sorry for the delay in your order. "
            "Our logistics team is currently investigating the issue and "
            "will provide an update shortly."
        )

    elif "damaged" in message or "broken" in message:
        return (
            "We apologize for receiving a damaged product. "
            "Please share photos of the item and packaging so we can assist "
            "with a replacement or refund."
        )

    elif "cancel" in message:
        return (
            "Your cancellation request has been received. "
            "Our team will verify the order status and process the request."
        )

    elif "where is my order" in message or "track" in message:
        return (
            "We are checking the current status of your shipment. "
            "You will receive tracking information shortly."
        )

    else:
        return (
            "Thank you for contacting customer support. "
            "Our support team will review your concern and get back to you soon."
        )