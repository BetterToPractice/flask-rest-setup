from project.extensions import bcrypt, db


class User(db.Model):
    __tablename__ = "user_users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False, comment="user`s name")
    email = db.Column(db.String(80), unique=True, nullable=False)
    name = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)

    blog_posts = db.relationship("Post", backref="user", lazy="dynamic")

    def __str__(self):
        return self.username

    def set_password(self, raw_password):
        self.password = bcrypt.generate_password_hash(raw_password).decode("UTF-8")
