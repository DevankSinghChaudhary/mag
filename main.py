from data import ask, improved_json
from prompts import analysis_prompt
from models import call_analysis

def main():
    #ASKING
    raw_data = ask()

    #PROMPTING
    prompt = analysis_prompt(raw_data)
    print(prompt)

    #CALLING AI
    ai_output = call_analysis(prompt)

    #IMPROVING JSON
    improved_output = improved_json(ai_output)
    print(improved_output)

if __name__ == "__main__":
    main()