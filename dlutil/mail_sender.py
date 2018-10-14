#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time: 13:58 2018/10/14
# @Author: Shen Sijie
# @File: mail_sender
# @Project: DeepLearningUtil

import smtplib
from email.mime.text import MIMEText


class MailSender(object):
    """
    A wrapped smtp mail sender
    """

    def __init__(self, user, passwd, host, port=25):
        """
        Initialize the sender
        :param user: user name
        :param passwd: password
        :param host: smtp server host name
        :param port: smtp server port, default value is 25
        """
        self.smtp = smtplib.SMTP()
        self.smtp.connect(host, port)
        self.smtp.login(user, passwd)

    def send(self, sender_address, sender_name, receivers, subject, content):
        """
        Send a message
        :param sender_address: address of sender, should be a string
        :param sender_name: name of sender, should be a string
        :param receivers: address of receivers, should be a list of strings
        :param subject: mail subject
        :param content: mail content
        :return:
        """
        message = MIMEText(content, 'plain', 'utf-8')
        message['Subject'] = subject
        message['From'] = sender_name
        message['To'] = ','.join(receivers)

        self.smtp.sendmail(sender_address, receivers, message.as_string())
