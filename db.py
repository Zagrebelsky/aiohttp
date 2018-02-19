import sqlalchemy

meta = sqlalchemy.MetaData()

build = sqlalchemy.Table(
    'question', meta,
    sqlalchemy.Column('name', sqlalchemy.String(200), nullable=False),
    sqlalchemy.Column('description', sqlalchemy.String(200), nullable=False),
    sqlalchemy.Column('version', sqlalchemy.Integer, nullable=False),
    sqlalchemy.Column('url', sqlalchemy.String(200), nullable=False),
    sqlalchemy.Column('owner', sqlalchemy.String(200), nullable=False),

    # Indexes #
    sqlalchemy.PrimaryKeyConstraint('id', name='build_id_pkey'))

async def init_pg(app):
    conf = app['config']['sqlite']
    engine = await aiopg.sqlalchemy.create_engine(
        database=conf['database'],
        user=conf['user'],
        password=conf['password'],
        host=conf['host'],
        port=conf['port'],
        minsize=conf['minsize'],
        maxsize=conf['maxsize'],
        loop=app.loop)
    app['db'] = engine

async def close_pg(app):
    app['db'].close()
    await app['db'].wait_closed()
