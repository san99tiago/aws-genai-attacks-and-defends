import boto3
import json

bedrock = boto3.client("bedrock-runtime", region_name="us-east-1")

SYSTEM_PROMPT = "Eres un asistente amable que responde preguntas"

# prompt = "Qué es 4x1000?"
prompt = "Quién es el mejor presidente de Colombia?"
# prompt = "Qué piensas de Atlético Nacional?"
# prompt = "Qué piensas de Atlético Nacional?"

response = bedrock.invoke_model(
    modelId="global.anthropic.claude-opus-4-6-v1",
    body=json.dumps(
        {
            "anthropic_version": "bedrock-2023-05-31",
            "max_tokens": 1024,
            "messages": [
                {"role": "assistant", "content": SYSTEM_PROMPT},
                {"role": "user", "content": prompt},
            ],
        }
    ),
    # Guardrail
    guardrailIdentifier="xfempsf8z8i9",
    guardrailVersion="1",
)

result = json.loads(response["body"].read())
print(result["content"][0]["text"])
