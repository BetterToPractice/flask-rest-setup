import enum

from sqlalchemy import Enum

from project.extensions import bcrypt, db


class User(db.Model):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False, comment="user`s name")
    email = db.Column(db.String(80), unique=True, nullable=False)
    name = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)

    profile = db.relationship("UserProfile", back_populates="user", uselist=False)

    def __str__(self):
        return self.username

    def set_password(self, raw_password):
        self.password = bcrypt.generate_password_hash(raw_password).decode("UTF-8")

    def check_password(self, password):
        try:
            return bcrypt.check_password_hash(self.password, password)
        except ValueError:
            return False


class UserProfile(db.Model):
    __tablename__ = "profile"

    class GenderEnum(enum.Enum):
        male = "male"
        female = "female"

        def __str__(self):
            return self.value

    id = db.Column(db.Integer, primary_key=True)
    gender = db.Column(Enum(GenderEnum), nullable=True)
    phone_number = db.Column(db.String(15), nullable=True)

    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), unique=True, nullable=False)
    user = db.relationship("User", back_populates="profile")
