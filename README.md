Welcome to an earlier rendition of my medical search engine project. This is part of a much larger system I am building, which incorporates a more complex and effective arsenal of technologies that allow me to build solutions at scale. I'm leaving this up here as a project you can check on to understand how to integrate several of the new AI, NLP, and vector tools that are currently available, with more "traditional" technologies/tools.

______________AR________CH____________I___TE_________CT____URE________________________________________

Backend

The backend portion of this project was developed using FastAPI, PostgreSQL, Pinecone, and OpenAI's GPT-3.5. Here's a brief overview of the backend architecture:

FastAPI: This framework was chosen for its speed and ease of use in building APIs. It serves as the core of our backend, handling requests and responses.
PostgreSQL: Our relational database management system, which stores user information, medical information, and other persistent data.
Pinecone: A vector database that allows us to perform fast and scalable similarity searches. It's used to index and search embeddings generated from medical text data.
OpenAI: We use OpenAI's GPT-4 for generating text summaries and potential diagnoses based on user-provided medical information.
LangChain: A library that simplifies working with language models and their outputs, integrating various components like prompts and parsers.


Fronted:

The frontend is built with React and Chakra UI to provide a responsive and modern user interface. As you can tell, my frontend skills are limited and pretty mid so I tried to use AI to help me as much as possible but tbh its pretty mid as well. Don't judge me plzz D: 


