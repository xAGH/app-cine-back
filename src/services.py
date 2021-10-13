from flask import make_response, request, jsonify
from flask_qrcode import QRcode
from werkzeug.utils import secure_filename
from os import path, getenv

class FilesService:
    
    __ALLOWED_EXTENSIONS: dict = {
        "images": ["png", "jpg", "jpeg", "svg"],
        "files": ["xlsx", "xls", "pdf", "txt"]
    }

    @classmethod
    def allow_file(cls, filename: str):
        return '.' in filename and \
            filename.rsplit('.', 1)[1].lower() in cls.__ALLOWED_EXTENSIONS["images"] or cls.__ALLOWED_EXTENSIONS["files"]

    @classmethod
    def found_file(cls, filename: str) -> bool:
        try:
            folder = path.join(getenv("UPLOAD_FOLDER", ""))
            if path.isfile(path.join(folder, filename)):
                return True
            return False
        except Exception as e:
            raise e

    def upload(self, file):
        try:
            if file.filename == '':
                return make_response(jsonify({
                    "response": {
                        "statusCode": 400,
                        "error": "Not file selected"
                    }
                }), 400)
            if file and self.allow_file(file.filename):
                filename = secure_filename(file.filename)
                print(filename)
                print(self.found_file(filename))
                if self.found_file(filename):
                    return make_response(jsonify({
                        "response": {
                            "statusCode": 400,
                            "error": "File already exists"
                        }
                    }), 400)
                file.save(path.join(getenv("UPLOAD_FOLDER"), filename))
                response = make_response(jsonify({
                    "response": {
                        "statusCode": 201,
                        "message": f"File {filename} was upload"
                    }
                }), 201)
                return response
        except FileExistsError as fe:
            return make_response(jsonify({
                "response": {
                    "statusCode": 400,
                    "error": f"Exception: {fe}"
                }
            }), 400)
        except Exception as e:
            return make_response(jsonify({
                "response": {
                    "statusCode": 400,
                    "error": f"Error: {e}"
                }
            }), 400)


class QrcodeService:

    def create_qrcode(self):
        pass
