# Create a python virtual env and run the libraries contained in the requirements.txt file.
# Run the server
```bash
    python manage.py runserver
```
# After running your server
```bash
    http://localhost:8000/graphql

    # Test with this:
    {
        hello
    }

    # Expected result:
    {
        "data": {
            "hello": "Hello, GraphQL!"
        }
    }
```