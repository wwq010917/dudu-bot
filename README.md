# Dudu - The Conversational Discord Bot

Dudu is a delightful bear bot on Discord, powered by OpenAI's GPT-3.5 Turbo. It's designed to have meaningful, mood-based conversations and suggest activities.

## Key Features

- **Powered by OpenAI**: Utilizes GPT-3.5 Turbo for natural conversations.
- **Mood-based Interactions**: Dudu's responses vary based on its current mood.
- **Memory Feature**: Remembers past interactions for context-aware conversations.
- **Dynamic Activities**: Suggests activities based on mood, time, and past actions.

## How Dudu Learns to Talk:

### Setting the Stage with OpenAI

- **API Interaction**: The code utilizes OpenAI's ChatCompletion API to create a conversation with the model. Each conversation is structured as a series of messages, alternating between the roles of "system", "user", and "assistant".
- **System's Role**: Provides high-level directives to set the behavior of the model. For Dudu, instructions ensure that the bot behaves like a lovely bear named "肚肚".
- **User's Role**: Simulates the user guiding the model through the desired outputs, such as suggesting activities for Dudu based on its current mood and time of day.
- **Temperature**: Determines the randomness of the model's output. A higher value (e.g., 0.9) produces more random outputs, while a lower value makes it more deterministic.

### Ensuring Dudu Remembers

- **Activity Logging**: Includes an `activity_log` that records Dudu's recent activities to avoid repetition in suggestions.
- **Historical Conversations**: Feeds the model with the last 10 interactions to provide context, ensuring coherent and context-aware conversations.
- **Mood and Location Context**: Informs the model about Dudu's current mood, mood score, and location, generating responses in line with Dudu's current state.

### Underlying Logic for Conversation

- **Activity Generation**: The `generate_activity` function suggests an activity for Dudu based on its mood, recent activities, and the time.
- **Sending Messages**: The `send_message` function simulates conversations, generating responses based on historical conversations, Dudu's mood, location, and recent activities.

## Setup

1. **Dependencies**: Ensure required libraries are installed.
2. **API Key**: Set the OpenAI API key in the `OPENAI_API_KEY` constant.
3. **Run**: Execute the main.py script to bring Dudu to life on Discord.

## Special Note

Built with love for my girlfriend. ❤️
