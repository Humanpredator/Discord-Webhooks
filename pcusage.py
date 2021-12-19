#requirements Module
import os
from dotenv import load_dotenv
from decouple import config
from pathlib import Path
import psutil
import sched, time
from discord_webhook import DiscordWebhook, DiscordEmbed

#Other Setting
dotenv_path = Path('config.env')
load_dotenv(dotenv_path=dotenv_path)
s = sched.scheduler(time.time, time.sleep)
#MainFunction
def wh(ds):
    #DiskUsage 
    dtotal = (psutil.disk_usage('/')[0])
    dused = (psutil.disk_usage('/')[1])
    dfree = (psutil.disk_usage('/')[2])
    dper = (psutil.disk_usage('/')[3])
    #Cpu Usage
    cpu = (psutil.cpu_percent(4))
    cpuper = (psutil.cpu_percent(1))
    corecoun = (psutil.cpu_count())
    #memory Usage
    mtotal = (psutil.virtual_memory()[0])
    mused = (psutil.virtual_memory()[3])
    mfree = (psutil.virtual_memory()[4])
    mper = (psutil.virtual_memory()[2])

    #BitConversion
    def humanbytes(B):
        """Return the given bytes as a human friendly KB, MB, GB, or TB string."""
        B = float(B)
        KB = float(1024)
        MB = float(KB ** 2) # 1,048,576
        GB = float(KB ** 3) # 1,073,741,824
        TB = float(KB ** 4) # 1,099,511,627,776

        if B < KB:
            return '{0} {1}'.format(B,'Bytes' if 0 == B > 1 else 'Byte')
        elif KB <= B < MB:
            return '{0:.2f} KB'.format(B / KB)
        elif MB <= B < GB:
            return '{0:.2f} MB'.format(B / MB)
        elif GB <= B < TB:
            return '{0:.2f} GB'.format(B / GB)
        elif TB <= B:
            return '{0:.2f} TB'.format(B / TB)

    #Main Code
    webhook = DiscordWebhook(url= os.getenv('WEBHOOK_URL',None), username = os.getenv('USERNAME',None))
    embed = DiscordEmbed(title='PC Usage', description='Your PC Usage.', color='03b2f8')
    embed.set_author(name='Humanpredator', url='https://github.com/Humanpredator', icon_url='https://www.linkpicture.com/q/317712_code-repository_github_repository_resource_icon.png')
    embed.set_timestamp()
    #webhook Cpu
    embed.add_embed_field(name='CPU Usage:', inline =  True, value= str(cpu))
    embed.add_embed_field(name='No.Of Core:', inline= True, value= str(corecoun))
    embed.add_embed_field(name='CPU Percentage:', inline= True, value= str(cpuper))
    #webhook memory
    embed.add_embed_field(name='Total RAM:', inline= True, value= str("{1}".format(mtotal,humanbytes(mtotal))))
    embed.add_embed_field(name='Used RAM:', inline= True, value= str("{1}".format(mused,humanbytes(mused))))
    embed.add_embed_field(name='Free RAM:', inline= True, value= str("{1}".format(mfree,humanbytes(mfree))))
    embed.add_embed_field(name='RAM Percentage:', inline= True, value= str("{1}".format(mper,humanbytes(mper))))
    #webhook disk
    embed.add_embed_field(name='TotalDisk:', inline= True, value= str("{1}".format(dtotal,humanbytes(dtotal))))
    embed.add_embed_field(name='UsedDisk:', inline= True, value= str("{1}".format(dused,humanbytes(dused))))
    embed.add_embed_field(name='FreeDisk:', inline= True, value= str("{1}".format(dfree,humanbytes(dfree))))
    embed.add_embed_field(name='Disk Percentage:', inline= True, value= str(dper))
    webhook.add_embed(embed)
    response = webhook.execute()
    s.enter(30, 1, wh, (ds,)) #func waiting time...!
s.enter(5, 1, wh, (s,)) #initial waiting time before execution...!
s.run()