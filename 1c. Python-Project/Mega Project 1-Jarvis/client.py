from openai import OpenAI

client = OpenAI(
    api_key="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"
)

completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {
            "role": "system",
            "content": "You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud",
        },
        {"role": "user", "content": "what is coding"},
    ],
)

print(completion.choices[0].message.content)
