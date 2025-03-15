import random
import datetime
import json
import os
from typing import Dict, List

class GrowthMindsetChallenge:
    def __init__(self):
        self.challenges = {
            "learning": [
                "Learn something new today and write about your experience",
                "Try a different approach to solve a problem you're facing",
                "Ask for feedback on something you're working on",
                "Practice a skill you find challenging for 20 minutes"
            ],
            "reflection": [
                "Write about a recent failure and what you learned from it",
                "Identify one area where you've shown improvement",
                "Share a challenge you overcame and how you did it",
                "Write about a time when persistence paid off"
            ],
            "mindset": [
                "Replace 'I can't' with 'I can't yet' today",
                "Write about how challenges help you grow",
                "Identify a negative thought and reframe it positively",
                "List three things you're working to improve"
            ]
        }
        self.progress_file = "growth_mindset_progress.json"
        self.load_progress()

    def load_progress(self):
        if os.path.exists(self.progress_file):
            with open(self.progress_file, 'r') as f:
                self.progress = json.load(f)
        else:
            self.progress = {
                "completed_challenges": [],
                "streak": 0,
                "last_completed": None
            }

    def save_progress(self):
        with open(self.progress_file, 'w') as f:
            json.dump(self.progress, f)

    def get_daily_challenge(self) -> str:
        """Return a random challenge from any category."""
        category = random.choice(list(self.challenges.keys()))
        return random.choice(self.challenges[category])

    def complete_challenge(self, reflection: str):
        today = datetime.datetime.now().strftime("%Y-%m-%d")
        
        # Update streak
        if self.progress["last_completed"]:
            last_date = datetime.datetime.strptime(self.progress["last_completed"], "%Y-%m-%d")
            yesterday = datetime.datetime.now() - datetime.timedelta(days=1)
            
            if last_date.date() == yesterday.date():
                self.progress["streak"] += 1
            elif last_date.date() != datetime.datetime.now().date():
                self.progress["streak"] = 1
        else:
            self.progress["streak"] = 1

        # Save completion
        self.progress["completed_challenges"].append({
            "date": today,
            "reflection": reflection
        })
        self.progress["last_completed"] = today
        self.save_progress()

    def display_stats(self):
        print("\n=== Your Growth Mindset Journey ===")
        print(f"Current Streak: {self.progress['streak']} days")
        print(f"Total Challenges Completed: {len(self.progress['completed_challenges'])}")
        
        if self.progress["completed_challenges"]:
            print("\nRecent Reflections:")
            for entry in self.progress["completed_challenges"][-3:]:
                print(f"\nDate: {entry['date']}")
                print(f"Reflection: {entry['reflection']}")

def main():
    challenge = GrowthMindsetChallenge()
    
    while True:
        print("\n=== Growth Mindset Daily Challenge ===")
        print("1. Get Today's Challenge")
        print("2. View Progress")
        print("3. Exit")
        
        choice = input("\nEnter your choice (1-3): ")
        
        if choice == "1":
            daily_challenge = challenge.get_daily_challenge()
            print(f"\nToday's Challenge: {daily_challenge}")
            
            do_challenge = input("\nWould you like to complete this challenge now? (yes/no): ")
            if do_challenge.lower() == "yes":
                reflection = input("\nWrite your reflection on the challenge:\n")
                challenge.complete_challenge(reflection)
                print("\nGreat job! Your progress has been saved.")
        
        elif choice == "2":
            challenge.display_stats()
        
        elif choice == "3":
            print("\nKeep growing! See you tomorrow!")
            break
        
        else:
            print("\nInvalid choice. Please try again.")

if __name__ == "__main__":
    main() 