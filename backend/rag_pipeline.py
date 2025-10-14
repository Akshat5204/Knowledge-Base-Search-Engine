from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
import os


# Use environment variable OPENAI_MODEL or default to GPT-3.5
MODEL_NAME = os.environ.get("OPENAI_MODEL", "gpt-3.5-turbo")


def generate_answer(question, docs):
    """
    Generate an AI answer using retrieved context chunks.
    :param question: The user's question (string)
    :param docs: A list of text chunks (list[str])
    :return: Model-generated answer (string)
    """
    # Combine retrieved chunks into one context string
    context = "\n\n---\n\n".join(docs) if docs else ""

    # Create the prompt for the LLM
    prompt = (
        "You are a helpful assistant. Use the following context to answer the question concisely. "
        "If the answer cannot be found in the context, say 'I don’t know based on the given information.'\n\n"
        f"Context:\n{context}\n\n"
        f"Question: {question}\n\n"
        "Answer:"
    )

    # Initialize the OpenAI Chat model via LangChain
    llm = ChatOpenAI(model_name=MODEL_NAME, temperature=0)

    # Generate the model’s answer
    response = llm.predict(prompt)

    return response
