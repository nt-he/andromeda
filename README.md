# Oscie-Bot-3
Oscie-Bot-3 is a bot that does alot of stuff :D

No I did not make this repo to avoid being sued

Make suggestions over in the Issues tab!
## Configuration
1. Create a new file called `.env`.
2. In that file, add a new line: `DISCORD_TOKEN=(token)`, replacing (token) with your bot token.
3. On the next line, put `SQLALCHEMY_URI=(database_url)`, replacing (database_url) with your database URL, for those just looking to contribute, you can simply use `sqlite:///relative/path/to/db.db`, or `sqlite:////absolute/path/to/db`. However, if you are running in production, you should use a database like [PostgreSQL](https://www.postgresql.org/).
4. (Optional) If you are in a scenario where the host of the bot is not the one who "owns" it according to Discord, you can add `TRUSTED_UERS=user,ids,seperated,by,commas` to add yourself as a trusted user.
## Setting up the `filter` cog
The `filter` cog is a filter designed to delete messages with bad words in them.
Unless you have cloned `https://github.com/mogade/badwords`, the cog will be disabled.

## Configuring the database
Run `alembic upgrade head`
