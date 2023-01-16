from transformers import GPT2LMHeadModel, GPT2Tokenizer

model_name_or_path = "sberbank-ai/rugpt3large_based_on_gpt2"

tokenizer = GPT2Tokenizer.from_pretrained(model_name_or_path)
model = GPT2LMHeadModel.from_pretrained(model_name_or_path)

text = "У лукоморья дуб зеленый"
input_ids = tokenizer.encode(text, return_tensors="pt")
out = model.generate(input_ids, do_sample=False, max_length=50, repetition_penalty=5.0, top_k=5, top_p=0.95, temperature=1, num_beams=None, no_repeat_ngram_size=3)

generated_text = list(map(tokenizer.decode, out))[0]
print()
print(generated_text)