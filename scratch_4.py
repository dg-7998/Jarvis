import wikipedia
import wolframalpha

while True:
    inp = input("Search: ")

    try:
        #wolframalpha
        app_id = "W4QQ6P-7UTV2E4TX8"
        client = wolframalpha.Client(app_id)

        res = client.query(inp)
        ans = next(res.results).text

        print(ans)
    except:
        #wikipedia
        print(wikipedia.summary(inp))