class LocalTextLoader:

    def load_data(self, file_path=None, url=None):
        meta_data = {
            "url": "local",
        }
        if file_path:
            with open(file_path, 'r') as file:
                content = file.read()
        elif url:
            # Assuming we have a function named `download_content` to download the content from the url
            content = download_content(url)
        else:
            raise ValueError("Either file_path or url must be provided.")
        return [{
            "content": content,
            "meta_data": meta_data,
        }]

