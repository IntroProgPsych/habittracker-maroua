items = [
    {"text": "How many days per week do you go to bed at a consistent hour?", "habit": "SleepRoutine"},
    {"text": "How many days per week do you sleep at least 7 hours?", "habit": "SleepRoutine"},
    {"text": "How many days per week do you avoid screens before bed?", "habit": "SleepRoutine"},

    {"text": "How many days per week do you exercise for at least 20 minutes?", "habit": "PhysicalActivity"},
    {"text": "How many days per week do you walk at least 30 minutes?", "habit": "PhysicalActivity"},
    {"text": "How many days per week do you stretch?", "habit": "PhysicalActivity"},

    {"text": "How many days per week do you eat at least one healthy meal?", "habit": "HealthyEating"},
    {"text": "How many days per week do you eat fruits or vegetables?", "habit": "HealthyEating"},
    {"text": "How many days per week do you drink enough water?", "habit": "HealthyEating"},

    {"text": "How many days per week do you practice mindfulness?", "habit": "Mindfulness"},
    {"text": "How many days per week do you journal or reflect?", "habit": "Mindfulness"},
    {"text": "How many days per week do you take intentional breaks?", "habit": "Mindfulness"},

    {"text": "How many days per week do you spend meaningful time with others?", "habit": "SocialConnection"},
    {"text": "How many days per week do you talk openly with someone?", "habit": "SocialConnection"},
    {"text": "How many days per week do you participate in social activities?", "habit": "SocialConnection"},
]


def get_valid_input(question):
    while True:
        try:
            value = int(input(f"{question} (0-7): "))
            if 0 <= value <= 7:
                return value
            else:
                print("Please enter a number between 0 and 7.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def interpret_score(score):
    if score >= 12:
        return "High"
    elif 6 <= score <= 11:
        return "Moderate"
    else:
        return "Low"


def main():
    totals = {
        "SleepRoutine": 0,
        "PhysicalActivity": 0,
        "HealthyEating": 0,
        "Mindfulness": 0,
        "SocialConnection": 0
    }

    print("Weekly Habit Tracker\n")

    for item in items:
        answer = get_valid_input(item["text"])
        totals[item["habit"]] += answer

    print("\nResults:\n")

    for habit, total in totals.items():
        print(f"{habit}: Score {total} → {interpret_score(total)}")


if __name__ == "__main__":
    main()

if __name__ == "__main__":
    main()
