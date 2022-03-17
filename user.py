from mysqlconnection import connectToMySQL # import the function that will return an instance of a connection
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
        query = "SELECT * FROM users;" # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('users_schema').query_db(query) # Create an empty list to append our instances of users
        users = []
        for user in results: # Iterate over the db results and create instances of users with cls.
            users.append( cls(user) )
        return users
    
    @classmethod
    def save(cls, data ):
        query = "INSERT INTO users ( first_name , last_name , email) VALUES ( %(fname)s , %(lname)s , %(mail)s);"
        result =  connectToMySQL('users_schema').query_db( query, data ) # data is a dictionary that will be passed into the save method from server.py
        return result
            