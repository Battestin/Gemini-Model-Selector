import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

GOOGLE_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)

model = "gemini-1.5-flash"

def load_file(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.read()
            return content
    except IOError as e:
        print(f"Error: {e}")

user_prompt = load_file("Alura\Gemini e Python criando ferramentas com a API\Gemini - Model selector\data\purchase_list_100_customers.csv")

print(f"\nUser prompt: {user_prompt}")

full_model = genai.GenerativeModel(f"models/{model}")
token_count = full_model.count_tokens(user_prompt)

token_limit = 3000

if token_count.total_tokens >= token_limit:
    model = "gemini-1.5-pro"

print(f"\nModel used: {model}")

llm = genai.GenerativeModel(
    model_name=model,
    system_instruction="""
    Identify the purchase profile for each customers below.
    The output format should be:

    Customer - <describe the client profile in 3 words>
    """
)

response = llm.generate_content(user_prompt)
print(f"\nResponse: {response.text}")
