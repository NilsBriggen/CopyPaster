import pyperclip
import time
from chatgpt_wrapper import ChatGPT

bot = ChatGPT()

def main():
    recent_value = ""
    pyperclip.copy("")
    while True:
        tmp_value = pyperclip.paste()
        if tmp_value != recent_value and tmp_value != "":
            recent_value = tmp_value
            interpreter(recent_value)
        time.sleep(1)

def interpreter(value):
    if value != "":
        if list(value)[0] == "?":
            try:
                response = bot.ask(value[1:])
                pyperclip.copy(response)
            except:
                print("Error: Could not get response from bot. Try again later.")

        elif list(value)[0] == "!":
            if value[1:] == "exit":
                exit()
            elif value[1:] == "search":
                pass
            elif value[1:] == "clear":
                pyperclip.copy("")
            elif value[1:] == "help":
                pyperclip.copy("Commands:\n? - Ask the bot a question\n!search - Search the web\n!clear - Clear the clipboard\n!exit - Exit the program\n!help - Show this message\n!about - Show information about this program")
            elif value[1:] == "about":
                pyperclip.copy("A fancy way to search stuff with a chatbot and similar without a UI.\nVery useful for programms that restrict access to certain things (Only for educational purposes)")
    
    return

main()