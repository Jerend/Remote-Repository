def main():
    print("Добро пожаловать в мое приложение!")
    
    with open('data.txt', 'r', encoding='utf-8') as file:
        content = file.read()
        print(f"Содержимое файла: {content}")
    
    with open('output.txt', 'w', encoding='utf-8') as file:
        file.write("Контент: "+ content)

if __name__ == "__main__":
    main()