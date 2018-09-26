import json
import sys

class MyApp:

    def dispatch(self, environ):
        query = environ['QUERY_STRING']
        method = environ['REQUEST_METHOD']
        path = environ['PATH_INFO']
        address = environ['REMOTE_ADDR']
        fileinfo = self.filereader()
        if method == 'GET':
            path_list = path.split("/")
            if len(path_list) > 1:
                inven1 = path_list[-1]
                return  fileinfo[inven1]
            else:
                inven = json.dumps(fileinfo)
                return inven

        elif method == 'PATCH':
            query_list=query.split("=")
            count = int(query_list[1])
            path_list = path.split("/")
            item = path_list[1]
            if item in fileinfo:
                fileinfo[item] += count
            else:
                fileinfo.update({item : count})


        elif method == 'DELETE':
            path_list1 = path.split("/")
            if len(path_list) > 1:
                del fileinfo[path_list1[-1]]
                return fileinfo
            else:
                # inventory = json.dumps(fileinfo)
                # remove inventory
                return "This list is empty"



        return "Your request is invalid, please try new URL"

    def filewriter(self, fileinfo):
        json.dump(fileinfo, open("inventory_api.txt", 'w'))
        return "Your inventory has been updated"

    def filereader(self):
        _dict = {}
        with open('inventory_api.txt', 'r') as f:
            _dict = json.loads(f.read())
        return _dict

