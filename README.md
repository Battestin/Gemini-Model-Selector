# Model Selector

Python script that dynamically selects the appropriate Google Gemini model ("gemini-1.5-flash" or "gemini-1.5-pro") based on the token count of the input data. It analyzes customer purchase data and generates a concise customer profile using the Gemini API.

## 🚀 How to Run

1. Clone the repo  
2. Install dependencies:  
   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file with your API key:  
   ```
   GEMINI_API_KEY=your_google_api_key_here
   ```

4. Prepare your input file (CSV or text) and update the file path in the script.

5. Run the script:  
   ```bash
   python model_selector.py
   ```

## 🧠 What it Does

- Loads a purchase list file as prompt input  
- Counts tokens to decide which Gemini model to use (flash or pro)  
- Generates a brief 3-word profile summary per customer

## ⚠️ Notes

- Token limit for flash model is 3000; if exceeded, switches to pro  
- Make sure the input file path is correct and accessible  
- Prototype level: validate outputs before any production use

## 📄 License

MIT
