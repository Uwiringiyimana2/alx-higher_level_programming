#!/usr/bin/python3
import requests
import sy

if __name__ == "__main__":
    letter = sys.argv[1] if len(sys.argv) > 1 else ""
    playload = {'q': letter}
    r = requests.post('http://0.0.0.0:5000/search_user', data=playload)

    if r.status_code == 200:
        try:
            json_data = r.json()
            if json_data:
                print("[{}] {}".format(json_data['id'], json_data['name']))
            else:
                print("No result")
        except ValueError:
            print("Not a Valid JSON")
    else:
        print("No result")
