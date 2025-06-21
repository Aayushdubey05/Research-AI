from openai import OpenAI
import os
import chromadb

# Initialize client
chroma_client = chromadb.Client()
ai_client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY")
)

# Load research papers collection
collection = chroma_client.get_collection("Research Papers")

# Get user query
user_input = input("Enter Your Query: ")

# Search for similar papers using vector search
search_results = collection.query(
    query_texts=[user_input],
    n_results=3,  # Get top 3 relevant papers
    include=["metadatas"]
)

# Extract paper metadata from search results
paper_metadata_list = []
for metadata in search_results["metadatas"][0]:
    paper_metadata_list.append(metadata)

# Get full text content from each paper
paper_texts = []
for paper in paper_metadata_list:
    paper_texts.append(paper['full_text'])

# Create prompt for AI model
prompt = [
    {
        "role": "system",
        "content": "You are a research assistant. Answer questions only using the provided research papers. If the answer is not in the papers, respond with: 'I cannot answer this question as it is out of my scope'"
    },
    {
        "role": "user", 
        "content": f"Research Papers: {paper_texts}\n\nQuestion: {user_input}"
    }
]

# Generate response using AI model
response = ai_client.chat.completions.create(
    model="model_name",
    messages=prompt
)

# Print the answer
answer = response.choices[0].message.content
print(answer)