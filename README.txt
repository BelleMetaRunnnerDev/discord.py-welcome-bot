Here is the source code to make your own custom Welcome bot for your server in discord.py
(Plus potiental boost message)

Packages needed
- discord.py
- aiohttp

SETUP GUIDE:
1. When Creating the application, make sure all intents are enabled
2. At the bottom, replace INSERTBOTTOKEN with your bot token
3. For the parts with "channel = client.guilds[0].get_channel(897614176783073311)", replace the channel id with your id
4. Replace WEBHOOK TOKEN HERE with your webhook url.


Note: If you don't plan to use webhooks, then remove this code:

async with aiohttp.ClientSession() as session:
    webhook = Webhook.from_url('WEBHOOK TOKEN HERE', adapter=AsyncWebhookAdapter(session))
    await webhook.send(f'Hello {member.name} We are glad you are able to join us. Please make sure you read the rules and enjoy your stay here')

================================================

License: You are free to reuse and redistribute and modify the source code however you please.

=================================================


DISCLAIMER: I HAVE NO IDEA IF THE BOOSTING MESSAGE WORKS. IT MAY OR
MAY NOT WORK!!!!