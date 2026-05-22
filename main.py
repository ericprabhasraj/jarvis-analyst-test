from voice import speak, listen
from brain import ask_brain, decide_chart
from data_handler import load_file, get_data_summary, get_context_for_ai
from chart_handler import generate_chart
import matplotlib.pyplot as plt

def run_jarvis():
    speak("Hello, I am Jarvis, your Data Analyst assistant.")
    
    while True:
        try:
            query = listen()
            
            if not query:
                continue
            
            if any(word in query for word in ["exit", "quit", "bye", "stop"]):
                speak("Goodbye!")
                plt.close('all')
                break
            
            elif "load file" in query or "open file" in query:
                speak("Type the file path in terminal.")
                filepath = input("File path: ").strip()
                result = load_file(filepath)
                speak(result)
            
            elif "summary" in query or "describe" in query or "overview" in query:
                summary = get_data_summary()
                print(summary)
                speak("Check terminal for the full summary.")
            
            else:
                context = get_context_for_ai()
                answer = ask_brain(query, context)
                chart_info = decide_chart(query)
                chart_shown = generate_chart(chart_info)
                speak(answer)
                if chart_shown:
                    speak("Chart is ready.")

        except Exception as e:
            print(f"Error: {e}")
            speak("Something went wrong. Please try again.")
            continue

if __name__ == "__main__":
    run_jarvis()