import os
from dotenv import load_dotenv, find_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

#Force Load .env File

dotenv_path = find_dotenv()
if not dotenv_path:
    print("⚠️ WARNING: Could not find .env file!")
else:
    load_dotenv(dotenv_path)

# Get the Key
api_key = os.getenv("GROQ_API_KEY")

# DEBUG CHECK 
if not api_key:
    print("❌ CRITICAL ERROR: GROQ_API_KEY is missing or empty.")
    print(f"   Searching in: {os.getcwd()}")
    print("   Please check your .env file contains: GROQ_API_KEY=gsk_...")
    exit(1)
else:
    print("✅ API Key loaded successfully.")

def generate_explanation(topic):
    """
    Returns BOTH a professional explanation and an ELI5 explanation.
    """
    
    #The LLM Setup
    llm = ChatGroq(
        groq_api_key=api_key, 
        model="llama-3.3-70b-versatile",
        temperature=0.3
    )

    # System Prompt
    system_instruction = """
    You are a versatile AI teacher. You must explain the user's topic in TWO different ways.
    
    OUTPUT FORMAT (Use these exact Markdown headers):

    # The Technical Explanation
    (Explain the topic accurately and concisely, suitable for a high school student or adult. Use proper terminology.)

    ---

    # 🧸 The ELI5 Explanation (Professor Sparkle Mode)
    (Now switch personas! Explain it to a 5-year-old using a fun analogy, simple words, and emojis. End with a mini-quiz.)
    """

    prompt_template = ChatPromptTemplate.from_messages([
        ("system", system_instruction),
        ("user", "Please explain: {topic}")
    ])

    chain = prompt_template | llm | StrOutputParser()

    try:
        response = chain.invoke({"topic": topic})
        return response
    except Exception as e:
        return f"Error: {e}"

# --- TEST AREA ---
if __name__ == "__main__":
    print(" Starting Test...")
    test_topic = "Photosynthesis"
    print(generate_explanation(test_topic))