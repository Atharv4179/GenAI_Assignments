from transformers import GPT2Tokenizer, GPT2LMHeadModel

tokenizer = GPT2Tokenizer.from_pretrained("./story_model")
model = GPT2LMHeadModel.from_pretrained("./story_model")

tokenizer.pad_token = tokenizer.eos_token

prompt = input("Enter story prompt: ")

inputs = tokenizer(prompt, return_tensors="pt")

output = model.generate(
    inputs["input_ids"],
    attention_mask=inputs["attention_mask"],
    max_length=120,
    temperature=0.9,
    top_k=50,
    top_p=0.95,
    do_sample=True,
    pad_token_id=tokenizer.eos_token_id
)

story = tokenizer.decode(output[0], skip_special_tokens=True)

print("\nGenerated Story:\n")
print(story)