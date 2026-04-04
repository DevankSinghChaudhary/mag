import json
from chunks import chunks
from data import ask, improved_output, cycle
from prompts import analysis_prompt
from models import call_analysis, chunks_model

def main():
    raw_data = ask()

    prompt = analysis_prompt(raw_data)

    ai_output = call_analysis(prompt)

    output = improved_output(ai_output)
    data = json.loads(output)

    chunks_data = chunks(data)
    print(chunks_data)
    print(len(chunks_data))
if __name__ == "__main__":
    main()