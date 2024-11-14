from flask import Flask, render_template
import csv
import PyPDF2

app = Flask(__name__)

# Function to load quotes from CSV
def load_quotes(filename="quotes.csv"):
    quotes = []
    try:
        with open(filename, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                quotes.append(row['Quote'])
        print("Quotes loaded successfully:", quotes)  # Debugging statement
    except Exception as e:
        print("Error loading quotes:", e)
    return quotes

# Function to load essays from a PDF file
def load_essays(filename="static/essays.pdf"):
    essays = []
    try:
        with open(filename, "rb") as file:
            reader = PyPDF2.PdfReader(file)
            for page_num in range(len(reader.pages)):
                page = reader.pages[page_num]
                essays.append(page.extract_text().strip())
        print("Essays loaded successfully:", essays)  # Debugging statement
    except Exception as e:
        print("Error loading essays:", e)
    return essays

# Load quotes and essays at the start
quotes = load_quotes()
essays = load_essays()

@app.route("/")
def home():
    # Debugging output to confirm data is passed to the template
    print("Rendering template with quotes and essays.")
    return render_template("index.html", quotes=quotes, essays=essays)

if __name__ == "__main__":
    app.run(debug=True)