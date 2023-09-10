import sys
import json

def execute_script(script_file):
    try:
        with open(script_file) as file:
            script_content = file.read()
            # Execute the script and get the result
            result = ...  # Run your Python script logic here
            result = 4
            # Send the result back to the extension
            response = {'result': result}
            sys.stdout.write(json.dumps(response))
            sys.stdout.flush()
    except Exception as e:
        # Send an error response back to the extension
        response = {'error': str(e)}
        sys.stdout.write(json.dumps(response))
        sys.stdout.flush()

# Read messages from the extension
while True:
    message = sys.stdin.readline().strip()
    if not message:
        break

    data = json.loads(message)
    if 'scriptFile' in data:
        script_file = data['scriptFile']
        execute_script(script_file)
