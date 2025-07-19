from workflows.content_creator_flow import resume_workflow, story_workflow
from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()


def main():
    story_workflow()


if __name__ == "__main__":
    main()
