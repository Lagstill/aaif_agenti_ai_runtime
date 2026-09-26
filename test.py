import os

import anthropic

# Talks to Claude through the ASAPP LiteLLM proxy, not api.anthropic.com. Export first:
#   export ANTHROPIC_BASE_URL=https://litellm.test.asapp.com
#   export ANTHROPIC_AUTH_TOKEN=sk-...
# The proxy uses its own model names; list them with:
#   curl -s $ANTHROPIC_BASE_URL/v1/models -H "Authorization: Bearer $ANTHROPIC_AUTH_TOKEN"
client = anthropic.Anthropic(
    base_url=os.environ["ANTHROPIC_BASE_URL"],
    auth_token=os.environ["ANTHROPIC_AUTH_TOKEN"],  # sent as "Authorization: Bearer ..."
)

message = client.messages.create(
    model="claude-4.5-sonnet",  # LiteLLM's name for claude-sonnet-4-5
    max_tokens=100,
    messages=[{"role": "user", "content": "Hey Claude, tell me a short fun fact about bees!"}],
)
print(message.model, "->", message.content[0].text)
