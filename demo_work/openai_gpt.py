import openai 
openai.api_key = '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'
messages = [ {"role": "system", "content": "This is the real estate business assist."} ] 
while True: 
  message = input("Question : ") 
  if message: 
    messages.append(
      {"role": "user", "content": message}
    ) 
    chat = openai.ChatCompletion.create( 
                  model="gpt-3.5-turbo", messages=messages 
                ) 
  reply = chat.choices[0].message.content 
  print(f"Assist : {reply}") 
  messages.append({"role": "assistant", "content": reply})
