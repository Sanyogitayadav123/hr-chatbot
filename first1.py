from key1 import KEY 
from llama_index import GPTVectorStoreIndex, SimpleDirectoryReader
from llama_index import  StorageContext
import os
os.environ['OPENAI_API_KEY'] = KEY 
def create_vector():
	documents = SimpleDirectoryReader("data").load_data()
	index = GPTVectorStoreIndex.from_documents(documents)

	# storage_context = StorageContext.from_defaults()
	index.storage_context.persist("./vectordatabase")

create_vector()
