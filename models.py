from bot import db
class User(db.Model):
    __tablename__ = 'users'
    __table_args__ = {'sqlite_autoincrement': True}
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    discord_id = db.Column(db.Integer, nullable=False, primary_key=False)
    strikes = db.Column(db.Integer, default=0, primary_key=False)
    muted = db.Column(db.Boolean, default=False, primary_key=False)
    guild = db.Column(db.Integer, primary_key=False)
        
class CachedUser(db.Model):
    __tablename__ = "cached_users"
    __table_args__ = {'sqlite_autoincrement': True}
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    username = db.Column(db.String(32), nullable=True, primary_key=False)
    discriminator = db.Column(db.String(4), nullable=True, primary_key=False)