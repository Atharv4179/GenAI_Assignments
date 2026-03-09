from transformers import GPT2Tokenizer, GPT2LMHeadModel, Trainer, TrainingArguments
from datasets import load_dataset

# Load dataset
dataset = load_dataset("text", data_files={"train": "stories.txt"})

# Load tokenizer
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
tokenizer.pad_token = tokenizer.eos_token

# Tokenize dataset
def tokenize_function(example):
    tokens = tokenizer(
        example["text"],
        truncation=True,
        padding="max_length",
        max_length=128
    )
    tokens["labels"] = tokens["input_ids"].copy()   # IMPORTANT FIX
    return tokens

tokenized_dataset = dataset.map(tokenize_function, batched=True)

# Load model
model = GPT2LMHeadModel.from_pretrained("gpt2")

# Training settings
training_args = TrainingArguments(
    output_dir="./story_model",
    num_train_epochs=3,
    per_device_train_batch_size=2,
    logging_steps=10,
    save_steps=100
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_dataset["train"]
)

# Train model
trainer.train()

# Save model
model.save_pretrained("./story_model")
tokenizer.save_pretrained("./story_model")