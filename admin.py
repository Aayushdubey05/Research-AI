
import chromadb
chroma_client = chromadb.Client()

# Importing the pdf files


# uploading the pdfs in the IPFS each pdf having a unique hash



# Converting the pdfs into structured text files using OCR
research_papers = [] # save the output of ocr into this list as dictonaries (also the ipfs hash)
     #format per paper
     #{ "id": 
     #  "title":
     #  "authors":
     #  "published_date":
     #  "journal":
     #  "abstract":
     #  "key_findings":
     #  "ipfs_hash":
     #  "full text": }
     


# now further structuring each paper in the research_paper[] so that we can give it to chromadb
documents = []
metadatas=[]
ids=[]

for paper in research_papers:
    documents.append(f"{paper['title']} {paper['abstract']} {paper['key_findings']}")
    metadatas.append({
        "title": paper['title'],
        "authors": paper['authors'],
        "published_date": paper['published_date'],
        "journal": paper['journal'],
        "abstract": paper['abstract'],
        "key_findings": paper['key_findings'],
        "ipfs_hash": paper['ipfs_hash'],
        "full_text": paper['full_text']
    })
    ids.append(paper['id'])

# creating a collection in chromadb and adding the documents, metadatas and ids to it
collection = chroma_client.create_collection("Research Papers")
collection.add(
    documents=documents,
    metadatas=metadatas,
    ids=ids
)













