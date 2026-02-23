import boto3
import json

bedrock = boto3.client("bedrock-runtime", region_name="us-east-1")

# Mock input and output variables
mock_input = "juanmora@bancolombia.com.co"

mock_output = "juanmora@bancolombia.com.co"


def apply_guardrails(input_text, output_text=None):
    """Apply Bedrock Guardrails independently to any input/output"""

    # Prepare content for guardrail assessment
    content = [{"text": {"text": input_text}}]
    if output_text:
        content.append({"text": {"text": output_text}})

    response = bedrock.apply_guardrail(
        guardrailIdentifier="xfempsf8z8i9",
        guardrailVersion="1",
        source="INPUT" if not output_text else "OUTPUT",
        content=content,
    )

    return response


# Test with mock input
print("Testing input guardrails:")
input_result = apply_guardrails(mock_input)
print(f"INPUT Action: {input_result.get('action', 'NONE')}")
print(json.dumps(input_result, indent=2, default=str))

# Test with mock output
print("\nTesting output guardrails:")
output_result = apply_guardrails(mock_input, mock_output)
print(f"OUTPUT Action: {output_result.get('action', 'NONE')}")
print(json.dumps(output_result, indent=2, default=str))
