from aiohttp import web
#from handlers import setup_routes
from service import BuildService
#app.on_startup.append(session)




app = web.Application()
app.router.add_get('/api/get', BuildService.get_all)
#app.router.add_post('/api/get/id', BuildService.get_all)
app.router.add_get('/api/get/id', BuildService.get_by_id)
app.router.add_post('/api/post/create', BuildService.create)
app.router.add_post('/api/post/update', BuildService.update)
web.run_app(app, host='127.0.0.1', port=8080)
