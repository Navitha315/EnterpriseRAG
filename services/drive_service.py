import os
import io

from dotenv import load_dotenv

from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload

from utils.download_tracker import load_tracker, save_tracker
from services.ingestion_service import ingest_document

load_dotenv()

SCOPES = ["https://www.googleapis.com/auth/drive"]
SERVICE_ACCOUNT_FILE = "service_account.json"

credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE,
    scopes=SCOPES
)

# Create the Drive client ONCE
service = build(
    "drive",
    "v3",
    credentials=credentials
)


def list_drive_files():

    folder_id = os.getenv("DRIVE_FOLDER_ID")

    results = service.files().list(
        q=f"'{folder_id}' in parents and trashed=false",
        fields="files(id,name,mimeType)"
    ).execute()

    return results.get("files", [])


def download_file(file_id, file_name):

    os.makedirs("documents", exist_ok=True)

    file_path = os.path.join("documents", file_name)

    request = service.files().get_media(fileId=file_id)

    with io.FileIO(file_path, "wb") as fh:

        downloader = MediaIoBaseDownload(fh, request)

        done = False

        while not done:
            _, done = downloader.next_chunk()

    return file_path


def sync_drive():

    files = list_drive_files()

    tracker = load_tracker()

    summary = {
        "downloaded": 0,
        "indexed": 0,
        "skipped": 0,
        "failed": []
    }

    for file in files:

        if file["id"] in tracker:
            summary["skipped"] += 1
            continue

        try:

            file_path = download_file(
                file["id"],
                file["name"]
            )

            tracker.append(file["id"])
            save_tracker(tracker)

            summary["downloaded"] += 1

            result = ingest_document(file_path)

            if result.get("message") == "Document already indexed":
                summary["skipped"] += 1
            else:
                summary["indexed"] += 1

        except Exception as e:

            summary["failed"].append({
                "file": file["name"],
                "error": str(e)
            })

    return summary
