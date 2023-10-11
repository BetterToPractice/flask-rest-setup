from flask import current_app

from project.apps.core.tokens import UserTokenGenerator


class ActivateAccountTokenGenerator(UserTokenGenerator):
    def get_data(self, user):
        return {
            **super().get_data(user),
            "is_email_confirmed": user.is_email_confirmed,
        }

    def generate_url(self, user):
        return current_app.config["FRONTEND_ACTIVATE_URL"].format(
            token=self.generate(user),
        )
