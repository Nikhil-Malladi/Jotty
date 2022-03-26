from pymongo import MongoClient
import pdb

class InitializeMongoDB():
    def make_connection(self):
        client = MongoClient('localhost', 27017)
        db=client['admin']
        cluster=db['Jotty']
        return cluster

class Playground():
    def __init__(self,username=None,email=None,password=None):
        self.username=username
        self.email=email
        self.password=password

    def createUser(self):
        cluster=InitializeMongoDB().make_connection()
        master_dict=dict()
        master_dict['username']=self.username
        master_dict['email']=self.email
        master_dict['password']=self.password

        # check if user exists
        query_data=cluster.find({"email":{"$eq":self.email}})
        query_data=[i for i in query_data]
        if not len(query_data):
            cluster.insert_one(master_dict)
            return {'status_code':1,'message':'Successfully created the User name and Email'}
        else:
            return {'status_code':0,'message':'User Already Exists'}

    def verifyUser(self):
        cluster=InitializeMongoDB().make_connection()
        query_data=cluster.find({"email":{"$eq":self.email}})
        query_data=[i for i in query_data]
        if len(query_data):
            return {'status_code':1,'message':'User Exists, Successfully Signed in'}
        else:
            return {'status_code':0,'message':'User details donot exist, please create new account'}
