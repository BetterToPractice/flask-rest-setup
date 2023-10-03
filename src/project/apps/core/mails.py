from flask import current_app, render_template
from flask_mail import Message

from project.extensions import mail


class BaseMailTemplate:
    subject_template_name = ""
    body_template_name = ""
    body_html_template_name = ""

    @classmethod
    def get_default_sender(cls):
        return current_app.config["MAIL_DEFAULT_SENDER"]

    def get_subject(self, context=None):
        return "".join(
            render_template(self.subject_template_name, **(context or {})).splitlines()
        )

    def get_body(self, context=None, is_html_template=False):
        body_template = (
            self.body_html_template_name if is_html_template else self.body_template_name
        )
        return render_template(body_template, **(context or {}))

    def send(self, recipients, sender=None, context=None):
        email_message = Message(
            subject=self.get_subject(context),
            sender=sender or self.get_default_sender(),
            recipients=[recipients] if isinstance(recipients, str) else recipients
        )
        email_message.body = self.get_body(context)
        email_message.html = self.get_body(context, is_html_template=True)
        mail.send(email_message)
