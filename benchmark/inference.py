import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
from config import NUM_NEW_TOKENS

def run_inference(model_name: str, prompt: str, max_new_tokens: int = NUM_NEW_TOKENS):
    print(f"\nLoading model: {model_name}")
    tokenizer = AutoTokenizer.from_pretrained(model_name)

    dtype = torch.float16 if torch.cuda.is_available() and "12b" in model_name else torch.float32
    device = "cuda" if torch.cuda.is_available() else "cpu"

    model = AutoModelForCausalLM.from_pretrained(
        model_name,
        dtype=dtype,
        device_map="auto",
        use_safetensors=True
    )
    model.eval()

    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_new_tokens=max_new_tokens,
            do_sample=True,
            temperature=0.7,
            top_p=0.9,
            pad_token_id=tokenizer.eos_token_id
        )

    generated_text = tokenizer.decode(
        outputs[0][inputs["input_ids"].shape[-1]:],
        skip_special_tokens=True
    )

    print(f"=== Result with {model_name} ===")
    print("\n", prompt + generated_text)
    print("=" * 60)
    return generated_text
