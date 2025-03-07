from openai import OpenAI
import os

api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)   

# call OpenAI api
def llm_response(prompt, question):
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": prompt}, # prompt
                {"role": "user", "content": question} # question
            ]
        )
    except Exception as e:
        print(e)
        return "LLM failed to generate a response"

    if response.choices[0].message.content is None:
        return "LLM failed to generate a response"
    return response.choices[0].message.content