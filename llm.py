import ollama

MODEL_A = "qwen2.5:7b"
MODEL_B = "mistral:7b"

def ask(model, prompt):
    response = ollama.chat(
        model=model,
        messages=[{"role": "user", "content": prompt}]
    )
    return response['message']['content']


task = "Design a smart home system using ESP32 and sensors"

prompt_A = f"""
You are an expert system designer.
Propose a detailed solution for: {task}
"""

answer_A = ask(MODEL_A, prompt_A)
print("\n--- LLM A (Planner) ---\n", answer_A)

for i in range(3):  # 3 rounds of improvement
    prompt_B = f"""
You are a strict reviewer.
Find flaws, missing parts, and improvements in this plan:

{answer_A}
"""
    critique = ask(MODEL_B, prompt_B)
    print(f"\n--- LLM B (Critic) Round {i+1} ---\n", critique)

    prompt_A = f"""
Improve your previous plan based on this critique:

PLAN:
{answer_A}

CRITIQUE:
{critique}
"""
    answer_A = ask(MODEL_A, prompt_A)
    print(f"\n--- LLM A Improved Round {i+1} ---\n", answer_A)
