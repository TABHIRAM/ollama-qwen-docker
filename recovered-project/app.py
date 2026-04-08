import requests
import os

OLLAMA_URL = os.getenv("OLLAMA_URL", "http://host.docker.internal:11434")

def ask_ollama(prompt):
    response = requests.post(
        f"{OLLAMA_URL}/api/generate",
        json={
            "model": "qwen2.5-coder:7b",  # or "qwen3-vl:4b"
            "prompt": prompt,
            "stream": False
        }
    )

    return response.json()["response"]


if __name__ == "__main__":
    print("🔥 Ollama Chat (Docker) Ready!")
    print("Type 'exit' to quit.\n")

    while True:
        user_input = input("👉 You: ")

        if user_input.lower() == "exit":
            print("👋 Exiting...")
            break

        response = ask_ollama(user_input)

        print("\n🤖 Model:\n")
        print(response)
        print("\n" + "-"*50 + "\n")