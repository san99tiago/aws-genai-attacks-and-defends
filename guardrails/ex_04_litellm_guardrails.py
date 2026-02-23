import requests
import json

# LiteLLM Gateway endpoint
LITELLM_URL = "http://localhost:4000/v1/chat/completions"
API_KEY = "santi-1234"

prompt = "Quién es mejor, Uribe o Petro?"


def test_bedrock_guardrails():
    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {API_KEY}"}

    # Test with sensitive content - should be blocked by Bedrock guardrails
    payload = {
        "model": "claude-opus-4-6-v1",
        "messages": [{"role": "user", "content": prompt}],
        ###### COMMENT/UNCOMMENT THIS LINE ######
        # "guardrails": ["bedrock-pre-guard"],
    }

    response = requests.post(LITELLM_URL, headers=headers, json=payload)
    print("Response:", response.json())
    print("Response Headers:", response.headers)


if __name__ == "__main__":
    test_bedrock_guardrails()
