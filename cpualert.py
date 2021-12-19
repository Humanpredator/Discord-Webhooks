#requirements Module
import os
from dotenv import load_dotenv
from pathlib import Path
import psutil
import sched, time
from discord_webhook import DiscordWebhook, DiscordEmbed

#Other Setting
dotenv_path = Path('config.env')
load_dotenv(dotenv_path=dotenv_path)
s = sched.scheduler(time.time, time.sleep)

#Main Code
def wh(ds):
    cpu = (psutil.cpu_percent(4))
    if((cpu > int(os.getenv('CPU_USG_LMT')))):
        cpu = str(cpu)
        webhook = DiscordWebhook(url= os.getenv('WEBHOOK_URL',None), username = os.getenv('USERNAME',None))
        embed = DiscordEmbed(title='CPU USAGE', description='Get alert When Cpu Uage exceeds.', color='03b2f8')
        embed.set_author(name='Humanpredator', url='https://github.com/Humanpredator', icon_url='https://www.linkpicture.com/q/317712_code-repository_github_repository_resource_icon.png')
        embed.set_footer(text='***Warning Usage Exceeded***')
        embed.set_timestamp()
        embed.add_embed_field(name='CPU Usage:', value= cpu )
        webhook.add_embed(embed)
        response = webhook.execute()
    s.enter(10, 1, wh, (ds,)) #func waiting time...!
s.enter(5, 1, wh, (s,)) #initial waiting time before execution...!
s.run()
