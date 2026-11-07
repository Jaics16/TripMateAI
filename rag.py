
import re
from pathlib import Path

# Project document directory
BASE_DIR = Path(__file__).resolve().parent
DOCUMENTS_DIR = BASE_DIR / "documents"


def load_documents():
    """Load all Markdown documents from the documents folder."""

    documents = []

    if not DOCUMENTS_DIR.exists():
        return documents

    for file_path in DOCUMENTS_DIR.glob("*.md"):
        try:
            content = file_path.read_text(encoding="utf-8")

            documents.append({
                "filename": file_path.name,
                "content": content
            })

        except OSError as error:
            print(f"Could not read {file_path.name}: {error}")

    return documents


def split_into_sections(documents):
    """Split Markdown documents into heading-based sections."""

    sections = []

    for document in documents:
        content = document["content"]
        filename = document["filename"]

        # Split on Markdown headings
        parts = re.split(r"(?m)(?=^#{1,3}\s+)", content)

        for part in parts:
            part = part.strip()

            if part:
                sections.append({
                    "filename": filename,
                    "content": part
                })

    return sections


def tokenize(text):
    """Convert text into lowercase searchable words."""

    words = re.findall(r"[a-zA-Z0-9]+", text.lower())

    # Common words that do not help much with retrieval
    stop_words = {
        "the", "is", "a", "an", "and", "or", "of",
        "to", "in", "for", "on", "with", "what",
        "when", "where", "how", "are", "do", "does",
        "can", "i", "we", "you", "your", "our",
        "it", "this", "that", "about", "me", "my"
    }

    return [word for word in words if word not in stop_words]


def retrieve_relevant_documents(query, top_k=3):
    """Retrieve the most relevant document sections for a query."""

    documents = load_documents()
    sections = split_into_sections(documents)

    if not sections:
        return []

    query_words = set(tokenize(query))

    if not query_words:
        return []

    scored_sections = []

    for section in sections:
        section_words = tokenize(section["content"])
        section_word_set = set(section_words)

        # Basic keyword overlap score
        score = len(query_words.intersection(section_word_set))

        # Slightly prioritize sections that match more query terms
        if score > 0:
            scored_sections.append({
                "filename": section["filename"],
                "content": section["content"],
                "score": score
            })

    # Highest score first
    scored_sections.sort(
        key=lambda item: item["score"],
        reverse=True
    )

    return scored_sections[:top_k]


def get_knowledge_context(query, top_k=3):
    """Format retrieved sections for the Gemini assistant."""

    results = retrieve_relevant_documents(query, top_k)

    if not results:
        return "No relevant information was found in the approved company documents."

    context_parts = []

    for result in results:
        context_parts.append(
            f"Source: {result['filename']}\n"
            f"Relevance score: {result['score']}\n"
            f"{result['content']}"
        )

    return "\n\n---\n\n".join(context_parts)


if __name__ == "__main__":

    print("\n========== TRIPMATE AI RAG TEST ==========\n")

    test_questions = [
        "What is TripMateAI?",
        "Tell me about Munnar.",
        "What is the cancellation policy?",
        "Can I make a real booking?",
        "Does the application process payments?"
    ]

    for question in test_questions:

        print(f"\nQUESTION: {question}")
        print("-" * 50)

        results = retrieve_relevant_documents(question)

        if results:
            for result in results:
                print(f"\nSource: {result['filename']}")
                print(f"Score: {result['score']}")
                print(result["content"][:500])
        else:
            print("No relevant information found.")

    print("\n========== RAG TEST COMPLETED ==========")
