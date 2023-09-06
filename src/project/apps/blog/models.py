from project.extensions import db


class Category(db.Model):
    __tablename__ = "blog_categories"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)

    def __str__(self):
        return self.title


class Post(db.Model):
    __tablename__ = "blog_posts"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True, nullable=False)
    body = db.Column(db.Text(), unique=True, nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey("user_users.id"))

    def __str__(self):
        return self.title
