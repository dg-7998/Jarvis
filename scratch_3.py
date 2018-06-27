import wikipedia

while True:
    inp = input("Search about something: ")
    wikipedia.set_lang("es")
    print(wikipedia.summary(inp, sentences=2))

