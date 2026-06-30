import google.generativeai as genai

genai.configure(api_key="paste your API key here")

print("\nFetching Available Models...\n")
for m in genai.list_models():
    print(m.name)
