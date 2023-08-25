import openai

openai.api_key = 'YOUR-API-KEY'
preset = [
    {'role':'system', 'content':'你的回答尽可能简短'}
]

def chat(question):
    userdic = {
        'role':'user',
        'content':question
    }
    message = preset.copy()
    message.append(userdic)
    
    response = openai.ChatCompletion.create(
        model = 'gpt-3.5-turbo',
        messages = message,
        temperature = 1,
        max_tokens = 1000
    )
    answer = response['choices'][0]['message']['content']
    promptTokens = response['usage']['prompt_tokens']
    completionTokens = response['usage']['completion_tokens']
    totalTokens = response['usage']['total_tokens']
    result = {
        'content':answer,
        'promptTokens':promptTokens,
        'completionTokens':completionTokens,
        'totalTokens':totalTokens
    }
    return result


if __name__ == "__main__":
    question = "你是谁"
    chat(question)
