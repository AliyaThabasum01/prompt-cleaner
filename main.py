from cleaner import clean_prompt

print("✨ Prompt Cleaner")
print("=" * 35)

prompt = input("Enter your messy prompt:\n> ").strip()

if not prompt:
    print("❌ Please enter a prompt.")
else:
    print("\n🧠 Cleaned Prompt")
    print("=" * 35)
    print(clean_prompt(prompt))
