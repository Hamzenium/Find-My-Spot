# import requests

# API_URL = "https://api-inference.huggingface.co/models/jayanta/google-vit-base-patch16-224-cartoon-emotion-detection"
# headers = {"Authorization": "Bearer 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"}

# def query(filename):
#     with open(filename, "rb") as f:
#         data = f.read()
#     response = requests.post(API_URL, headers=headers, data=data)
#     return response.json()

# output = query("/Users/muhammadhamzasohail/Desktop/parking_street.jpeg")
# print(output)