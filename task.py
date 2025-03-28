import os
import requests
import jinja2
from dotenv import load_dotenv
load_dotenv()
template_loader=jinja2.FileSystemLoader("templates")
template_env = jinja2.Environment(loader=template_loader)

def render_template(template_filename,**context):
    return template_env.get_template(template_filename).render(**context)

def send_simple_message(to, subject, body, html):
    return requests.post(
        "https://api.mailgun.net/v3/sandbox5637584e609047398f0b6703adf45ee8.mailgun.org/messages",
  		auth=("api", os.getenv('1944ca3e6b213f2504bda149e543be41-f6202374-f2c62d85','1944ca3e6b213f2504bda149e543be41-f6202374-f2c62d85')),
  		data={"from": "ANUSHA K <postmaster@sandbox5637584e609047398f0b6703adf45ee8.mailgun.org>",
			"to": [to],
  			"subject": subject,
  			"text": body,
            "html": html})

def send_user_registration_email(email, username):
    return send_simple_message(
        email,
        "Successfully signed up",
        f"Hi {username}! You have successfully signed up to the StoresREST API",
        render_template("email/action.html",username=username)
	)
