class LocalTextLoader:

    def load_data(self, content, file_path=None):
        meta_data = {
            "url": "local",
        }
        if file_path:
            meta_data["file_path"] = file_path
            meta_data["file_size"] = os.path.getsize(file_path)
            meta_data["file_creation_time"] = os.path.getctime(file_path)
        return [{
            "content": content,
            "meta_data": meta_data,
        }]

