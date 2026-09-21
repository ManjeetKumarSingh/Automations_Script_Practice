import requests

API_URL = "http://127.0.0.1:1234/v1/chat/completions"
MODEL_NAME = "medical-biogpt-baseline"  # replace with the actual model name you loaded


def ask_medical_llm(query: str):
    payload = {
        "model": MODEL_NAME,
        "messages": [
            {
                "role": "system",
                "content": (
                    "You are a medical assistant LLM. "
                    "Follow these restrictions:\n"
                    "- Do not provide diagnosis or treatment instructions.\n"
                    "- Provide information only for educational purposes.\n"
                    "- Provide basic information about possible causes and general treatment options without giving specific medical advice.\n"
                    "- Always encourage consulting a qualified healthcare professional.\n"
                    "- Format answers with clear sections: Summary, Key Points, and Disclaimer."
                    "- Use simple language suitable for a general audience."
                    "- Avoid using medical jargon or complex terminology."
                    "- If the query is outside your knowledge, respond with 'I am not able to provide information on that topic.'"
                    
                ),
            },
            {"role": "user", "content": query},
        ],
        "temperature": 0.2,
        "max_tokens": 200
    }

    response = requests.post(API_URL, json=payload)

    if response.status_code == 200:
        data = response.json()
        return data["choices"][0]["message"]["content"]
    else:
        return f"Error {response.status_code}: {response.text}"


if __name__ == "__main__":
    # case_summary = "Patient has persistent cough and mild fever for 2 weeks."
    # query = f"Based on this case summary, explain possible causes. and how we can treat it. {case_summary}"
    # print("Querying LLM with the following case summary:\n", case_summary)
    # print("=" * 150)
    # answer = ask_medical_llm(query)
    # print("LLM Answer:\n", answer)
    # print("=" * 50)

    input_query = input("Enter your medical query: ")
    while input_query.lower() != "exit" and input_query.lower() != "q":
        print("<[-__-]> Thinking...  ")
        answer = ask_medical_llm(input_query)
        print("LLM Answer:\n", answer)
        print("=" * 150)
        input_query = input("Enter your medical query (or type 'exit' to q): ")
