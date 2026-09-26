def load_document(file_path):
    with open(file_path, 'r', encoding="utf-8") as file:
        content = file.read()
    return content


document = load_document(r"C:\Users\sound\OneDrive\Desktop\Personalized-RAG-Evaluation\data\documents\machine_learing.txt")
print(document)