from document_gpt.helper.conversation import create_conversation

response = create_conversation(
    'can you explain more about the online way?',
    [
        ('hi', 'Hello! How can I assist you today?'),
        ('how to get the caste certificate?', '''You can get a caste certificate in Karnataka through three different methods: online, offline, or through Janasevaka (home service). 

To apply online, you can visit the website https://sevasindhu.karnataka.gov.in/ and follow the steps mentioned there. You will need to register, provide your Aadhaar number, and fill in the required details. 

To apply offline, you can visit your nearest Nadakacheri or Bangalore One center. You will need to contact the Nadakacheri operator, carry the required documents such as Aadhaar card, voter ID, old caste certificate, etc., and pay a fee of Rs. 25. Your service will be delivered within 21 working days.

To apply through Janasevaka, you can book a slot by calling 080-4455-4455 or through the website https://janasevaka.karnataka.gov.in/index_eng.html#. The Janasevaka executive will visit your location on the scheduled date and time. You will need to provide the required documents and pay a fee of Rs. 155. Your service will be delivered within 21 working days.

Please note that these instructions are specific to Karnataka. The process may vary in other states.''')
    ]
)

print(response)
