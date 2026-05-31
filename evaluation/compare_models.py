import sys
import os

sys.path.append(os.path.abspath("."))

from notebooks.baseline_model import generate_ai_reply
from notebooks.rule_based import generate_rule_based_reply
from notebooks.retrieval_based import generate_retrieval_reply


messages = [
    "My order is delayed.",
    "I want a refund.",
    "The package arrived damaged.",
    "Where is my order?",
    "I want to cancel my order.",
    "My tracking information is not updating."
]


with open("evaluation/day3_results.txt", "w") as file:

    for msg in messages:

        file.write("\n")
        file.write("=" * 80)
        file.write("\n")

        file.write(f"MESSAGE:\n{msg}\n\n")

        file.write("BASELINE MODEL:\n")
        file.write(generate_ai_reply(msg))
        file.write("\n\n")

        file.write("RULE BASED MODEL:\n")
        file.write(generate_rule_based_reply(msg))
        file.write("\n\n")

        file.write("RETRIEVAL BASED MODEL:\n")
        file.write(generate_retrieval_reply(msg))
        file.write("\n\n")


print("Comparison completed successfully.")
print("Results saved to evaluation/day3_results.txt")