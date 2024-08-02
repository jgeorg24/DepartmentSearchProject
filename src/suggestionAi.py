from fuzzywuzzy import process
import docx

# Function to read names from a .docx file
def load_names_from_docx(file_path):
    doc = docx.Document(file_path)
    # clean up names the document
    names = [paragraph.text.strip() for paragraph in doc.paragraphs if paragraph.text.strip()]
    return names

# store names from the file into a list called names
names = load_names_from_docx('data/Names.docx')

def suggest_name(input_name):
    # Convert the input name to uppercase for case-insensitive comparison
    input_name_upper = input_name.strip().upper()
    names_upper = [name.upper() for name in names]
    
    # Check if the input name exactly matches any name in the list
    if input_name_upper in names_upper:
        return None 
    # Find the closest matching name
    suggested_name, _ = process.extractOne(input_name, names)
    return suggested_name

if __name__ == '__main__':
    input_name = input("Enter a name: ")
    suggested_name = suggest_name(input_name)
    # If a suggestion is found, print it
    if suggested_name:
        print(f"Suggested Name: {suggested_name}")

    
