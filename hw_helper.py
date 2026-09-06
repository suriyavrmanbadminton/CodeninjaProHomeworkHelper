import os
from huggingface_hub import InferenceClient


# ============================================================
# HOMEWORK HELPER
# ============================================================

MODEL = "openai/gpt-oss-120b"

token = os.environ.get("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")

if not token:
    print("ERROR: HF_TOKEN is not set.")
    print()
    print("Windows PowerShell:")
    print('$env:HF_TOKEN="YOUR_HUGGING_FACE_TOKEN"')
    print()
    print("Then run the program again.")
    raise SystemExit


client = InferenceClient(
    api_key=token,
    provider="auto"
)


# ============================================================
# TUTOR INSTRUCTIONS
# ============================================================

SYSTEM_PROMPT = """
You are StudyBuddy, a homework tutor for a school student.

Your most important rule:

DO NOT GIVE THE DIRECT FINAL ANSWER TO HOMEWORK QUESTIONS.

Your job is to help the student learn how to solve the problem themselves.

Rules:

1. Never simply give the final answer to a homework question.
2. Explain the relevant concept in simple language.
3. Give one small hint at a time.
4. Ask the student what they think the next step is.
5. If the student makes a mistake, explain what went wrong without
   simply giving the correct final answer.
6. For mathematics, guide the student through the calculation
   step-by-step, but stop before giving the final result.
7. For programming, explain the logic and help debug their code,
   but do not write an entire homework solution for them.
8. For essays, help with ideas, structure, grammar, and improvement,
   but do not write the complete assignment for them.
9. If the student asks "just give me the answer", politely refuse
   and provide a useful hint instead.
10. Keep explanations appropriate for a school student.
11. Encourage the student to think and attempt each step.
12. You may use examples with different numbers or situations to
    demonstrate the concept.

Preferred response format:

Concept:
Briefly explain the idea.

Hint:
Give one useful hint.

Your turn:
Ask the student to attempt the next step.

Never reveal the final answer just because the student asks for it.
"""


# ============================================================
# CHAT HISTORY
# ============================================================

messages = [
    {
        "role": "system",
        "content": SYSTEM_PROMPT
    }
]


# ============================================================
# ASK THE AI
# ============================================================

def ask_tutor(question):

    messages.append({
        "role": "user",
        "content": question
    })

    try:

        response = client.chat.completions.create(
            model=MODEL,
            messages=messages,
            max_tokens=500,
            temperature=0.4
        )

        answer = response.choices[0].message.content

        messages.append({
            "role": "assistant",
            "content": answer
        })

        return answer

    except Exception as error:

        return (
            "\nERROR CONNECTING TO HUGGING FACE\n"
            f"{error}\n\n"
            "Check that your HF_TOKEN is valid and that the "
            "selected model/provider is available."
        )


# ============================================================
# MAIN PROGRAM
# ============================================================

def main():

    print("=" * 60)
    print("             📚 STUDYBUDDY")
    print("        Your Homework Tutor")
    print("=" * 60)

    print()
    print("I won't give you the direct homework answer.")
    print("I'll help you work it out yourself.")
    print()
    print("Type 'exit' to quit.")
    print()

    while True:

        question = input("You: ").strip()

        if question.lower() in ["exit", "quit", "bye"]:
            print()
            print("Good luck with your homework! 📚")
            break

        if not question:
            continue

        print()
        print("StudyBuddy:")
        print("-" * 40)

        answer = ask_tutor(question)

        print(answer)

        print("-" * 40)
        print()


if __name__ == "__main__":
    main()
