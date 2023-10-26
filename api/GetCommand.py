import requests



resp=requests.get("https://reqres.in/")
code=resp.status_code 
assert code==200, "code does not match"
print(code)

