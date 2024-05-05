# smtp_configurations.py
# Define SMTP server configurations
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Define SMTP server configurations
smtp_servers = [
    # Gmail
    {
        'smtp_server': 'smtp.gmail.com',
        'smtp_port': 587,
        'sender_email': os.getenv('SENDER_EMAIL'),
        'sender_password': os.getenv('SENDER_PASSWORD')
    },
    # Office 365
    {
        'smtp_server': 'smtp.office365.com',
        'smtp_port': 587,
        'sender_email': os.getenv('SENDER_EMAIL'),
        'sender_password': os.getenv('SENDER_PASSWORD')
    },
    # Yahoo Mail
    {
        'smtp_server': 'smtp.mail.yahoo.com',
        'smtp_port': 587,
        'sender_email': os.getenv('SENDER_EMAIL'),
        'sender_password': os.getenv('SENDER_PASSWORD')
    },
    # AOL Mail
    {
        'smtp_server': 'smtp.aol.com',
        'smtp_port': 587,
        'sender_email': os.getenv('SENDER_EMAIL'),
        'sender_password': os.getenv('SENDER_PASSWORD')
    },
    # Outlook.com
    {
        'smtp_server': 'smtp-mail.outlook.com',
        'smtp_port': 587,
        'sender_email': os.getenv('SENDER_EMAIL'),
        'sender_password': os.getenv('SENDER_PASSWORD')
    },
    # Zoho Mail
    {
        'smtp_server': 'smtp.zoho.com',
        'smtp_port': 587,
        'sender_email': os.getenv('SENDER_EMAIL'),
        'sender_password': os.getenv('SENDER_PASSWORD')
    },
    # iCloud Mail
    {
        'smtp_server': 'smtp.mail.me.com',
        'smtp_port': 587,
        'sender_email': os.getenv('SENDER_EMAIL'),
        'sender_password': os.getenv('SENDER_PASSWORD')
    },
    # Comcast Mail
    {
        'smtp_server': 'smtp.comcast.net',
        'smtp_port': 587,
        'sender_email': os.getenv('SENDER_EMAIL'),
        'sender_password': os.getenv('SENDER_PASSWORD')
    },
    # AT&T Mail
    {
        'smtp_server': 'smtp.att.yahoo.com',
        'smtp_port': 587,
        'sender_email': os.getenv('SENDER_EMAIL'),
        'sender_password': os.getenv('SENDER_PASSWORD')
    },
    # GMX Mail
    {
        'smtp_server': 'smtp.gmx.com',
        'smtp_port': 587,
        'sender_email': os.getenv('SENDER_EMAIL'),
        'sender_password': os.getenv('SENDER_PASSWORD')
    },
    # Mail.com
    {
        'smtp_server': 'smtp.mail.com',
        'smtp_port': 587,
        'sender_email': os.getenv('SENDER_EMAIL'),
        'sender_password': os.getenv('SENDER_PASSWORD')
    },
    # ProtonMail
    {
        'smtp_server': 'smtp.protonmail.com',
        'smtp_port': 587,
        'sender_email': os.getenv('SENDER_EMAIL'),
        'sender_password': os.getenv('SENDER_PASSWORD')
    },
    # 163.com
    {
        'smtp_server': 'smtp.163.com',
        'smtp_port': 25,
        'sender_email': os.getenv('SENDER_EMAIL'),
        'sender_password': os.getenv('SENDER_PASSWORD')
    },
    # 126.com
    {
        'smtp_server': 'smtp.126.com',
        'smtp_port': 25,
        'sender_email': os.getenv('SENDER_EMAIL'),
        'sender_password': os.getenv('SENDER_PASSWORD')
    },
    # QQ Mail (Tencent)
    {
        'smtp_server': 'smtp.qq.com',
        'smtp_port': 587,
        'sender_email': os.getenv('SENDER_EMAIL'),
        'sender_password': os.getenv('SENDER_PASSWORD')
    },
    # Sina Mail
    {
        'smtp_server': 'smtp.sina.com',
        'smtp_port': 25,
        'sender_email': os.getenv('SENDER_EMAIL'),
        'sender_password': os.getenv('SENDER_PASSWORD')
    },
    # Sohu Mail
    {
        'smtp_server': 'smtp.sohu.com',
        'smtp_port': 25,
        'sender_email': os.getenv('SENDER_EMAIL'),
        'sender_password': os.getenv('SENDER_PASSWORD')
    },
    # Tencent Enterprise Mail
    {
        'smtp_server': 'smtp.exmail.qq.com',
        'smtp_port': 25,
        'sender_email': os.getenv('SENDER_EMAIL'),
        'sender_password': os.getenv('SENDER_PASSWORD')
    },
    # Alibaba Cloud Mail (Aliyun)
    {
        'smtp_server': 'smtpdm.aliyun.com',
        'smtp_port': 80,
        'sender_email': os.getenv('SENDER_EMAIL'),
        'sender_password': os.getenv('SENDER_PASSWORD')
    },
    # NetEase Mail
    {
        'smtp_server': 'smtp.ym.163.com',
        'smtp_port': 25,
        'sender_email': os.getenv('SENDER_EMAIL'),
        'sender_password': os.getenv('SENDER_PASSWORD')
    },
    # Yahoo! Mail China
    {
        'smtp_server': 'smtp.mail.yahoo.com.cn',
        'smtp_port': 587,
        'sender_email': os.getenv('SENDER_EMAIL'),
        'sender_password': os.getenv('SENDER_PASSWORD')
    },
    # Tianyi Cloud (China Telecom)
    {
        'smtp_server': 'smtp.189.cn',
        'smtp_port': 25,
        'sender_email': os.getenv('SENDER_EMAIL'),
        'sender_password': os.getenv('SENDER_PASSWORD')
    },
    # Foxmail (Tencent)
    {
        'smtp_server': 'smtp.foxmail.com',
        'smtp_port': 25,
        'sender_email': os.getenv('SENDER_EMAIL'),
        'sender_password': os.getenv('SENDER_PASSWORD')
    },
    # China Mobile Mail
    {
        'smtp_server': 'smtp.139.com',
        'smtp_port': 25,
        'sender_email': os.getenv('SENDER_EMAIL'),
        'sender_password': os.getenv('SENDER_PASSWORD')
    },
    # Tom Mail
    {
        'smtp_server': 'smtp.tom.com',
        'smtp_port': 25,
        'sender_email': os.getenv('SENDER_EMAIL'),
        'sender_password': os.getenv('SENDER_PASSWORD')
    },
    # 21CN Mail
    {
        'smtp_server': 'smtp.21cn.com',
        'smtp_port': 25,
        'sender_email': os.getenv('SENDER_EMAIL'),
        'sender_password': os.getenv('SENDER_PASSWORD')
    },
    # 263.net
    {
        'smtp_server': 'smtp.263.net',
        'smtp_port': 25,
        'sender_email': os.getenv('SENDER_EMAIL'),
        'sender_password': os.getenv('SENDER_PASSWORD')
    },
    # ChinaCache Mail
    {
        'smtp_server': 'smtp.chinacache.net',
        'smtp_port': 25,
        'sender_email': os.getenv('SENDER_EMAIL'),
        'sender_password': os.getenv('SENDER_PASSWORD')
    },
    # Huawei Cloud Mail
    {
        'smtp_server': 'smtp.huaweicloud.com',
        'smtp_port': 587,
        'sender_email': os.getenv('SENDER_EMAIL'),
        'sender_password': os.getenv('SENDER_PASSWORD')
    },
    # ChinaNet Mail
    {
        'smtp_server': 'smtp.chinanetcenter.com',
        'smtp_port': 25,
        'sender_email': os.getenv('SENDER_EMAIL'),
        'sender_password': os.getenv('SENDER_PASSWORD')
    },
    # Ctrip Mail
    {
        'smtp_server': 'smtp.ctrip.com',
        'smtp_port': 25,
        'sender_email': os.getenv('SENDER_EMAIL'),
        'sender_password': os.getenv('SENDER_PASSWORD')
    },
    # Kingsoft Cloud Mail
    {
        'smtp_server': 'smtp.qcloud.com',
        'smtp_port': 25,
        'sender_email': os.getenv('SENDER_EMAIL'),
        'sender_password': os.getenv('SENDER_PASSWORD')
    },
]
