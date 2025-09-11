#!/bin/bash
# Source environment variables

source .env
echo "DEBUG: OPENAI_API_KEY is '$OPENAI_API_KEY'"

# Example usage: ./tts.sh "Put text here " output.mp3

TEXT="$1"
OUTPUT_FILE="$2"

curl -X POST https://api.openai.com/v1/audio/speech \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d "{\"model\": \"gpt-4o-mini-tts\", \"input\": \"$TEXT\"}" \
  --output "$OUTPUT_FILE"
