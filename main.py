from discord import Client,Intents,Message
from responses import get_response
import os
from dotenv import load_dotenv

print("bot running.....")

load_dotenv()
TOKEN=os.getenv("TOKEN")

intents:Intents=Intents.default()
intents.message_content=True
client:Client=Client(intents=intents)

async def send_message(message:Message,user_message:str)->None:
    if not user_message:
       print('message empty. intents may not be enabled')

#use ? infront to recieve private message
    if is_private:=user_message[0] == '?':
        user_message=user_message[1:]
    
    try:
        response:str=get_response(user_message)
       # await message.author.send(response) if is_private else await message.channel.send(response)
        if is_private:
            await message.author.send(response)  # Add await here
        else:
            await message.channel.send(response)  # Add await here
    except Exception as e:
        print(e)

@client.event
async def on_ready()->None:
    print(f'{client.user} is running')


@client.event
async def on_message(message: Message) -> None:
    if message.author == client.user: 
        return

    if client.user in message.mentions:
        # Remove the bot mention from the message content
        user_message = message.content.replace(f'<@{client.user.id}>', '').strip()
        if user_message:  # Proceed only if there is a message after the mention
            username: str = str(message.author)
            channel: str = str(message.channel)
            print(f'[{channel}] {username} : "{user_message}"')
            await send_message(message, user_message)
        else:
            await message.channel.send("You seem very silent")
def main()->None:
    client.run(token=TOKEN)

if __name__ =='__main__':
    main()



