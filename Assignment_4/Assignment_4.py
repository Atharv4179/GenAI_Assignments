from transformers import AutoTokenizer, AutoModelForQuestionAnswering
import torch

# Load pretrained QA model
model_name = "distilbert-base-cased-distilled-squad"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForQuestionAnswering.from_pretrained(model_name)

print("AI Question Answering Chatbot")
print("Type 'exit' to stop\n")

context = """
Artificial Intelligence (AI) is a field of computer science that focuses on creating
systems capable of performing tasks that normally require human intelligence.
Machine learning is a subset of AI that allows machines to learn patterns from data.
Deep learning is a branch of machine learning that uses neural networks with many layers.
"""

while True:
    question = input("Ask a question: ")

    if question.lower() == "exit":
        break

    inputs = tokenizer(question, context, return_tensors="pt")

    with torch.no_grad():
        outputs = model(**inputs)

    start_index = torch.argmax(outputs.start_logits)
    end_index = torch.argmax(outputs.end_logits) + 1

    answer = tokenizer.decode(inputs["input_ids"][0][start_index:end_index])

    print("Answer:", answer)
    print()