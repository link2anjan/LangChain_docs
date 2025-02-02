from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain


llm = ChatGroq(
    temperature=0, 
    groq_api_key='', 
    model_name="llama-3.3-70b-versatile"
)

 # Step 2: Define a prompt template for the task
# In this case, we're asking for a general knowledge question about the moon landing.
prompt = PromptTemplate(
    input_variables=["question"],  # Define the variable that will be replaced in the template
    template="Answer the following question: {question}"  # Template structure
)

# Step 3: Create a RunnableSequence by chaining the prompt and LLM
llm_chain = prompt | llm  # This chains the prompt with the LLM

# Step 4: Define the input question
question = "The first person to land on the moon was ..."

# Step 5: Invoke the chain with the input (using the new `invoke` method)
response = llm_chain.invoke({"question": question})


# Step 6: Print the response content (Groq model's output)
print(response.content)

question = "from where you got the answer"
response = llm_chain.invoke({"question": question})


# Step 6: Print the response content (Groq model's output)
print(response.content)
