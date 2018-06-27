import wolframalpha

inp = input("Question: ")
app_id = "W4QQ6P-7UTV2E4TX8"
client = wolframalpha.Client(app_id)

res = client.query(inp)
ans = next(res.results).text

print(ans)
