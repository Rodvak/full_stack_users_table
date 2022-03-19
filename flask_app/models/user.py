from flask_app.config.mysqlconnection import connectToMySQL # import the function that will return an instance of a connection

class User: # model the class after the User table from our database
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
        
    @classmethod # Now we use class methods to query our database
    def get_all(cls):
        query = "SELECT * FROM users;" 
        results = connectToMySQL('users_schema').query_db(query)# make sure to call the connectToMySQL function with the schema you are targeting.
        users = [] # Create an empty list to append our instances of users
        for user in results: # Iterate over the db results and create instances of users with cls.
            users.append( cls(user) )
        return users
    
    
    @classmethod
    def save(cls, data ):
        query = "INSERT INTO users ( first_name , last_name , email, created_at, updated_at) VALUES ( %(first_name)s , %(last_name)s , %(email)s, NOW(), NOW());"
        result =  connectToMySQL('users_schema').query_db( query, data ) # data is a dictionary that will be passed into the save method from server.py
        return result
    
        #USERS CRUD (try to figure out how to print the unique user)
    @classmethod
    def get_user(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        result = connectToMySQL ('users_schema').query_db(query, data)
        if result:
            return cls(result[0])
         
    @classmethod
    def update_user(cls, data):
        query = "UPDATE users SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s, updated_at = NOW() WHERE id = %(id)s;"
        connectToMySQL ('users_schema').query_db(query, data)
        
    @classmethod
    def delete_user(cls,data):
        query = "DELETE FROM users WHERE id = %(id)s;"
        connectToMySQL ('users_schema').query_db(query, data)

