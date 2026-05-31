knowledge_base = {
    "refund":
        "Refunds are generally processed within 5-7 business days after approval.",

    "delay":
        "Orders may occasionally be delayed due to logistics or weather conditions.",

    "damaged":
        "Damaged products can be replaced within 7 days of delivery.",

    "cancel":
        "Orders can be cancelled before they are shipped.",

    "tracking":
        "Tracking details are available in the Orders section of your account.",

    "order":
        "You can track your order using the tracking link sent via email.",

    "defective":
        "Defective products are eligible for replacement within 7 days."
}


def generate_retrieval_reply(message):

    message = message.lower()

    for keyword, answer in knowledge_base.items():

        if keyword in message:
            return answer

    return (
        "No matching support article was found in the knowledge base."
    )