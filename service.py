from aiohttp import web
import json
import db


class BuildService:
    async def get_all(self):
        try:
            response_obj = {'status': db.select_all()}
            print('Get all builds ', db.select_all())
            return web.Response(text=json.dumps(response_obj), content_type='application/json', status=200)
        except Exception as e:
            #  Bad path where create is not set
            response_obj = {'status': 'failed', 'reason': str(e)}
            #  return failed with a status code of 500 i.e. 'Server Error'
            return web.Response(text=response_obj, status=500)

    async def get_by_id(self):
        try:
            request_id = self.query['id']
            response_obj = {'status': db.select_by_id(request_id)}
            print('Get all by id ', db.select_by_id(request_id))
            return web.Response(text=json.dumps(response_obj), content_type='application/json', status=200)
        except Exception as e:
            #  Bad path where create is not set
            response_obj = {'status': 'failed', 'reason': str(e)}
            #  return failed with a status code of 500 i.e. 'Server Error'
            return web.Response(text=json.dumps(response_obj), status=500)

    async def create(self):
        try:
            build_request = await self.json()
            db.insert(build_request)
            print('Creating new build: ', build_request )
            response_obj = {'status': 'created'}
            return web.Response(text=json.dumps(response_obj), status=200)
        except Exception as e:
            # Bad path where create is not set
            response_obj = {'status': 'failed', 'reason': str(e)}
            # return failed with a status code of 500 i.e. 'Server Error'
            return web.Response(text=json.dumps(response_obj), status=500)

    async def update(self):
        try:
            build_request = await self.json()
            db.update(build_request)
            print('Creating new build: ', build_request)
            response_obj = {'status': 'added'}
            return web.Response(text=json.dumps(response_obj), content_type='application/json', status=200)
        except Exception as e:
            #  Bad path where create is not set
            response_obj = {'status': 'failed', 'reason': str(e)}
            #  return failed with a status code of 500 i.e. 'Server Error'
            return web.Response(text=json.dumps(response_obj), status=500)

    async def delete(self):
        try:
            build_request = await self.json()
            db.delete(build_request)
            print('Deleted: ', build_request)
            response_obj = {'status': 'deleted'}
            return web.Response(text=json.dumps(response_obj), content_type='application/json', status=200)
        except Exception as e:
            #  Bad path where create is not set
            response_obj = {'status': 'failed', 'reason': str(e)}
            #  return failed with a status code of 500 i.e. 'Server Error'
            return web.Response(text=json.dumps(response_obj), status=500)
