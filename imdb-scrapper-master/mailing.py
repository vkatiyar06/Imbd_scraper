import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib


host = "smtp.gmail.com"
port = 587
username = "your_email@gmail.com"  # enter your email
password = "*******"  # enter your password


def mailer(to_user, query, messages):
    from_email = username
    msg = """"""
    print(query)
    print(messages)
    for i in range(len(query)):
        msg += """TV series - """ + query[i] + \
            """\nstatus-"""+messages[i]+"""\n\n"""

    try:
        email_conn = smtplib.SMTP(host, port)
        email_conn.ehlo()
        email_conn.starttls()
        email_conn.login(username, password)
        the_msg = MIMEMultipart("alternative")
        the_msg['Subject'] = "IMDB INFO!"
        the_msg["From"] = from_email
        the_msg["To"] = to_user
        part_1 = MIMEText(msg, 'plain')
        the_msg.attach(part_1)
        email_conn.sendmail(
            from_email, [to_user], the_msg.as_string())
        email_conn.quit()
    except smtplib.SMTPException:
        print("error sending message")
