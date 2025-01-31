import requests

class User:

    def get_user(self,api_url, user_id):
        response = requests.get(f"{api_url}/users/{user_id}")
        if response.status_code == 200:
            return response.json()
        raise ValueError("Error fetching the user")


