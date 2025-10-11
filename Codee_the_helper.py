import random


def show_menu():
    print("🎯".center(40, "="))
    print("CODEE".center(40))
    print("🎯".center(40, "="))
    print('Hi! My name is Codee! How I can help you?')
    print('1) Say hello.')
    print('2) Tell a joke xD')
    print('3) Show weather. ')
    print('4) Play a guessing game.')
    print('5) Exit.')

def get_user_choise():
    choice = int(input('Please, choice the number of function -->  '))
    return choice

def greet_user():
    print('Hiiiiiiiiiiiiiiiii! Love you bro. I`m hope, you can learn python. Just keep working... Stay hard!')
    return

def tell_joke():
    jokes = ['Why wibecoder is so bad??? Because they`re so terrible that theres a vacancy for a cleaner who works for Vibecoders. So, buddy, you`d better learn from AI so you can help AI later, because it once helped you become a programmer. It`s a friend, not an employee!!!',
            'Why do programmers confuse Halloween and Christmas? Because Oct 31 = Dec 25',
            '"What do you call a person who talks to ghosts? An exorcist."',
            'It`s not a joke. I love The Herta btw <3',
            "Why did Python become so popular? It has a snake-like charm!",
            '"What did one byte say to another? See a bit - say hello!"']
    joke = random.choice(jokes)
    print(joke)
    return

def play_guessing_game():
    while True:
        secret_number = random.randint(1, 10)
        attempts = 0

        while True:
            choice = int(input('I`m wished for a random numer (1/10), try to guess. Input the number here -->  '))
            attempts += 1
            if secret_number == choice:
                print(f'You win! Well done. Your attempts: {attempts}')
                break
            elif secret_number > choice:
                print('Nah, your number is less than the guessed one. Try again. ')
            else:
                if secret_number < choice:
                    print('Nah, your number is higher than the guessed one. Try again!!!')
        
        
        play_again = input("Play again? yes or no: ")
        if play_again != 'yes':
            break

def show_weather():
    cities_weather = [
        {"city": "Stavropol", "weather": "sunny", "temp": "+24"},
        {"city": "Mosscow", "weather": "rain", "temp": "+15"},
        {"city": "Saratov", "weather": "cloudy", "temp": "+16"},
        {"city": "Sochi", "weather": "sunny", "temp": "+25"},
        {"city": "Novosibirsk", "weather": "snow", "temp": "-5"}
    ]
    
    print("\n🌤️  WEATHER IN CITIES:")
    print("=" * 30)
    for city_info in cities_weather:
        print(f"{city_info['city']}: {city_info['weather']}, {city_info['temp']}°C")
    print("=" * 30)
    return

def get_user_choice():
    choice = input("Choice the number (1-5): ")
    return choice

def main():
    print("Welcome to your personal assistant!")
    
    while True:
        show_menu()
        choice = get_user_choice()
        
        if choice == "1":
            greet_user()
        elif choice == "2":
            tell_joke()
        elif choice == "3":
            show_weather()
        elif choice == "4":
            play_guessing_game()
        elif choice == "5":
            print("Goodbye!!! 👋")
            break
        else:
            print("Wrong choice! Please, try again.")

# ===== ЗАПУСК =====
if __name__ == "__main__":
    main()
