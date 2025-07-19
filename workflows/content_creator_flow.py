from agents.resume_agent import ResumeAgent
from llm_config.ollama_mistral import get_mistral_model
from tools.obsidian_writer import write_to_obsidian
from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()


def resume_workflow():
    # Step 1: Ask user for input
    user_input = input("Ada yang bisa saya resume? ")

    # Step 2: Process input with ResumeAgent
    agent = ResumeAgent()
    processed = agent.run(user_input)
    print(processed)

    # Step 3: Ask for confirmation
    confirm = input("Simpan ke Obsidian? (y/n): ")
    if confirm.lower() == "y":
        note_title = "Resume"  # You can make this dynamic if you want
        write_to_obsidian(note_title, user_input)
    else:
        print("Tidak disimpan ke Obsidian.")


def story_workflow():
    # Step 1: Ask for story title
    title = input("Title of the story you want to compose: ")

    # Step 2: Generate story using Mistral
    mistral_model = get_mistral_model()
    prompt = f"Create a story with a title: '{title}'"
    # Use .invoke instead of __call__ for LangChain >=0.1.7
    story = mistral_model.invoke(prompt)

    print("\nThe resulting story:\n")
    print(story)

    # Step 3: Save to Obsidian
    confirm = input("Save story to Obsidian? (y/n): ")
    if confirm.lower() == "y":
        write_to_obsidian(title, story)
    else:
        print("nope?! ok man, thats fine.")
