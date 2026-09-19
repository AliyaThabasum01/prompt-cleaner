def clean_prompt(prompt):
    words = prompt.split()

    if len(words) < 4:
        return f"Task: {prompt}"

    midpoint = len(words) // 2

    context = " ".join(words[:midpoint])
    task = " ".join(words[midpoint:])

    return (
        f"Goal: Complete the requested task.\n\n"
        f"Context:\n{context}\n\n"
        f"Task:\n{task}\n\n"
        f"Output:\nProvide a clear and structured response."
    )
