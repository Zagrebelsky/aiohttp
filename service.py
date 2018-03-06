from aiohttp import web
import json
import db



class BuildService:
    async def get_all(request):
        try:
            response_obj = { 'status' : db.select_all() }
            #здесь выдаем из базы
            print('Get all builds ', db.select_all())
            return web.Response(text=json.dumps(response_obj))
        except Exception as e:
            # Bad path where create is not set
            response_obj = { 'status' : 'failed', 'reason': str(e) }
            # return failed with a status code of 500 i.e. 'Server Error'
            return web.Response(text=json.dumps(response_obj), status=500)

    async def get_by_id(request):
        try:
            request_id = request.query['id']
            response_obj = { 'status' : db.select_by_id(request_id) }
            #здесь выдаем из базы
            print('Get all by id ', db.select_by_id(request_id))
            return web.Response(text=json.dumps(response_obj))
        except Exception as e:
            # Bad path where create is not set
            response_obj = { 'status' : 'failed', 'reason': str(e) }
            # return failed with a status code of 500 i.e. 'Server Error'
            return web.Response(text=json.dumps(response_obj), status=500)

    async def create(request):
        try:
            # happy path where name is set
            build_request = await request.json()
            # Process our new user
            db.incert(build_request)
            print('Creating new build: ', build_request )
            response_obj = { 'status' : 'added' }
            #Здесь пишем в базу
            # return a success json response with status code 200 i.e. 'OK'
            return web.Response(text=json.dumps(response_obj), status=200)
        except Exception as e:
            # Bad path where create is not set
            response_obj = { 'status' : 'failed', 'reason': str(e) }
            # return failed with a status code of 500 i.e. 'Server Error'
            return web.Response(text=json.dumps(response_obj), status=500)

    async def update(request):
        try:
            # happy path where name is set
            build_request = await request.json()
            # Process our new user
            db.incert(build_request)
            print('Creating new build: ', build_request )
            response_obj = { 'status' : 'added' }
            #Здесь пишем в базу
            # return a success json response with status code 200 i.e. 'OK'
            return web.Response(text=json.dumps(response_obj), status=200)
        except Exception as e:
            # Bad path where create is not set
            response_obj = { 'status' : 'failed', 'reason': str(e) }
            # return failed with a status code of 500 i.e. 'Server Error'
            return web.Response(text=json.dumps(response_obj), status=500)
