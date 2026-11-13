from dotenv import load_dotenv
import os
load_dotenv()

def main():
    print("hello from lanchain course")
    print(os.environ.get("AZURE_OPENAI_API_KEY"))




if __name__ == "__main__":
    main()