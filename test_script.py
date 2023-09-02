from document_gpt.helper.conversation import create_conversation

qa = create_conversation()

response = qa.run(context='Human: What is 2 plus 9?\nAI: 2 plus 9 is 11.',
                  query='Can you add 50 into that?'
                  )

print(response)
