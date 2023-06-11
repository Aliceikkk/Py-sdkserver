from __main__ import app

import random
import smtplib
import re
from datetime import datetime, timedelta
from email.mime.text import MIMEText
from email.utils import formataddr
from flask import Blueprint, request, flash, jsonify
from smtplib import SMTPException
from database import get_db
from config import get_config


def generate_captcha():
    return ''.join(str(random.randint(0, 9)) for _ in range(6))


def send_email(to, subject, body):
    config = get_config()
    from_addr = config['mail']['sender_email']
    password = config['mail']['sender_password']
    smtp_server = config['mail']['smtp_server']
    smtp_port = config['mail']['smtp_port']

    # 构建邮件内容
    message = MIMEText(body, 'plain', 'utf-8')
    message['From'] = formataddr(['米忽悠', from_addr])
    message['To'] = formataddr(['亲爱的玩家', to])
    message['Subject'] = subject

    try:
        import ssl
        context = ssl.create_default_context()

        # 使用 SMTP_SSL 创建 SMTP 连接
        with smtplib.SMTP_SSL(smtp_server, smtp_port, context=context) as smtp:
            smtp.login(from_addr, password)
            smtp.sendmail(from_addr, to, message.as_string())
    except SMTPException:
        raise Exception('邮件发送失败')


def send_captcha():
    email = request.form.get('email')

    # 验证邮箱格式是否正确
    if not re.fullmatch(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', email):
        return jsonify({'success': False, 'message': '邮箱格式错误'})

    captcha = generate_captcha()
    body = f'您的验证码是：{captcha}，有效期为15分钟，请尽快使用。'
    try:
        send_email(email, '验证码', body)
    except Exception as e:
        return jsonify({'success': False, 'message': f'验证码发送失败：{e}'})

    # 将验证码写入数据库
    db = get_db()
    cursor = db.cursor()
    expire_time = datetime.now() + timedelta(minutes=15)
    cursor.execute('INSERT INTO `captcha` (`email`, `captcha`, `expire_time`) VALUES (?, ?, ?)', (email, captcha, expire_time.timestamp()))
    db.commit()

    return jsonify({'success': True, 'message': '验证码已发送，请在邮箱中查收'})

