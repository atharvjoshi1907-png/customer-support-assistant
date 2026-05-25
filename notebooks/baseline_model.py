from transformers import pipeline

print("Loading model...")

generator = pipeline(
    "text-generation",
    model="distilgpt2"
)

prompt = """
You are a professional customer support assistant.

Customer: My order has not arrived yet and I am upset.

Support Agent:
"""

response = generator(
    prompt,
    max_new_tokens=40,
    temperature=0.4,
    repetition_penalty=1.5,
    do_sample=True,
    truncation=True
)

generated_text = response[0]["generated_text"]

reply = generated_text.split("Support Agent:")[-1]

print("\nGenerated Reply:\n")
print(reply.strip())