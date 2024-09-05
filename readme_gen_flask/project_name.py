from github_metadata import github_metadata_endpoint_handler
from flask import jsonify, request
import global_variables


def get_project_name():
    try:
        repository_url = request.args.get("repository_url")
        if not repository_url:
            return jsonify({"error": "Missing 'repository_url' parameter"}), 400

        if not global_variables.global_metadata:
            print("No global metadata found. Retrieving metadata.....")
            github_metadata_endpoint_handler()

        project_name_markdown = f"""
<p align="center">
    <h1 align="center">{global_variables.global_metadata.name}</h1>
</p>
            """
        return jsonify({"project_name_markdown": project_name_markdown}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500
