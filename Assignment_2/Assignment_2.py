from transformers import pipeline

# Load text generation model
generator = pipeline("text-generation", model="gpt2")

def ask_ai(prompt):
    response = generator(prompt, max_length=100, num_return_sequences=1)
    return response[0]['generated_text']


# -----------------------
# ZERO SHOT
# -----------------------

prompt = """
Classify sentiment.

Sentence: The phone battery drains quickly.
"""

print("\n----- ZERO SHOT -----")
print(ask_ai(prompt))


# -----------------------
# FEW SHOT
# -----------------------

prompt = """
Sentence: I love this laptop
Sentiment: Positive

Sentence: The service was terrible
Sentiment: Negative

Sentence: The battery life is amazing
Sentiment:
"""

print("\n----- FEW SHOT -----")
print(ask_ai(prompt))


# -----------------------
# CHAIN OF THOUGHT
# -----------------------

prompt = """
Solve step by step.

If a student buys 3 notebooks for 20 each
and 2 pens for 10 each,
what is the total cost?
"""

print("\n----- CHAIN OF THOUGHT -----")
print(ask_ai(prompt))


# -----------------------
# TREE OF THOUGHT
# -----------------------

prompt = """
Solve the puzzle using different reasoning paths.

Make number 24 using numbers 4,4,6,6.
"""

print("\n----- TREE OF THOUGHT -----")
print(ask_ai(prompt))


# -----------------------
# INTERVIEW PROMPT
# -----------------------

prompt = """
Act like an interviewer helping a student solve the problem.

Problem: Find average of 10,20,30,40.
Ask questions step by step.
"""

print("\n----- INTERVIEW APPROACH -----")
print(ask_ai(prompt))