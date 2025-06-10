from locust import HttpUser, TaskSet, task, between
from utils.data_generator import generate_user

class UserBehavior(TaskSet):

    def on_start(self):
        self.user = generate_user()
        self.client.post("/users", json=self.user)

    @task(3)
    def get_all_products(self):
        self.client.get("/products")

    @task(2)
    def get_single_product(self):
        self.client.get("/products/1")

    @task(1)
    def add_to_cart(self):
        cart_data = {
            "userId": 1,
            "date": "2020-02-03",
            "products": [{"productId": 1, "quantity": 1}]
        }
        self.client.post("/carts", json=cart_data)

    @task(1)
    def authenticate_user(self):
        self.client.post("/auth/login", json={
            "username": self.user["username"],
            "password": self.user["password"]
        })

class WebsiteUser(HttpUser):
    tasks = [UserBehavior]
    wait_time = between(1, 3)
    host = "https://fakestoreapi.com"
