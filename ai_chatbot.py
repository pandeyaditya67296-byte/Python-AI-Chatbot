import random
import datetime

class GoogleAIAssistant:
    def __init__(self, bot_name="Nexus"):
        self.bot_name = bot_name
        self.memory = {}
        
    def get_greeting(self):
        current_hour = datetime.datetime.now().hour
        if current_hour < 12:
            return "Good morning! Ready to build the future of AI?"
        elif current_hour < 17:
            return "Good afternoon! Let's solve some high-level engineering challenges."
        else:
            return "Good evening! Late-night code building leads to breakthroughs."

    def process_query(self, user_input):
        text = user_input.lower().strip()
        
        if not text:
            return "Please input a valid command or query."
            
        if "hello" in text or "hi" in text or "hey" in text:
            return f"Hello! I am {self.bot_name}, your advanced logic and AI simulation assistant designed for Google-level projects."
            
        elif "time" in text or "date" in text:
            now = datetime.datetime.now()
            return f"Current System Timestamp: {now.strftime('%Y-%m-%d %H:%M:%S')}"
            
        elif "ai" in text or "artificial intelligence" in text:
            return "Artificial Intelligence is the simulation of human intelligence in machines programmed to think, adapt, and solve complex multi-dimensional problems."
            
        elif "python" in text:
            return "Python is a high-level, interpreted programming language renowned for its dynamic semantics, robust libraries, and core dominance in AI/ML engineering."
            
        elif "google" in text:
            return "Google drives massive technological evolution through distributed systems, TensorFlow, large language models, and world-scale infrastructure."
            
        elif "exit" in text or "quit" in text or "bye" in text:
            return "EXIT"
            
        else:
            return "Fascinating query! My rule-based engine is expanding. Try asking about Google or system time."

def main():
    assistant = GoogleAIAssistant(bot_name="Nexus-AI")
    print("=" * 60)
    print(f"  {assistant.bot_name} - Advanced Intelligent Assistant v1.0")
    print("=" * 60)
    print(assistant.get_greeting())
    
    while True:
        try:
            user_input = input("User ❯ ")
            response = assistant.process_query(user_input)
            if response == "EXIT":
                print("Goodbye!")
                break
            print(f"{assistant.bot_name} ❯ {response}\n")
        except (KeyboardInterrupt, EOFError):
            break

if __name__ == "__main__":
    main()
      
