import requests

GITHUB_API_URL = "https://api.github.com"
OWNER = "username-or-org"
REPO = "repo-name"
TOKEN = "YOUR_TOKEN"

HEADERS = {
    "Accept": "application/vnd.github+json",
    "Authorization": f"Bearer {TOKEN}",
    "X-GitHub-Api-Version": "2022-11-28"
}


def list_workflow_runs():
    """
    List all workflow runs for the specified repository.
    Returns a list of workflow run IDs.
    """
    url = f"{GITHUB_API_URL}/repos/{OWNER}/{REPO}/actions/runs"
    response = requests.get(url, headers=HEADERS)

    if response.status_code == 200:
        runs = response.json().get("workflow_runs", [])
        run_ids = [run['id'] for run in runs]
        return run_ids
    else:
        print(f"Error fetching workflow runs: {response.status_code} - {response.text}")
        return []


def delete_workflow_run(run_id):
    """
    Delete a workflow run by its ID.
    """
    url = f"{GITHUB_API_URL}/repos/{OWNER}/{REPO}/actions/runs/{run_id}"
    response = requests.delete(url, headers=HEADERS)

    if response.status_code == 204:
        print(f"Successfully deleted run ID: {run_id}")
    else:
        print(f"Error deleting run ID {run_id}: {response.status_code} - {response.text}")


def main():
    # Step 1: List all workflow runs
    run_ids = list_workflow_runs()

    if not run_ids:
        print("No workflow runs found.")
        return

    print(f"Found {len(run_ids)} workflow runs. Deleting...")

    # Step 2: Loop through each run and delete it
    for run_id in run_ids:
        delete_workflow_run(run_id)


if __name__ == "__main__":
    main()
