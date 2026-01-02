from locust import HttpUser,task,between
import random

sentences = ["I love to hear your voice.You are the strongest person I know, and I admire your accomplishments so much.","I’m so amazed by you every day. I can’t believe we get to do life together.","I Hate You Text Messages","I Hate You"] 

class AppUser(HttpUser):
    wait_time = between(2,5)

    @task
    def index_page(self):
        self.client.get("/")
      

    @task
    def sentiment_page(self):
        mytext = random.choice(sentences)
        self.client.get("/sentiment/"+str(mytext))
