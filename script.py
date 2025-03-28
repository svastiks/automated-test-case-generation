from openai import OpenAI
client = OpenAI()

completion = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {
            "role": "user",
            "content": "Hey, help me analyze some test cases for the code I'm writing."
        }
    ]
)

print(completion.choices[0].message.content)