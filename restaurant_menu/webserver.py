import cgi
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer

# import DB CRUD operations
from database_setup import Base, Restaurant, MenuItem
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# connect to the DB and create a session
engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()



class webserverHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            if self.path.endswith('/restaurants'):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()

                restaurants = session.query(Restaurant).all()
                output = ""
                output += "<html><body>"
                output += "<a href='/restaurants/new'>Create New Restaurant</a></br><br>"
                for restaurant in restaurants:
                    output += restaurant.name
                    output += "</br></br><a href='/restaurants/{}/edit' >Edit</a></br>".format(restaurant.id)
                    output += "<a href='/restaurants/{}/delete'>Delete</a></br></br>".format(restaurant.id)
                output += "</body></html>"
                self.wfile.write(output)
                print(output)
                return

            if self.path.endswith('/restaurants/new'):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()

                output = ""
                output += "<html><body>"
                output += "<h1>Create a New Restaurant!</h1>"
                output += "<form method='POST' enctype='multipart/form-data' "
                output += "action='/restaurants/new'>"
                output += "<input name='newRestaurantName' type='text' placeholder='New Restaurant Name'>"
                output += "<input type='submit' value='Create'>"
                output += "</body></html>"
                self.wfile.write(output)
                print(output)
                return

            if self.path.endswith('/edit'):
                restaurantID = self.path.split('/')[2]
                myRestaurant = session.query(Restaurant).filter_by(id=restaurantID).one()
                if myRestaurant:
                    self.send_response(200)
                    self.send_header('Content-type', 'text/html')
                    self.end_headers()
                    output = ""
                    output += "<html><body>"
                    output += "<h1>Edit {}</h1>".format(myRestaurant.name)
                    output += "<form method='POST' enctype='multipart/form-data' action='/restaurants/{}/edit' >".format(restaurantID)
                    output += "<input name='editRestaurantName' type='text' placeholder='{}' >".format(myRestaurant.name)
                    output += "<input type='submit' value='Rename'>"
                    output += "</form>"
                    output += "</body></html>"
                    self.wfile.write(output)
                    print(output)


            if self.path.endswith('/delete'):
                restaurantID = self.path.split('/')[2]
                myRestaurant = session.query(Restaurant).filter_by(id=restaurantID).one()
                if myRestaurant:
                    self.send_response(200)
                    self.send_header('Content-type', 'text/html')
                    self.end_headers()
                    output = ""
                    output += "<html><body>"
                    output += "<h1>You are about to delete {}?</h1>".format(myRestaurant.name)
                    output += "<form method='POST' enctype='multipart/form-data' action='/restaurants/{}/delete' >".format(restaurantID)
                    output += "<input type='submit' value='Delete'></br></br>"
                    output += "<a href='/restaurants'>Cancel</a>"
                    output += "</form>"
                    output += "</body></html>"
                    self.wfile.write(output)
                    print(output)

        except IOError:
            self.send_error(404, "File not found %s" % self.path)


    def do_POST(self):
        try:
            # CRUD Create
            if self.path.endswith('/restaurants/new'):
                ctype, pdict = cgi.parse_header(
                    self.headers.getheader('content-type'))
                if ctype == 'multipart/form-data':
                    fields = cgi.parse_multipart(self.rfile, pdict)
                    message_content = fields.get('newRestaurantName')

                # Create a new restaurant object
                newRestaurant = Restaurant(name=message_content[0])
                session.add(newRestaurant)
                session.commit()

                self.send_response(301)
                self.send_header('Content-type', 'text/html')
                self.send_header('Location', '/restaurants')
                self.end_headers()

            # CRUD Edit
            if self.path.endswith('/edit'):
                ctype, pdict = cgi.parse_header(
                    self.headers.getheader('content-type'))
                if ctype == 'multipart/form-data':
                    fields = cgi.parse_multipart(self.rfile, pdict)
                    message_content = fields.get('editRestaurantName')
                    restaurantID = self.path.split('/')[2]

                    myRestaurant = session.query(Restaurant).filter_by(id=restaurantID).one()
                    if myRestaurant:
                        myRestaurant.name = message_content[0]
                        session.add(myRestaurant)
                        session.commit()

                        self.send_response(301)
                        self.send_header('Content-type', 'text/html')
                        self.send_header('Location', '/restaurants')
                        self.end_headers()

            # CRUD Delete
            if self.path.endswith('/delete'):
                restaurantID = self.path.split('/')[2]
                myRestaurant = session.query(Restaurant).filter_by(id=restaurantID).one()
                if myRestaurant:
                    session.delete(myRestaurant)
                    session.commit()

                    self.send_response(301)
                    self.send_header('Content-type', 'text/html')
                    self.send_header('Location', '/restaurants')
                    self.end_headers()

        except:
            pass


def main():
    try:
        port = 8080
        server = HTTPServer(('', port), webserverHandler)
        print("Web server running on port {}.").format(port)
        server.serve_forever()

    except KeyboardInterrupt:
        # Ctrl+C was pressed....shutdown the server
        print("^C entered, stopping web server...")
        server.socket.close()


if __name__ == '__main__':
    main()
