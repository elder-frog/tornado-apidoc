import tornado.ioloop
import tornado.web

from tornado_apidoc import make_apidoc_route


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        """
        @api {get} /api/hello hello world!
        @apiName hello_world
        @apiGroup hello
        @apiDescription hello world!
        @apiVersion 1.0.0

        @apiExample {curl} Example usage:
            curl -i /api/hello

        @apiSuccessExample {json} Success-Response:
            HTTP/1.1 200 OK
            {
                "hello": "world"
            }
        """
        return self.write('hello world!')


if __name__ == "__main__":
    application = tornado.web.Application([
        (r'/api/hello', MainHandler),
        make_apidoc_route(folder_path='./static')
    ])
    application.listen(5000)
    tornado.ioloop.IOLoop.current().start()
