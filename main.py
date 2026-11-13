from dotenv import load_dotenv
import os
from langchain_core.prompts import PromptTemplate
from langchain_openai import AzureChatOpenAI
from langchain_openai import ChatOpenAI

load_dotenv()

def main():
    print("hello from lanchain course")
    

    information = """ Alan Mathison Turing (23 June 1912 – 7 June 1954) was an English mathematician and logician[6] widely regarded as the father of theoretical computer science.[7] He formalised the concepts of algorithm and computation with the Turing machine, a model of a general-purpose computer,[8][9][10] and his contributions to cryptanalysis helped the Allies of World War II decipher messages encrypted by the German Enigma machine. He also contributed the Turing test to philosophy of artificial intelligence and the Turing pattern concept to mathematical and theoretical biology. 
    Born in London and raised in southern England, Turing graduated from King's College, Cambridge, and earned a doctorate from Princeton University in 1938. During World War II, he worked at the Government Code and Cypher School at Bletchley Park, Britain's codebreaking centre, and focused on decrypting German naval messages as the head of Hut 8. His techniques improved on the pre-war Polish bomba method and hastened cryptanalysis of the Enigma ciphering system. The resulting intelligence, known as Ultra, proved helpful in the Battle of the Atlantic.[11][12] After the war, Turing joined the National Physical Laboratory, where he designed the Automatic Computing Engine, an early stored-program computer.
    In 1948, he joined Max Newman's Computing Machine Laboratory at the University of Manchester, contributing to the development of early Manchester computers.[13] He also turned to mathematical biology, working on the chemical basis of morphogenesis[14][2] and theorizing chemical oscillators independently of their experimental observation.[15] In 1952, after acknowledging a sexual relationship with another man, Turing was prosecuted for gross indecency. He received probation conditional on chemical castration and lost his security clearance. He died on 7 June 1954, aged 41, by cyanide poisoning. The inquest ruled his death a suicide.
    Turing left a lasting legacy in mathematics, computing, and codebreaking. His wartime work, covered by the Official Secrets Act, went unrecognised during his lifetime. He later received numerous honors and memorials.[15] His death was examined and interpreted by his family and biographers, who variously accepted, supported, questioned, or disputed the inquest's verdict. Following a 2009 campaign, British prime minister Gordon Brown officially apologised for the "appalling way [Turing] was treated", and Queen Elizabeth II granted Turing a pardon in 2013. The Alan Turing law refers to part of a 2017 UK law that retroactively pardoned men cautioned or convicted under the criminalisation of homosexual acts.[16]
    """
    summary_template = """
    given the information {information} about a person I want you to create:
    1. A short summary
    2. two interesting facts about them
    """
    summary_prompt_template = PromptTemplate(
    input_variables=["information"], template=summary_template
    )
    
    llm = ChatOpenAI(
    model=os.getenv("AZURE_OPENAI_DEPLOYMENT"),
    base_url=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_key=os.getenv("AZURE_OPENAI_API_KEY")

    )
    
    chain = summary_prompt_template | llm
    response = chain.invoke(input={"information": information})
    print(response.content)

if __name__ == "__main__":
    main()