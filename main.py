from aiohttp import web
from service import BuildService

app = web.Application()
app.router.add_get('/api/get', BuildService.get_all)
app.router.add_get('/api/get/id', BuildService.get_by_id)
app.router.add_post('/api/post/create', BuildService.create)
app.router.add_post('/api/post/update', BuildService.update)
app.router.add_post('/api/post/delete', BuildService.delete)
web.run_app(app, host='127.0.0.1', port=8080)
