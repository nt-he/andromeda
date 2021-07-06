from bot import db
class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(Integer, primary_key=True)
    discord_id = db.Column(Integer, primary_key=True, nullable=False)
    strikes = db.Column(Integer, default=0)
    muted = db.Column(Boolean, default=False)