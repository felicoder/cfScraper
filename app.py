from flask import Flask, request, jsonify
from browser import getCF

app = Flask(__name__)

@app.route('/getCF', methods=['POST'])
def call_function():
    data = request.get_json()

    if not data or "url" not in data:
        return jsonify({"error": "Missing 'url' parameter"}), 400

    url = data["url"]
    proxy = data.get("proxy")  # Optional parameter
    delay = data.get("delay")  # Pass delay as an argument to getCF
    headless = data.get("headless")
    try:
        options = {
            "url": url,
        }
        if proxy:
            options["proxy"] = proxy  # Add proxy only if provided
        if delay:
            options["delay"] = delay
        if headless:
            options["headless"] = headless
        result = getCF(**options)

        return jsonify({"message": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run()
