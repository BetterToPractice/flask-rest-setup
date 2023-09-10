from project.extensions import db


class Post(db.Model):
    __tablename__ = "blog_post"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True, nullable=False)
    body = db.Column(db.Text(), unique=True, nullable=False)

    comments = db.relationship("Comment", back_populates="post", lazy="dynamic", cascade="all,delete-orphan")

    def __str__(self):
        return self.title


class Comment(db.Model):
    __tablename__ = "blog_comment"

    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.Text, unique=True, nullable=False)

    post_id = db.Column(db.Integer, db.ForeignKey("blog_post.id"), nullable=False)
    post = db.relationship("Post", back_populates="comments")

    def __str__(self):
        return self.body
