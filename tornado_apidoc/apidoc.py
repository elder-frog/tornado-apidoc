import codecs
import json
import mimetypes
from os.path import join, getmtime, getsize, abspath

import tornado.web


class ApiDocHandler(tornado.web.RequestHandler):

    def initialize(self, folder_path=None, dynamic_url=True):
        self.folder_path = 'docs' if folder_path is None else folder_path
        self.dynamic_url = dynamic_url

    def get(self, path=None):
        if not path or path == '/':
            path = 'index.html'

        if self.dynamic_url and path == '/api_project.js':
            return self.__send_file('api_project.js')

        if self.dynamic_url and path == '/main.js':
            return self.__send_file('main.js')

        return self.__send_file(path)

    def __send_file(self, filename):
        filename = join(self.folder_path, filename.strip('/'))

        readmode = 'rb' if filename.endswith('ico') else 'r'

        with open(filename, readmode) as f:
            data = f.read()

        self.set_header('Content-Type', mimetypes.guess_type(filename)[0])
        self.set_header("Last-Modified", int(getmtime(filename)))

        return self.write(data)


def pre_add_base_url(folder_path, url_path):
    with codecs.open(join(folder_path, 'index.html'), 'r') as f:
        data = f.read()

    url_path = url_path.strip('/')
    url_path += '/'

    data = data.replace(
        '<head>',
        f"""
        <head>
          <base href="{url_path}">
        """
    )

    with codecs.open(join(folder_path, 'index.html'), 'w') as f:
        f.write(data)


def make_apidoc_route(folder_path=None, url_path=None, dynamic_url=True):
    url_path = '/docs' if url_path is None else url_path

    pre_add_base_url(folder_path, url_path)

    return (
        rf'{url_path}(.*)',
        ApiDocHandler,
        {'folder_path': folder_path, 'dynamic_url': dynamic_url}
    )
