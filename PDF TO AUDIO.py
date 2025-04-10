import pyttsx3
import PyPDF2

# Ask user to input the PDF file path
file_path = input("Enter the full path to the PDF file: ")

try:
    # Open the PDF file
    with open(file_path, 'rb') as book:
        pdfReader = PyPDF2.PdfReader(book)

        # Total number of pages
        pages = len(pdfReader.pages)
        print(f"Total Pages: {pages}")

        # Initialize the speech engine
        speaker = pyttsx3.init()

        # Choose the page to read (e.g., first page = index 0)
        page = pdfReader.pages[0]
        text = page.extract_text()

        if text:
            speaker.say(text)
            speaker.runAndWait()
        else:
            print("No readable text found on the page. The page may be image-based.")

except FileNotFoundError:
    print("The file path you entered does not exist. Please check and try again.")
except Exception as e:
    print(f"An error occurred: {e}")
