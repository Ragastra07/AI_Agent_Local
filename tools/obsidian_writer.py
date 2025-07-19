import os

def write_to_obsidian(note_title, content):
    vault_path = os.getenv("OBSIDIAN_VAULT_PATH")
    note_path = os.path.join(vault_path, f"{note_title}.md")

    with open(note_path, "w") as f:
        f.write(content)
    print(f"Note '{note_title}' saved to {note_path}")
