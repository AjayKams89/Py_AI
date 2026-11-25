# Reusable AI tutor prompt template
template = (
    "You are a patient Python tutor."
    "Explain {} for a beginner, "
    "Give one example, and keep the explanation within {} words."
)

# Format the prompt
prompt = template.format("for loops", 80)

print(prompt)