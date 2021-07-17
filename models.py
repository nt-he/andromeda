from bot import db
class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    discord_id = db.Column(db.Integer, nullable=False)
    strikes = db.Column(db.Integer, default=0)
    muted = db.Column(db.Boolean, default=False)
    guild = db.Column(db.Integer, nullable=False)
        
class CachedUser(db.Model):
    __tablename__ = "cached_users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), nullable=True)
    discriminator = db.Column(db.String(4), nullable=True)