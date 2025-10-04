from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama

load_dotenv()
import os


def main():
    print("Hello from langchain-course!")
    # print(os.environ.get("OPENAI_API_KEY"))
    information = '''The Wright Flyer (also known as the Kitty Hawk,[3][4] Flyer I or the 1903 Flyer) made the first sustained flight by a manned heavier-than-air powered and controlled aircraft on December 17, 1903.[1] Invented and flown by brothers Orville and Wilbur Wright, it marked the beginning of the pioneer era of aviation.

                        The aircraft is a single-place biplane design with anhedral (drooping) wings, front double elevator (a canard) and rear double rudder. It used a 12 horsepower (9 kilowatts) gasoline engine powering two pusher propellers. Employing "wing warping", it was relatively unstable and very difficult to fly.[5]

                        The Wright brothers flew it four times in a location now part of the town of Kill Devil Hills, about 4 miles (6 kilometers) south of Kitty Hawk, North Carolina. The airplane flew 852 ft (260 m) on its fourth and final flight, but was damaged on landing, and wrecked minutes later when powerful gusts blew it over.

                        The brothers shipped the wreckage back to Dayton, and the aircraft never flew again. Orville later restored it and displayed it on several occasions. The Flyer joined the Smithsonian Institution's collection of historic aircraft in 1948 after the end of a long and bitter dispute between Orville and the Institution over its refusal to recognize the Flyer as the first successful airplane. Today, it is on display in a place of honor in the National Air and Space Museum in Washington, D.C.    '''
    summary_template = '''
                        given the information {information} I want yo to create :
                        1. A short summary and two interesting facts about it
                        '''
    summary_prompt_template = PromptTemplate(input_variables = ['information'],template = summary_template)
    # llm = ChatOpenAI(temperature = 0, model ='gpt-5')
    llm = ChatOllama(temperature =0, model = 'gemma3:270m')
    chain = summary_prompt_template | llm
    response = chain.invoke(input={'information': information})
    print(response.content)
if __name__ == "__main__":
    main()
